from django.shortcuts import render, redirect
from inicio.forms import IniciarVentaFormulario, BuscarArticulo
from inicio.models import Vender

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy    

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def about(request):
    return render(request, 'inicio/about.html')


def articulos_en_venta(request):
    
    formulario = BuscarArticulo(request.GET)
    if formulario.is_valid():
        articulo_a_buscar = formulario.cleaned_data['articulo']
        listado_de_articulos = Vender.objects.filter(articulo__icontains=articulo_a_buscar)
   
    formulario = BuscarArticulo()    
    return render(request, 'inicio/articulos_en_venta.html', {'formulario': formulario, 'articulos':listado_de_articulos})


def iniciar_venta(request):
    mensaje = ''
    if request.method == 'POST':
        forumulario = IniciarVentaFormulario(request.POST)
        if forumulario.is_valid():
            info = forumulario.cleaned_data
            venta = Vender(articulo=info['articulo'],precio=info['precio'],fecha_de_oferta=info['fecha_de_oferta'], descripcion=info['descripcion'], vendedor=info['vendedor'])
            venta.save()
            return redirect('inicio:articulos_en_venta')
        else:
            return render(request, 'inicio/iniciar_venta.html', {'formulario': forumulario})
    forumulario = IniciarVentaFormulario()
    return render(request, 'inicio/iniciar_venta.html', {'formulario': forumulario, 'mensaje':mensaje})


   
class DetalleGato(DetailView):
    model = Vender
    template_name = "inicio/detalle_articulos.html"
    
    
class ModificarGato(UpdateView):
    model = Vender
    fields = ['articulo', 'precio', 'fecha_de_oferta', 'descripcion', 'vendedor']
    template_name = "inicio/modificar_articulos.html"
    success_url = reverse_lazy('inicio:articulos_en_venta')


class EliminarGato(DeleteView):
    model = Vender
    template_name = "inicio/eliminar_articulos.html"
    success_url = reverse_lazy('inicio:articulos_en_venta')
  
   