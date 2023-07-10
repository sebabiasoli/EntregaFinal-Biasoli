from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Vender(models.Model):
    articulo = models.CharField(max_length=30)
    precio = models.IntegerField()
    fecha_de_oferta = models.DateField(null=True)
    descripcion = RichTextField(null=True)
    vendedor = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes_articulos', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)