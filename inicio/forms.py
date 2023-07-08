from django import forms
from ckeditor.fields import RichTextFormField

class IniciarVentaFormulario(forms.Form):
    articulo = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    fecha_de_oferta = forms.DateField(required=False)
    descripcion = RichTextFormField()
    vendedor= forms.CharField(max_length=50)
    
    
    
class BuscarArticulo(forms.Form):
    articulo = forms.CharField(max_length=30, required=False)
    

    