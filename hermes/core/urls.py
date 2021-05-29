from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^usuarios/$', views.UsuariosList.as_view(), name='Dados_usuario'),
]