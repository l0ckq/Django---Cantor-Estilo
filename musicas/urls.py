from django.urls import path
from .views import listar_musicas, editar_musica, excluir_musica, cadastrar_musica

urlpatterns = [
    path('', listar_musicas, name = 'listar_musicas'),
    path('musicas/cadastrar/', cadastrar_musica, name = 'cadastrar_musica'),
    path('musicas/editar/<int:id>/', editar_musica, name = 'editar_musica'), # "<int:id>" se passa o tipo de dado e a variável
    path('musicas/excluir/<int:id>/', excluir_musica, name = 'excluir_musica'),
]
