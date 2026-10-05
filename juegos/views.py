from django.shortcuts import render, redirect, get_object_or_404
from .models import Juego

def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/lista_juegos.html', {'juegos': juegos})

def guardar_juego(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        precio = request.POST.get('precio')
        plataforma = request.POST.get('plataforma', 'PC')
        
        Juego.objects.create(
            titulo=titulo,
            precio=precio,
            plataforma=plataforma,
            anio_lanzamiento=2024
        )
    return redirect('lista_juegos')

def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    return render(request, 'juegos/edicion_juego.html', {'juego': juego})

def actualizar_juego(request, id):
    if request.method == 'POST':
        juego = get_object_or_404(Juego, id=id)
        juego.titulo = request.POST.get('titulo')
        juego.precio = request.POST.get('precio')
        juego.save()
    return redirect('lista_juegos')

def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    return redirect('lista_juegos')