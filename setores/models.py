from django.db import models
from diretorias.models import Diretoria
# Create your models here.

class Setor(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    responsavel = models.CharField(max_length=200, blank=True, null=True)
    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE, blank=True, null=True)
    telefone = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['diretoria', 'nome',]
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self) -> str:
        return self.nome