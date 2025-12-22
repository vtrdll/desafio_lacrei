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

    def  get(self,  request):
        logger.info('Endpoint')
        return Response ({"status": "ok"})



class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def  get(self,  request):
        logger.info('Endpoint')
        return Response ({"status": "ok"})
