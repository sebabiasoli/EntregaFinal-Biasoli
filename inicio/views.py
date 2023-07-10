from django.shortcuts import render, redirect
from inicio.forms import IniciarVentaFormulario, BuscarArticulo
from inicio.models import Vender

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy    
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from usuario.models import InfoExtra
from django.contrib.auth import get_user
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


 
@login_required
def iniciar_venta(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = IniciarVentaFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            venta = formulario.save(commit=False)
            venta.usuario = request.user  # Asigna el usuario actual como creador
            venta.save()
            return redirect('inicio:articulos_en_venta')
        else:
            return render(request, 'inicio/iniciar_venta.html', {'formulario': formulario})
    formulario = IniciarVentaFormulario()
    return render(request, 'inicio/iniciar_venta.html', {'formulario': formulario, 'mensaje': mensaje})
 
   
class DetalleArticulo(DetailView):
    model = Vender
    template_name = "inicio/detalle_articulos.html"
    

class ModificarArticulo(LoginRequiredMixin,UpdateView):
    model = Vender
    fields = ['articulo', 'precio', 'fecha_de_oferta', 'descripcion', 'vendedor', 'imagen']
    template_name = "inicio/modificar_articulos.html"
    success_url = reverse_lazy('inicio:articulos_en_venta')
    
    def dispatch(self, request, *args, **kwargs):
        # Obtiene el objeto a editar
        self.object = self.get_object()

        # Verifica si el usuario actual es el creador del objeto
        if self.object.usuario == self.request.user or self.request.user.is_staff:
            # Redirige al template de modificación del creador
            self.template_name = 'inicio/modificar_articulos.html'
        else:
            # Redirige al template de autorización para otros usuarios
            self.template_name = 'inicio/autorizacion.html'

        return super().dispatch(request, *args, **kwargs)


class EliminarArticulo(LoginRequiredMixin,DeleteView):
    model = Vender
    template_name = "inicio/eliminar_articulos.html"
    success_url = reverse_lazy('inicio:articulos_en_venta')
    
    def dispatch(self, request, *args, **kwargs):
        # Obtiene el objeto a editar
        self.object = self.get_object()

        # Verifica si el usuario actual es el creador del objeto
        if self.object.usuario == self.request.user or self.request.user.is_staff:
            # Redirige al template de modificación del creador
            self.template_name = 'inicio/eliminar_articulos.html'
        else:
            # Redirige al template de autorización para otros usuarios
            self.template_name = 'inicio/autorizacion.html'

        return super().dispatch(request, *args, **kwargs)
  
   