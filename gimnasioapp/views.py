from django.shortcuts import render
from rest_framework import viewsets

def home(request):
    return render(request, 'home.html')
def vista_maquinas(request):
    return render(request, 'maquinas_list.html')

from .models import (
    Gimnasio, 
    Usuario, 
    Ejercicio, 
    Rutina, 
    DetalleRutina, 
    SesionEntrenamiento
)
from .serializers import (
    GimnasioSerializer, 
    UsuarioSerializer, 
    EjercicioSerializer, 
    RutinaSerializer, 
    DetalleRutinaSerializer, 
    SesionEntrenamientoSerializer
)

class GimnasioViewSet(viewsets.ModelViewSet):
    queryset = Gimnasio.objects.all()
    serializer_class = GimnasioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer

class DetalleRutinaViewSet(viewsets.ModelViewSet):
    queryset = DetalleRutina.objects.all()
    serializer_class = DetalleRutinaSerializer

class SesionEntrenamientoViewSet(viewsets.ModelViewSet):
    queryset = SesionEntrenamiento.objects.all()
    serializer_class = SesionEntrenamientoSerializer
