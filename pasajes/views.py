from django.shortcuts import render

# Create your views here.
from models import TbCliente
from models import TbVuelo
from models import TbPasaje

from serializers import TbCLienteSerializer
from serializers import TbVueloSerializer
from serializers import TbPasajeSerializer

from rest_framework.viewsets import ModelViewSet


class TbClienteViewSet(ModelViewSet):
	queryset = TbCliente.objects.all()
	serializer_class = TbCLienteSerializer

class TbVueloViewSet(ModelViewSet):
	queryset = TbVuelo.objects.all()
	serializer_class = TbVueloSerializer

class TbPasajeViewSet(ModelViewSet):
	queryset = TbPasaje.objects.all()
	serializer_class = TbPasajeSerializer