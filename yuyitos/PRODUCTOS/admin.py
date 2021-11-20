from django.contrib import admin


from PRODUCTOS.model.comuna import Comuna
from PRODUCTOS.model.pedido_estado import EstadoPedido
from PRODUCTOS.model.pedido import Pedido
from PRODUCTOS.model.producto_categoria import CategoriaProducto
from PRODUCTOS.model.producto_tipo import TipoProducto
from PRODUCTOS.model.producto import Producto
from PRODUCTOS.model.proveedor import Proveedor



# Register your models here.

admin.site.register(Comuna)
admin.site.register(EstadoPedido)
admin.site.register(Pedido)
admin.site.register(CategoriaProducto)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Proveedor)
