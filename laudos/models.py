from django.db import models

from secrets import token_urlsafe

from django.contrib.auth.models import User

from setores.models import Setor
from suprimentos.models import Material

# Create your models here.


class Laudo(models.Model):
    CHOICES_STATUS = (
        ('01', 'Aberto'),
        ('02', 'Finalizado')
    )
    identificacao = models.CharField(max_length=24, null=True, blank=True)
    setor = models.ForeignKey(
        Setor, blank=True, null=True, on_delete=models.SET_NULL)
    funcionario = models.CharField(max_length=200, null=True, blank=True)
    justificativa = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2, choices=CHOICES_STATUS, default='01', blank=True, null=True)
    profissional = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if not self.identificacao:
            self.identificacao = token_urlsafe(16)
        super(Laudo, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.identificacao


class LaudoMaterial(models.Model):
    numero_laudo = models.ForeignKey(
        Laudo, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='materiais')
    item = models.ForeignKey(
        Material, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True, default=0)


class Empenho(models.Model):
    numero_laudo = models.ForeignKey(Laudo, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='empenhos')
    numero_empenho = models.CharField(max_length=10, blank=True, null=True)
    fornecedor = models.CharField(max_length=255, blank=True, null=True)
    nota_fiscal = models.CharField(max_length=10, blank=True, null=True)