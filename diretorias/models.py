from django.db import models

# Create your models here.

class TipoDiretoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nome


class Diretoria(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.ForeignKey(TipoDiretoria, on_delete=models.CASCADE)
    responsavel = models.CharField(max_length=200)

    class Meta:
        ordering = ['nome', 'tipo',]
        verbose_name = 'Diretoria'
        verbose_name_plural = 'Diretorias'

    def __str__(self):
        return self.nome