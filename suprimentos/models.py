from django.db import models

# Create your models here

STATUS_CHOICE = (('1', 'Ativo'), ('2', 'Inativo'), ('3', '...'))


class ProcessoLicitatorio(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)

    def __str__(self):
        return self.nome


class Material(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    proc_licitatorio = models.ForeignKey(
        ProcessoLicitatorio, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)

    def __str__(self):
        return self.nome
