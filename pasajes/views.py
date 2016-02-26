from django.shortcuts import render

# Create your views here.
from models import TbCliente
from models import TbVuelo
from models import TbPasaje
from models import TbDestino
from models import TbItinerario

from serializers import TbCLienteSerializer
from serializers import TbVueloSerializer
from serializers import TbPasajeSerializer
from serializers import TbDestinoSerializer
from serializers import TbItinerarioSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics


#class TbCliente2ViewSet(generics.ListAPIView):
#   queryset = TbCliente.objects.all()
#   serializer_class = TbCLienteSerializer

class TbClienteViewSet(ModelViewSet):
    queryset = TbCliente.objects.all()
    serializer_class = TbCLienteSerializer
    def get_queryset(self):
        queryset = TbCliente.objects.all()
        ruc = self.request.GET.get('des_ruc', None)
        if ruc is not None:
            queryset = queryset.filter(des_ruc=ruc)
        return queryset

class TbVueloViewSet(ModelViewSet):
    queryset = TbVuelo.objects.all().order_by('des_modelo_avion')
    serializer_class = TbVueloSerializer
    def get_queryset(self):
        queryset = TbVuelo.objects.all()
        iti = self.request.GET.get('itineario', None)
        if iti is not None:
            queryset = queryset.filter(id_itinerario=iti)
        return queryset

class TbPasajeViewSet(ModelViewSet):
    queryset = TbPasaje.objects.all()
    serializer_class = TbPasajeSerializer

class TbDestinoViewSet(ModelViewSet):
    queryset = TbDestino.objects.all()
    serializer_class = TbDestinoSerializer

class TbItinerarioViewSet(ModelViewSet):
    queryset = TbItinerario.objects.all()
    serializer_class = TbItinerarioSerializer
    def get_queryset(self):
        queryset = TbItinerario.objects.all()
        id_destino = self.request.GET.get('id_destino', None)
        if id_destino is not None:
            queryset = queryset.filter(id_destino = id_destino)
        return queryset