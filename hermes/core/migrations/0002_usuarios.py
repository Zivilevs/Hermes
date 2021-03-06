# Generated by Django 3.2.3 on 2021-05-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('cpf', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('data_criacao', models.DateTimeField(auto_now=True)),
                ('cep', models.IntegerField()),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
