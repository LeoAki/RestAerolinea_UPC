#serializers.py
from models import TbCliente
from models import TbVuelo
from models import TbPasaje
from models import TbDestino
from models import TbItinerario

from rest_framework.serializers import ModelSerializer


class TbCLienteSerializer(ModelSerializer):
	class Meta:
		model = TbCliente

class TbVueloSerializer(ModelSerializer):
	class Meta:
			model = TbVuelo

class TbPasajeSerializer(ModelSerializer):
	class Meta:
			model = TbPasaje

class TbDestinoSerializer(ModelSerializer):
	class Meta:
			model = TbDestino

class TbItinerarioSerializer(ModelSerializer):
	class Meta:
			model = TbItinerario