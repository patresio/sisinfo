from django.db import models

from django.contrib.auth.models import User

from setores.models import Setor
from suprimentos.models import Material, CPUCompleto

# Create your models here.


class Laudo(models.Model):
    CHOICES_STATUS = (
        ('01', 'Aberto'),
        ('02', 'Em andamento'),
        ('03', 'Finalizado')
    )
    identificacao = models.CharField(max_length=24, null=True, blank=True)
    setor = models.OneToOneField(
        Setor, blank=True, null=True, on_delete=models.SET_NULL)
    funcionario = models.CharField(max_length=200, null=True, blank=True)
    justificativa = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2, choices=CHOICES_STATUS, default='01', blank=True, null=True)
    suprimentos = models.ManyToManyField(Material)
    profissional = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
