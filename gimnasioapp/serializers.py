from rest_framework import serializers
from .models import (
    Gimnasio, 
    Usuario, 
    Ejercicio, 
    Rutina, 
    DetalleRutina, 
    SesionEntrenamiento
)

class GimnasioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gimnasio
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = '__all__'

class DetalleRutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleRutina
        fields = '__all__'

class SesionEntrenamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionEntrenamiento
        fields = '__all__'