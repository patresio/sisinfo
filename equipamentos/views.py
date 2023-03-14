from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.

from .models import Equipamento
from .forms import EquipamentoForm


def equipamentos(request):
    equipamentos = Equipamento.objects.all()
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Equipamento inserido com sucesso!')
        else:
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro!')
        return redirect(reverse('equipamentos'))
    form = EquipamentoForm()
    context = {
        'form': form,
        'equipamentos': equipamentos
    }
    return render(request, 'equipamentos.html', context)
