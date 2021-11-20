from django.db import models

from rest_framework import serializers


class Comuna(models.Model):
    cod_comuna = models.CharField(max_length=30,
                                blank=True,
                                null=True)
    nom_comuna = models.CharField(max_length=255,
                                blank=True,
                                null=True)
    estado = models.BooleanField(default=True,
                                blank=True,
                                null=True)

    class Meta:
        verbose_name="Comuna"
        verbose_name_plural = "Comunas"
        db_table = "ped_comuna"
    
    def __str__(self):
        return str(self.nom_comuna)


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields =(
            'cod_comuna',
            'nom_comuna',
            'estado',
        )


