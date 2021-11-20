from django.db import models


from rest_framework import serializers



class EstadoPedido(models.Model):

    cod_estado = models.CharField(max_length=50,
                                    blank=True,
                                    null=True)
    descripcion = models.CharField(max_length=255,
                                    blank=True,
                                    null=True)

    class Meta:
        verbose_name = "Estado Pedido"
        verbose_name_plural = "Estados de Pedido"
        db_table = "ped_pedido_estado"
    
    def __str__(self):
        return str(self.descripcion)

class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = (
            'cod_estado',
            'descripcion'
        )




