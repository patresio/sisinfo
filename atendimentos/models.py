from django.db import models

# Tecnico
from django.contrib.auth.models import User
# Setores
from setores.models import Setor
# Laudos
from laudos.models import Laudo
# Equipamentos
from equipamentos.models import Equipamento

# Create your models here.


class OrdemServico(models.Model):
    STATUS = (('1', 'Aberto'), ('2', 'Finalizado'))
    CHOICES_CONTATO = (
        ('1', 'Contato Telefônico'),
        ('2', 'Contato por WhatsApp'),
        ('3', 'Contato por Email'),
        ('4', 'Contato Pessoalmente')
    )
    protocolo = models.CharField(max_length=10)
    tecnico = models.ForeignKey(
        User, related_name="tecnico", on_delete=models.SET_NULL, null=True, blank=True)
    setor = models.ForeignKey(
        Setor, related_name="setor", on_delete=models.SET_NULL, null=True, blank=True)
    funcionario = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=STATUS, null=True, blank=True)
    tipo_contato = models.CharField(
        max_length=1, choices=CHOICES_CONTATO, null=True, blank=True)
    contato = models.CharField(max_length=11, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.protocolo


class Atendimento(models.Model):
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, null=True, blank=True)
    
