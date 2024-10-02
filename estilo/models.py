from django.db import models

class Estilo(models.Model):
    nome = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome
