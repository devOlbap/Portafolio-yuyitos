from django.db import models

from rest_framework import serializers

class TipoProducto(models.Model):
    cod_tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)

    class Meta:
        verbose_name="Tipo Producto"
        verbose_name_plural = "Tipos de Producto"
        db_table = 'ped_producto_tipo'

    def __str__(self):
        return str(self.descripcion)

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoProducto
        fields = (
            'cod_tipo',
            'descripcion',
        )