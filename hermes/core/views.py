from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .models import Music, Usuarios
from .serializers import MusicSerializer, UsuarioSerializer

# Create your views here.
class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class UsuariosList(generics.ListCreateAPIView):

    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
    