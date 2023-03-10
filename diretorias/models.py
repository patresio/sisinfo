from django.db import models

# Create your models here.

CHOICES_TIPO = (
    ('1', 'Gabinete'), 
    ('2', 'Departamento'), 
    ('3', 'Diretoria'), 
    ('4', 'Secretaria'))


class Diretoria(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=CHOICES_TIPO, default='3')
    responsavel = models.CharField(max_length=200)

    def __str__(self):
        return self.nome