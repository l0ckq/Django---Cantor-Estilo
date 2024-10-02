from django.db import models
from estilo.models import Estilo

class Musica(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.nome