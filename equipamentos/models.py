from django.db import models
from secrets import token_urlsafe
from setores.models import Setor

import os
from django.conf import settings

# Create your models here.


class Equipamento(models.Model):
    tipo_choices = (
        ('01', 'COMPUTADOR'),
        ('02', 'NOTEBOOK'),
        ('03', 'ROTEADOR'),
        ('04', 'MIKROTIK')
    )
    status_choices = (
        ('1', 'Ativo'),
        ('2', 'Inativo'),
        ('3', 'Reserva'),
        ('4', 'Baixa Patrimônio')
    )
    indentificador = models.CharField(
        max_length=24, null=True, blank=True)
    codigo_sharepoint = models.CharField(max_length=10, null=True, blank=True)
    setor = models.ForeignKey(
        Setor, on_delete=models.SET_NULL, blank=True, null=True)
    configuracao = models.TextField(blank=True, null=True)
    serial_windows = models.CharField(max_length=25, blank=True, null=True)
    serial_office = models.CharField(max_length=25, blank=True, null=True)
    ip = models.CharField(max_length=12, blank=True, null=True)
    mac_address = models.CharField(max_length=12, blank=True, null=True)
    patrimonio = models.CharField(max_length=10, blank=True, null=True)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=2, choices=tipo_choices, default='01')
    responsavel = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(
        max_length=1, choices=status_choices, default='1')
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['id', 'setor', 'indentificador', 'status', 'patrimonio']

    def save(self, *args, **kwargs):
        if not self.indentificador:
            self.indentificador = token_urlsafe(16)
        super(Equipamento, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.indentificador


class Imagem(models.Model):
    imagem = models.ImageField(upload_to='images/equipamentos')
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, null=True, blank=True)

    def delete(self, *args, **kwargs):
        nome_imagem = str(self.imagem)
        imagem_name = f'{settings.MEDIA_ROOT}/{nome_imagem}'
        if os.path.exists(imagem_name):
            os.remove(imagem_name)
        super(Imagem, self).delete(*args, **kwargs)
