from django import forms
from ckeditor.fields import RichTextFormField
from django.core.validators import FileExtensionValidator

# class IniciarVentaFormulario(forms.Form):
#     articulo = forms.CharField(max_length=30)
#     precio = forms.IntegerField()
#     fecha_de_oferta = forms.DateField(required=False)
#     descripcion = RichTextFormField()
#     vendedor= forms.CharField(max_length=50)
#     imagen = forms.ImageField(required=False)

from django import forms
from .models import Vender

class IniciarVentaFormulario(forms.ModelForm):
    class Meta:
        model = Vender
        fields = ['articulo', 'precio', 'fecha_de_oferta', 'descripcion', 'vendedor', 'imagen']
    
    
    
class BuscarArticulo(forms.Form):
    articulo = forms.CharField(max_length=30, required=False)
    

    