from django import forms
from django.forms import ModelForm

#model
from CLIENTES.model.cliente import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'rut',
            'rut_dv',
            'nombres',
            'paterno',
            'materno',
            'telefono',
            'autorizado',
            'direccion',
        )
        labels = {
            'id':'',
            'rut':'',
            'rut_dv':'',
            'nombres':'',
            'paterno':'',
            'materno':'',
            'telefono':'',
            'autorizado':'Autorizado',
            'direccion':'',
        }
        widgets={
            #'id':forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'rut':forms.TextInput(attrs={'class':'form-control', 'placeholder':'RUT...'}),
            'rut_dv':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digito verificador'}),
            'nombres':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombres...'}),
            'paterno':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido paterno...'}),
            'materno':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido materno...'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'telefono...'}),
            'autorizado':forms.CheckboxInput(attrs={'class':'checkbox'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Av. El Manzano #756 ...'})
        }




