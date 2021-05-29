from django.db.models import fields
from rest_framework import serializers
from .models import Music, Usuarios

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:

        model = Usuarios
        fields =  '__all__'