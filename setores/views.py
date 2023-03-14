from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
from .models import Setor
from .forms import SetorForm


def setores(request):
    setores = Setor.objects.all()
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Inserido com sucesso!')
        else:
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro!')
        return redirect(reverse('setores'))
    form = SetorForm()
    context = {
        'form': form,
        'setores': setores,
    }
    return render(request, 'setores.html', context)


def update_setor(request, id):
    setor = get_object_or_404(Setor, id=id)
    form = SetorForm(instance=setor)
    setores = Setor.objects.all()

    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)

        if form.is_valid():
            return extrair_forms_atualizar(form, request)
        else:
            return render(request, 'setores.html', {'form': form, 'setor':setor, 'setores':setores})
    elif request.method == 'GET':
        return render(request, 'setores.html', {'form': form, 'setor':setor, 'setores':setores})
    
    return redirect('setores')


def extrair_forms_atualizar(form, request):
    setor = form.save(commit=False)
    setor.nome = form.cleaned_data['nome']
    setor.responsavel = form.cleaned_data['responsavel']
    setor.diretoria = form.cleaned_data['diretoria']
    setor.telefone = form.cleaned_data['telefone']
    setor.endereco = form.cleaned_data['endereco']

    setor.save()

    messages.add_message(request, constants.SUCCESS, 'Atualizado com Sucesso!')
    return redirect(reverse('setores'))


def delete_setor(request, id):
    setor = Setor.objects.get(id=id)
    setor.delete()
    messages.add_message(request, constants.ERROR, 'Excluido com sucesso!')
    return redirect(reverse('setores'))
