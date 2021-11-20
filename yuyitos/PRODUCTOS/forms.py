from django import forms
from django.forms import ModelForm

#model
from PRODUCTOS.model.producto import Producto
from PRODUCTOS.model.proveedor import Proveedor
from PRODUCTOS.model.pedido import Pedido


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = (
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
  
        widgets={
            #'id':forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'sku':forms.TextInput(attrs={'class':'form-control', 'placeholder':'SKU...'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción..'}),
            'precio_compra':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Precio de compra'}),
            'precio_venta':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Precio de venta...'}),
            'stock':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Stock...'}),
            'stock_critico':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Stock Critico...'}),
            'categoria':forms.Select(attrs={'class':'form-control', }),
            'tipo_producto':forms.Select(attrs={'class':'form-control', }),
            'proveedor':forms.Select(attrs={'class':'form-control', })

        }




class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = (
            'razon_social', 
            'rut',
            'dv',
            'direccion',
            'giro',
            'rubro',
            'telefono',
            'correo',
            'nom_representante',
            'comuna',
        )
        widgets={
            #'id':forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'razon_social':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Empresa...'}),
            'rut':forms.TextInput(attrs={'class':'form-control', 'placeholder':'RUT..'}),
            'dv':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digito Verificador'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion...'}),
            'giro':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Giro...'}),
            'rubro':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rubro...'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono...' }),
            'correo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo...' }),
            'nom_representante':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Representante...' }),
            'comuna':forms.Select(attrs={'class':'form-control', }),

        }




class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = (
            'num_orden', 
            'proveedor',

            'productos',
            'cant_productos',
            'total_pedido',
            #'fecha_emision', 
            'fecha_modificacion',
            'fecha_envio',
            'fecha_recepcion', 
            'estado',
        )
        widgets={
            #'id':forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'num_orden':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero Orden...'}),
            'proveedor':forms.Select(attrs={'class':'form-control', }),

            'productos':forms.SelectMultiple(attrs={'class':'form-control', }),
            'cant_productos':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cant de productos'}),
            'total_pedido':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total Pedido...'}),
            #'fecha_emision':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_modificacion':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_envio':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_recepcion':forms.DateInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),

        }
