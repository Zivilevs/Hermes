from django.db import models
from django.db.models.base import Model
from datetime import datetime

# Create your models here.

class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title

class Usuarios(models.Model):

    class Meta:
        db_table = 'usuario'
    
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)  # vai ter metodo
    cpf = models.IntegerField()
    email = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now=True)
    cep = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    

