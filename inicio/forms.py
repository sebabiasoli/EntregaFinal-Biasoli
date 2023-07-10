from django import forms
from ckeditor.fields import RichTextFormField
from django.core.validators import FileExtensionValidator
from django import forms
from .models import Vender

class IniciarVentaFormulario(forms.ModelForm):
    class Meta:
        model = Vender
        fields = ['articulo', 'precio', 'fecha_de_oferta', 'descripcion', 'vendedor', 'imagen']
    
    
    
class BuscarArticulo(forms.Form):
    articulo = forms.CharField(max_length=30, required=False)
    

    