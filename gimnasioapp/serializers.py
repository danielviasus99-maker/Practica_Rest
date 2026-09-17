from rest_framework import serializers
from .models import Rutina, Usuario


class RutinaSerializer(serializers.ModelSerializer):

  class Meta:
    model = Rutina
    fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):

  class Meta:
    model = Usuario
    fields = '__all__'