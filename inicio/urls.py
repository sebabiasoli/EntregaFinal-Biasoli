from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('articulos_en_venta/', views.articulos_en_venta, name='articulos_en_venta'),
    path('iniciar_venta/', views.iniciar_venta, name='iniciar_venta'),
    path('articulos_en_venta/<int:pk>/detalle/', views.DetalleGato.as_view(), name='detalle_articulos'),
    path('articulos_en_venta/<int:pk>/modificar/', views.ModificarGato.as_view(), name='modificar_articulos'),
    path('articulos_en_venta/<int:pk>/eliminar/', views.EliminarGato.as_view(), name='eliminar_articulos')
]
