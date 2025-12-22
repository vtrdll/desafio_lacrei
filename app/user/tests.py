from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse



class UserAuthTests(APITestCase):

    def setUp(self):
        # Criar um usuário para testes
        self.user = User.objects.create_user(
            username="teste", 
            password="pass123456"
        )
        self.token_url = reverse('token_obtain_pair')  # endpoint JWT

    def test_login_jwt_sucesso(self):
        data = {
            "username": "teste",
            "password": "pass123456"
        }
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        
    def test_login_jwt_erro_credenciais(self):
        data = {
            "username": "teste",
            "password": "senha_errada"
        }
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'No active account found with the given credentials')
