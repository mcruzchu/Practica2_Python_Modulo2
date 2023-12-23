from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Plato

def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'platos/lista_platos.html', {'platos': platos})

def platos_peruanos(request):
    # Asumiendo que ya has creado los platillos en la base de datos
    platos = Plato.objects.filter(procedencia='Perú', precio__gt=40)
    return render(request, 'platos/platos_peruanos.html', {'platos': platos})

def eliminar_platos_baratos(request):
    # Elimina los platos con precio menor a 15 soles
    Plato.objects.filter(precio__lt=15).delete()

    # Redirecciona a la lista de platos después de la eliminación
    return redirect(reverse('lista_platos'))