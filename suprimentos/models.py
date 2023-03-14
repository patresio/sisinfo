from django.db import models

# Create your models here

STATUS_CHOICE = (('1', 'Ativo'), ('2', 'Inativo'))


class ProcessoLicitatorio(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)

    class Meta:
        ordering = ('status',)
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'

    def __str__(self):
        return self.nome


class Material(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    proc_licitatorio = models.ForeignKey(
        ProcessoLicitatorio, 
        on_delete=models.SET_NULL, 
        verbose_name='processo',
        related_name='materiais',
        blank=True, 
        null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)

    class Meta:
        ordering = ('status', 'proc_licitatorio', 'nome',)
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return self.nome


class CPUCompleto(models.Model):
    titulo = models.CharField(max_length=200)
    proc_licitatorio = models.ForeignKey(ProcessoLicitatorio, on_delete=models.CASCADE, null=True, blank=True)
    pecas = models.ManyToManyField(Material)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)

    def __str__(self):
        return self.titulo
