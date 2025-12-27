from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Profissional, Consulta
from .serializers import ProfissionalSerializer, ConsultaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

import logging


logger = logging.getLogger(__name__)


class ProfissionalViewSet(ModelViewSet):

    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        logger.info("Listagem de Profissionais acessada")
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'list':

            return [IsAuthenticated()]
        return [IsAdminUser()]


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        logger.info("Listagem de Consultas acessada")
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsAdminUser()]
