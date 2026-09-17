from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Rutina, Usuario
from .serializers import RutinaSerializer, UsuarioSerializer


def home(request):
    return render ('request','home.html')

class RutinaViewSet(viewsets.ModelViewSet):
  queryset = Rutina.objects.all()
  serializer_class = RutinaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer


