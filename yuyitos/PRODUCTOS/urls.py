"""yuyitos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

#from PRODUCTOS.view.producto import IndexPageView as listProductos
#from PRODUCTOS.view.producto import ProductoView as detailProducto

#from PRODUCTOS.view.proveedor import IndexPageView as listProveedor
#from PRODUCTOS.view.proveedor import ProveedorView as detailProveedor

from PRODUCTOS.view.producto import IndexPageView as litProductos
from PRODUCTOS.view.producto import AddProducto as addProducto
from PRODUCTOS.view.producto import updateProducto as upProducto
from PRODUCTOS.view.producto import deleteProducto as delProducto

#proveedor
from PRODUCTOS.view.proveedor import IndexPageView as listProveedores
from PRODUCTOS.view.proveedor import AddProveedor as addProveedor
from PRODUCTOS.view.proveedor import updateProveedor as upProveedor
from PRODUCTOS.view.proveedor import deleteProveedor as delProveedor


#pedido
from PRODUCTOS.view.pedido import IndexPageView as listPedidos
from PRODUCTOS.view.pedido import AddPedido as addPedido
from PRODUCTOS.view.pedido import updatePedido 
from PRODUCTOS.view.pedido import deletePedido 








producto_url = [
    path('', litProductos.as_view(), name="listProductos"),
    path('add/', addProducto.as_view(), name="addProducto"),
    path('update/<int:pk>', upProducto, name="updateProducto"),
    path('delete/<int:pk>', delProducto, name="deleteProducto"),


    #proveedor
    path('proveedores/', listProveedores.as_view(), name="listProveedor"),
    path('proveedores/add/', addProveedor.as_view(), name="addProveedor"),
    path('proveedores/update/<int:pk>', upProveedor, name="updateProveedor"),
    path('proveedores/delete/<int:pk>', delProveedor, name="deleteProveedor"),

    #pedido
    path('pedidos/', listPedidos.as_view(), name="listPedidos"),
    path('pedidos/add/', addPedido.as_view(), name="addPedido"),
    path('pedidos/update/<int:pk>', updatePedido, name="upPedido"),
    path('pedidos/delete/<int:pk>', deletePedido, name="delPedido"),




    #path('proveedores/<int:pk>/', detailProveedor.as_view(), name="listProveedor"),


]
