from django.shortcuts import render
from .models import Mesero
from django.urls import reverse

def lista_meseros(request):
    meseros = Mesero.objects.all()
    return render(request, 'meseros/lista_meseros.html', {'meseros': meseros})

def meseros_jovenes_peruanos(request):
    jovenes_meseros = Mesero.objects.filter(nacionalidad='Perú', edad__lt=30)
    return render(request, 'meseros/meseros_jovenes_peruanos.html', {'meseros': jovenes_meseros})

def actualizar_edades(request):
    # Actualiza la edad de todos los meseros, sumándoles 5 años
    meseros = Mesero.objects.all()
    for mesero in meseros:
        mesero.edad += 5
        mesero.save()

    # Redirecciona a la lista de meseros después de la actualización
    return render(request, 'meseros/edades_actualizadas.html')