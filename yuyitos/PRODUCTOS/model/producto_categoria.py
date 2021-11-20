from django.db import models


class CategoriaProducto(models.Model):
    cod_categoria = models.CharField(max_length=30)
    nom_categoria = models.CharField(max_length=255)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural = "Categorias"
        db_table = "ped_producto_categoria"
    
    def __str__(self):
        return str(self.nom_categoria)

from rest_framework.serializers import ModelSerializer

class CategoriaProductoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fiels=(
            'cod_categoria',
            'nom_categoria',
        )



