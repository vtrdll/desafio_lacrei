from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profissional, Consulta


urls = ['/api/profissionais/',
        '/api/consultas/']


class UserAuthTests(APITestCase):
    '''
    testes de e login '''
    def setUp(self):
        self.user = User.objects.create_user(
            username="teste", password="P@ss@aa@#531**46"
        )
        self.token_url = reverse("token_obtain_pair")

    def test_login_jwt_sucesso(self):
        data = {"username": "teste", "password": "P@ss@aa@#531**46"}
        response = self.client.post(self.token_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_jwt_erro_credenciais(self):
        data = {"username": "teste", "password": "senha_errada"}
        response = self.client.post(self.token_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)
        self.assertEqual(
            str(response.data["detail"]),
            "No active account "
            "found with the given credentials",
        )


class AuthRequiredTest(APITestCase):
    '''
    testes de autenticação '''

    def test_sem_token(self):
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(
                response.status_code,
                status.HTTP_401_UNAUTHORIZED
            )

    def test_com_token(self):
        user = User.objects.create_user('joao2', '1234')
        refresh = RefreshToken.for_user(user)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
        )

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class AdminCrudTest(APITestCase):
    '''
    testes de permissão admin/usuario '''

    def authenticate(self, user):
        token = RefreshToken.for_user(user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {token.access_token}'
        )

    def setUp(self):

        self.user = User.objects.create_user(
            username='user',
            password='123'
        )
        self.admin = User.objects.create_superuser(
            username='admin',
            password='123'
        )

        self.profissional = Profissional.objects.create(
            nome='Maria',
            profissao='Esteticista',
            endereco='Rua X',
            contato='vitordossantos88@hotmail.com'
        )

        self.consulta = Consulta.objects.create(
             profissional=self.profissional,
        )

        self.url_profissional = reverse(
            'profissional-detail',
            args=[self.profissional.id]
        )

        self.url_consulta = reverse(
            'consulta-detail',
            args=[self.consulta.id]
        )

    def test_user_comum_nao_cria(self):
        self.authenticate(self.user)

        data_profissionais = {
            "nome": "Maria JOse",
            "profissao": "Esteticista",
            "endereco": "Rua Y",
            "contato": "novo@email.com"
        }

        data_consultas = {"profissional": self.profissional.id}

        resp_profissionais = self.client.post(
            '/api/profissionais/', data=data_profissionais, format='json'
        )
        resp_consultas = self.client.post(
            '/api/consultas/', data=data_consultas, format='json'
        )
        self.assertEqual(
            resp_profissionais.status_code,
            status.HTTP_403_FORBIDDEN
        )
        self.assertEqual(resp_consultas.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_comum_nao_edita(self):
        self.authenticate(self.user)

        data_profissionais = {
            "nome": "Maria Editada",
            "profissao": "Esteticista",
            "endereco": "Rua Y",
            "contato": "novo@email.com"
        }

        data_consulta = {"profissional": self.profissional.id}

        resp_profissional = self.client.put(
            self.url_profissional,
            data=data_profissionais,
            format='json'
        )
        resp_consulta = self.client.put(
            self.url_consulta,
            data=data_consulta,
            format='json'
        )

        self.assertEqual(
            resp_profissional.status_code,
            status.HTTP_403_FORBIDDEN
        )
        self.assertEqual(
            resp_consulta.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_user_comum_nao_deleta(self):
        self.authenticate(self.user)
        resp_profissional = self.client.delete(self.url_profissional)
        resp_consulta = self.client.delete(self.url_consulta)
        self.assertEqual(
            resp_profissional.status_code,
            status.HTTP_403_FORBIDDEN
        )
        self.assertEqual(
            resp_consulta.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_admin_create(self):
        self.authenticate(self.admin)

        data_profissional = {
            "nome": "Maria JOse",
            "profissao": "Esteticista",
            "endereco": "Rua Y",
            "contato": "novo@email.com"
        }

        data_consultas = {"profissional": self.profissional.id}

        resp_profissionais = self.client.post(
            '/api/profissionais/',
            data=data_profissional,
            format='json'
        )
        resp_consultas = self.client.post(
            '/api/consultas/',
            data=data_consultas,
            format='json'
        )

        self.assertEqual(
            resp_profissionais.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            resp_consultas.status_code,
            status.HTTP_201_CREATED
        )

    def test_admin_edit(self):
        self.authenticate(self.admin)

        data_profissionais = {
            "nome": "Maria Editadaaaa",
            "profissao": "Esteticistaaaa",
            "endereco": "Ruaaa Y",
            "contato": "novo@emAAail.coooom"
        }

        data_consulta = {"profissional": self.profissional.id}

        resp_profissional = self.client.put(
            self.url_profissional,
            data=data_profissionais,
            format='json'
        )
        resp_consulta = self.client.put(
            self.url_consulta,
            data=data_consulta,
            format='json'
        )

        self.assertEqual(
            resp_profissional.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            resp_consulta.status_code,
            status.HTTP_200_OK
        )

    def test_admin_deleta(self):
        self.authenticate(self.admin)

        resp_consulta = self.client.delete(self.url_consulta)
        self.assertEqual(resp_consulta.status_code, status.HTTP_204_NO_CONTENT)

        resp_profissional = self.client.delete(self.url_profissional)
        self.assertEqual(
            resp_profissional.status_code,
            status.HTTP_204_NO_CONTENT
        )
