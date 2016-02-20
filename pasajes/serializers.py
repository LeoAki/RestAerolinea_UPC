#serializers.py
from models import TbCliente
from models import TbVuelo
from models import TbPasaje

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