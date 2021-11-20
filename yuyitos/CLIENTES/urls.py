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

from CLIENTES.view.cliente import IndexPageView as list_clientes
from CLIENTES.view.cliente import AddCliente as add_cliente
from CLIENTES.view.cliente import updateCliente 
from CLIENTES.view.cliente import deleteCliente 



cliente_url = [
    path('', list_clientes.as_view(), name="listClientes"),
    path('add', add_cliente.as_view(), name="crear-cliente"),
    path('update/<int:pk>', updateCliente, name="actualizarCliente"),
    path('delete/<int:pk>', deleteCliente, name="eliminarCliente"),

    #path(''),

    #
]
