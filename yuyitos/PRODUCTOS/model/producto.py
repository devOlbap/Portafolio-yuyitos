from django.db import models

#foreign keys
from PRODUCTOS.model.producto_categoria import CategoriaProducto
from PRODUCTOS.model.producto_tipo import TipoProducto
from PRODUCTOS.model.proveedor import Proveedor


from rest_framework import serializers



class Producto(models.Model):

    sku = models.CharField(max_length=17,
                            blank=True,
                            null=True)
    descripcion = models.CharField(max_length=255,
                            blank=True,
                            null=True)
    precio_compra = models.IntegerField(
                                        blank=True,
                                        null=True)
    precio_venta = models.IntegerField(
                                        blank=True,
                                        null=True)
    
    stock = models.IntegerField(
                                blank=True,
                                null=True)
    stock_critico = models.IntegerField(
                                blank=True,
                                null=True)

    categoria= models.ForeignKey(CategoriaProducto,
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)
    
    tipo_producto = models.ForeignKey(TipoProducto,
                                    blank=True,
                                    null=True,
                                    on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor,
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "ped_producto"

    def __str__(self):
        cod = str(self.sku)
        return cod
    
    def getStock(self):

        if self.stock_critico > self.stock:
            data = {
                'mensaje':'Alerta de stock critico',
                'stock disponible': self.stock
            }
            return data
        else:
            return self.stock
    
    def getPrecioCompra(self):
        return str(self.precio_compra)
    
    def getPrecioVenta(self):
        return str(self.precio_venta)

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields=(
            'sku', 
            'descripcion',
            'precio_compra',
            'precio_venta',
            'stock',
            'stock_critico',
            'categoria',
            'tipo_producto',
            'proveedor',
        )