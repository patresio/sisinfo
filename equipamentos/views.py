from django.shortcuts import render

# Create your views here.

from .models import Equipamento
from .forms import EquipamentoForm


def equipamentos(request):
    equipamentos = Equipamento.objects.all()
    form = EquipamentoForm()
    context = {
        'form': form,
        'equipamentos': equipamentos
    }
    return render(request, 'equipamentos.html', context)