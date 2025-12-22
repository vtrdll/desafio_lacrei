from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Profissional, Consulta
from .serializers import ProfissionalSerializer, ConsultaSerializer
from rest_framework.response import Response
import logging



logger = logging.getLogger(__name__)

class ProfissionalViewSet(ModelViewSet):

    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

    def list(self, request, *args, **kwargs):
        logger.info('Listagem de Profissionais acessada')
        return super().list(request, *args, **kwargs)



class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def list(self, request, *args, **kwargs):
        logger.info('Listagem de Consultas acessada')
        return super().list(request, *args, **kwargs)