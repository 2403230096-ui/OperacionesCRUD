from django.contrib import admin
from django.urls import path, include  # <-- Agrega include aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('juegos.urls')),  # Rutas de la API (si ya existían)
    path('juegos/', include('juegos.urls')), # <-- Agrega esta línea para que reconozca /juegos/
]
