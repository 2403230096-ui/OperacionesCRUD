from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.lista_juegos, name='lista_juegos'),
    path('guardar/', views.guardar_juego, name='guardar_juego'),
    path('eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('actualizar/<int:id>/', views.actualizar_juego, name='actualizar_juego'), # <-- Nueva ruta
]