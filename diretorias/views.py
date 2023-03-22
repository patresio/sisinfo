from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Diretoria
from .forms import DiretoriaForm


@login_required(login_url='login')
def diretorias(request):
    diretorias = Diretoria.objects.all()
    if request.method == 'POST':
        form = DiretoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Inserido com sucesso!')
        else:
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro!')
        return redirect(reverse('diretorias'))
    form = DiretoriaForm()
    context = {
        'form': form,
        'diretorias': diretorias,
    }
    return render(request, 'diretorias.html', context)


@login_required(login_url='login')
def update_diretoria(request, id):
    diretoria = get_object_or_404(Diretoria, id=id)
    form = DiretoriaForm(instance=diretoria)
    diretorias = Diretoria.objects.all()

    if request.method == 'POST':
        form = DiretoriaForm(request.POST, instance=diretoria)

        if form.is_valid():
            return extrair_forms_atualizar(form, request)
        else:
            return render(request, 'diretorias.html', {'form': form, 'diretoria': diretoria})
    elif request.method == 'GET':
        return render(request, 'diretorias.html', {'form': form, 'diretoria': diretoria, 'diretorias': diretorias})

    return redirect('diretorias')


def extrair_forms_atualizar(form, request):
    diretoria = form.save(commit=False)
    diretoria.nome = form.cleaned_data['nome']
    diretoria.tipo = form.cleaned_data['tipo']
    diretoria.responsavel = form.cleaned_data['responsavel']

    diretoria.save()

    messages.add_message(request, constants.SUCCESS, 'Atualizado com sucesso!')
    return redirect(reverse('diretorias'))


@login_required(login_url='login')
def delete_diretoria(request, id):
    diretoria = Diretoria.objects.get(id=id)
    diretoria.delete()
    messages.add_message(request, constants.ERROR, 'Excluido com sucesso!')
    return redirect(reverse('diretorias'))
