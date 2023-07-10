from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from usuario.form import MiFormularioDeCreacionDeUsuarios, MiFormularioDeEdicionDeDatosDeUsuario

from django.urls import reverse_lazy
from usuario.models import InfoExtra




# Create your views here.



def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/login.html',  {'formulario': formulario})
            
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html',  {'formulario': formulario})




def registrarse(request):
    if request.method == 'POST':
        formulario = MiFormularioDeCreacionDeUsuarios(
            request.POST, request.FILES)
        if formulario.is_valid():
            user = formulario.save()
            info_extra = InfoExtra(
                user=user, avatar=formulario.cleaned_data['avatar'])
            info_extra.save()
            return redirect('usuario:login')
    else:
        formulario = MiFormularioDeCreacionDeUsuarios()
    return render(request, 'usuario/registro.html', {'formulario': formulario})




@login_required
def perfil_usuario(request):
    usuario = request.user
    try:
        info_extra = InfoExtra.objects.get(user=usuario)
        imagen_usuario = info_extra.avatar
    except InfoExtra.DoesNotExist:
        imagen_usuario = None
    return render(request, 'usuario/perfil_usuario.html', {'usuario': usuario, 'imagen_usuario': imagen_usuario})



@login_required
def edicion_perfil(request):
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()
            
            formulario.save()
            return redirect('inicio:inicio')
    else:
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(initial={'avatar': info_extra_user.avatar}, instance=request.user)
        
    return render(request, 'usuario/edicion_perfil.html', {'formulario': formulario})


class ModificarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/modificar_pass.html'
    success_url = reverse_lazy('usuario:editar_perfil')



