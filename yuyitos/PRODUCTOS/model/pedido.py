from PRODUCTOS.model.proveedor import Proveedor
from django.db import models

#rest-framework
from rest_framework import serializers

#foreign keys
from PRODUCTOS.model.pedido_estado import EstadoPedido
from PRODUCTOS.model.producto import Producto


class Pedido(models.Model):

    num_orden = models.CharField(max_length=20,
                                blank=True,
                                null=True,
                                verbose_name="Numero Orden")

    productos = models.ManyToManyField(Producto)

    cant_productos = models.IntegerField(blank=True,
                                        null=True,
                                        verbose_name="Cantidad Productos")

    total_pedido = models.IntegerField(
                                        null=True,
                                        blank=True,
                                        verbose_name="Total Pedido")
    
    fecha_emision = models.DateField(auto_now_add=True)

    fecha_modificacion = models.DateField(blank=True,
                                        null=True)
    
    fecha_envio = models.DateField(blank=True,
                                    null=True)

    fecha_recepcion = models.DateField(blank=True,
                                    null=True)

    estado = models.ForeignKey(EstadoPedido,
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor,
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)
   

    class Meta:
        verbose_name="Pedido"
        verbose_name_plural = "Pedidos"
        db_table = "ped_pedido"

    def __str__(self):
        text = 'N° '+str(self.num_orden) + ' / ' + str(self.fecha_emision) + ' / '+str(self.proveedor)
        return str(text)


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = (
            'num_orden', 
            'productos',
            'cant_productos',
            'total_pedido',
            'fecha_emision', 
            'fecha_modificacion',
            'fecha_envio',
            'fecha_recepcion', 
            'estado',
            'proveedor',
        )