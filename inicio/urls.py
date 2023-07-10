from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('articulos_en_venta/', views.articulos_en_venta, name='articulos_en_venta'),
    path('iniciar_venta/', views.iniciar_venta, name='iniciar_venta'),
    path('articulos_en_venta/<int:pk>/detalle/', views.DetalleArticulo.as_view(), name='detalle_articulos'),
    path('articulos_en_venta/<int:pk>/modificar/', views.ModificarArticulo.as_view(), name='modificar_articulos'),
    path('articulos_en_venta/<int:pk>/eliminar/', views.EliminarArticulo.as_view(), name='eliminar_articulos')
]
