# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TbCliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    ind_tipo_documento = models.CharField(max_length=1)
    des_num_documento = models.CharField(max_length=20)
    des_nombre = models.CharField(max_length=20)
    des_primer_apellido = models.CharField(max_length=20)
    des_ruc = models.CharField(max_length=11, blank=True, null=True)  # Field name made lowercase.
    des_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tb_cliente'


class TbCompania(models.Model):
    id_compa_ia = models.IntegerField(db_column='id_compa\xf1ia', primary_key=True)  # Field renamed to remove unsuitable characters.
    des_nom_aerolinea = models.CharField(max_length=50)
    des_razon_social = models.CharField(max_length=50)
    num_ruc = models.CharField(max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_compania'


class TbDestino(models.Model):
    id_destino = models.IntegerField(primary_key=True)
    des_nomd_aeropuerto = models.CharField(max_length=50)  # Field name made lowercase.
    des_ciudad = models.CharField(max_length=50)
    cod_ciudad = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'tb_destino'


class TbOrigen(models.Model):
    id_origen = models.IntegerField(primary_key=True)
    des_nomo_aeropuerto = models.CharField(max_length=50)  # Field name made lowercase.
    des_ciudad = models.CharField(max_length=50)
    cod_ciudad = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'tb_origen'


class TbItinerario(models.Model):
    id_itinerario = models.IntegerField(primary_key=True)
    id_origen = models.ForeignKey(TbOrigen, models.DO_NOTHING, db_column='id_origen')
    id_destino = models.ForeignKey(TbDestino, models.DO_NOTHING, db_column='id_destino')
    fec_vuelo = models.DateField()
    num_hora = models.TimeField()
    num_duracion = models.TimeField()

    class Meta:
        managed = False
        db_table = 'tb_itinerario'



class TbPais(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    des_pais = models.CharField(max_length=50)
    cod_pais = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'tb_pais'


class TbVuelo(models.Model):
    id_vuelo = models.IntegerField(primary_key=True)
    id_compa_ia = models.ForeignKey(TbCompania, models.DO_NOTHING, db_column='id_compa\xf1ia')  # Field renamed to remove unsuitable characters.
    id_itinerario = models.ForeignKey(TbItinerario, models.DO_NOTHING, db_column='id_itinerario')
    ind_capacidad = models.IntegerField()
    des_modelo_avion = models.CharField(max_length=50)
    num_vuelo = models.CharField(max_length=6)
    num_precio = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_vuelo'


class TbPasaje(models.Model):
    id_pasaje = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(TbCliente, models.DO_NOTHING, db_column='id_cliente')
    id_vuelo = models.ForeignKey(TbVuelo, models.DO_NOTHING, db_column='id_vuelo')
    ind_clase = models.CharField(max_length=1)
    num_asiento_alfa = models.CharField(max_length=1)
    num_asiento = models.IntegerField()
    des_telef_trabajo = models.CharField(max_length=15, blank=True, null=True)
    des_telef_fijo = models.CharField(max_length=15, blank=True, null=True)
    des_telef_celular = models.CharField(max_length=15, blank=True, null=True)
    id_pais = models.ForeignKey(TbPais, models.DO_NOTHING, db_column='id_pais')

    class Meta:
        managed = False
        db_table = 'tb_pasaje'

