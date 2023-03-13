from django.shortcuts import render

# Create your views here.
from .models import ProcessoLicitatorio, Material
from .forms import ProcessoLicitatorioForm, MaterialForm

# Materiais


def suprimentos(request):
    context = {}
    return render(request, 'suprimentos.html', context)

# Processos


def processos(request):
    form = ProcessoLicitatorioForm()
    processos = ProcessoLicitatorio.objects.all()
    context = {
        'form': form,
        'processos': processos,
    }
    return render(request, 'processos.html', context)
