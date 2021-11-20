from django.db import models
from django.db.models.base import Model


#foreing keys
from PRODUCTOS.model.comuna import Comuna


from rest_framework import serializers




class Proveedor(models.Model):
    
    razon_social = models.CharField(max_length=255,
                                    null=True,
                                    blank=True)

    rut = models.CharField(max_length=8,
                                    null=True,
                                    blank=True)

    dv = models.CharField(max_length=1,
                                    null=True,
                                    blank=True)

    direccion = models.CharField(max_length=255,
                                    null=True,
                                    blank=True)

    giro = models.CharField(max_length=255,
                            blank=True,
                            null=True)

    rubro = models.CharField(max_length=255,
                            blank=True,
                            null=True)

    telefono = models.CharField(max_length=15,
                                blank=True,
                                null=True)

    correo = models.CharField(max_length=255,
                                null=True,
                                blank=True)
    nom_representante = models.CharField(max_length=255,
                                null=True,
                                blank=True)
    comuna = models.ForeignKey(Comuna,
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "ped_proveedor"

    def __str__(self):
        return str(self.razon_social)

    def getByRut(self, rut_prov):
        
        try:
            prov = Proveedor.objects.filter(rut=rut_prov)

        except Exception as ex:
            print('ERROR AL CONSULTAR PROVEEDOR POR RUT: ', str(ex))

        byRUT = Proveedor.objects.get(rut = prov.rut)
        return byRUT

class ProveedorSerializer(serializers.ModelSerializer):
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

