from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_meseros, name='lista_meseros'),
    path('jovenes-peruanos/', views.meseros_jovenes_peruanos, name='meseros_jovenes_peruanos'),
    path('actualizar-edades/', views.actualizar_edades, name='actualizar_edades'),
]


