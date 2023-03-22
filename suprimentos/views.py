from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants


from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import ProcessoLicitatorio, Material, CPUCompleto
from .forms import ProcessoLicitatorioForm, MaterialForm, CPUCompletoForm

# Processos


@login_required(login_url='login')
def processos(request):
    processos = ProcessoLicitatorio.objects.all()
    if request.method == 'POST':
        form = ProcessoLicitatorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Inserido com sucesso!')
        else:
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro!')
        return redirect(reverse('processos_licitatorios'))
    form = ProcessoLicitatorioForm()
    context = {
        'form': form,
        'processos': processos,
    }
    return render(request, 'processos.html', context)


@login_required(login_url='login')
def update_processo(request, id):
    processo = get_object_or_404(ProcessoLicitatorio, id=id)
    form = ProcessoLicitatorioForm(instance=processo)
    processos = ProcessoLicitatorio.objects.all()
    if request.method == 'POST':
        form = ProcessoLicitatorioForm(request.POST, instance=processo)
        if form.is_valid():
            return extrair_forms_atualizar_processos(form, request)
        else:
            return render(request, 'processos.html', {'form': form, 'processos': processos, 'processo': processo})
    elif request.method == 'GET':
        return render(request, 'processos.html', {'form': form, 'processos': processos, 'processo': processo})
    return redirect('processos_licitatorios')


def extrair_forms_atualizar_processos(form, request):
    # sourcery skip: remove-redundant-if
    processo = form.save(commit=False)
    processo.nome = form.cleaned_data['nome']
    processo.status = form.cleaned_data['status']
    processo.save()

    # Ajuste para troca de status
    if processo.status == '2' and processo.status != '1':
        materiais = Material.objects.filter(proc_licitatorio=processo.id)
        for material in materiais:
            material.status = '2'
            material.save()
    elif processo.status == '1' and processo.status != '2':
        materiais = Material.objects.filter(proc_licitatorio=processo.id)
        for material in materiais:
            material.status = '1'
            material.save()

    messages.add_message(request, constants.SUCCESS, 'Atualizado com Sucesso!')
    return redirect(reverse('processos_licitatorios'))


@login_required(login_url='login')
def delete_processo(request, id):
    processo = ProcessoLicitatorio.objects.get(id=id)
    processo.delete()
    messages.add_message(request, constants.ERROR, 'Excluido com sucesso!')
    return redirect(reverse('processos_licitatorios'))


# Material de Informatica
@login_required(login_url='login')
def suprimentos(request):
    materiais = Material.objects.all()
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        processo = ProcessoLicitatorio.objects.get(
            id=form.data['proc_licitatorio'])
        if processo.status != '1':
            messages.add_message(request, constants.WARNING,
                                 'Processo Licitatório INATIVO')
        elif form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Inserido com sucesso!')
        else:
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro!')
        return redirect(reverse('suprimentos'))
    form = MaterialForm()

    context = {
        'form': form,
        'materiais': materiais,
    }
    return render(request, 'suprimentos.html', context=context)


@login_required(login_url='login')
def update_suprimento(request, id):
    material = get_object_or_404(Material, id=id)
    form = MaterialForm(instance=material)
    materiais = Material.objects.all()
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            return extrair_forms_atualizar_material(form, request)
        else:
            return render(request, 'suprimentos.html', {'form': form, 'material': material, 'materiais': materiais})
    elif request.method == 'GET':
        return render(request, 'suprimentos.html', {'form': form, 'material': material, 'materiais': materiais})
    return redirect('suprimentos')


def extrair_forms_atualizar_material(form, request):
    material = form.save(commit=False)
    material.nome = form.cleaned_data['nome']
    material.proc_licitatorio = form.cleaned_data['proc_licitatorio']
    material.status = form.cleaned_data['status']
    material.save()

    messages.add_message(request, constants.SUCCESS, 'Atualizado com Sucesso!')
    return redirect(reverse('suprimentos'))


@login_required(login_url='login')
def delete_suprimento(request, id):
    material = Material.objects.get(id=id)
    material.delete()
    messages.add_message(request, constants.ERROR, 'Excluido com sucesso!')
    return redirect(reverse('suprimentos'))


# CPU Completo
@login_required(login_url='login')
def cpucompleto(request):
    form = CPUCompletoForm()
    context = {
        'form': form,
    }
    return render(request, 'cpucompleto.html', context)
