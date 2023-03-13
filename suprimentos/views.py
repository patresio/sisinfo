from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
from .models import ProcessoLicitatorio, Material
from .forms import ProcessoLicitatorioForm, MaterialForm

# Materiais


def suprimentos(request):
    context = {}
    return render(request, 'suprimentos.html', context)

# Processos

def processos(request):
    processos = ProcessoLicitatorio.objects.all()
    if request.method == 'POST':
        form = ProcessoLicitatorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Inserido com sucesso!')
        else:
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro!')
        return redirect(reverse('processos_licitatorios'))
    form = ProcessoLicitatorioForm()
    context = {
        'form': form,
        'processos': processos,
    }
    return render(request, 'processos.html', context)

def update_processos(request, id):
    processo = get_object_or_404(ProcessoLicitatorio, id=id)
    form = ProcessoLicitatorioForm(instance=processos)
    processos = ProcessoLicitatorio.objects.all()

    if request.method == 'POST':
        form = ProcessoLicitatorioForm(request.POST, instance=processo)

        if form.is_valid():
            return extrair_forms_atualizar(form, request)
        else:
            return render(request, 'processos.html', {'form': form, 'processos': processos, 'processo': processo})
    elif request.method == 'GET':
        return render(request, 'processos.html', {'form': form, 'processos': processos, 'processo': processo})
    return redirect('processos_licitatorios')

def extrair_forms_atualizar(form, request):
    processo = form.save(commit=False)
    processo.nome = form.cleaned_data['nome']
    processo.status = form.cleaned_data['status']
    processo.save()

    messages.add_message(request, constants.SUCCESS, 'Atualizado com Sucesso!')
    return redirect(reverse('processos_licitatorios'))

def delete_processo(request, id):
    processo = ProcessoLicitatorio.objects.get(id=id)
    processo.delete()
    messages.add_message(request, constants.ERROR, 'Excluido com sucesso!')
    return redirect(reverse('processos_licitatorios'))


# Material de Informatica

def suprimentos(request):
    
    context = {}
    return render(request, 'suprimentos.html', context=context)