from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.messages import constants

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Laudo, LaudoMaterial
from .forms import LaudoForm, LaudoMaterialForm


@login_required(login_url='login')
def pageLaudos(request):
    laudos = Laudo.objects.all()
    context = {
        'laudos': laudos,
    }
    return render(request, 'laudos.html', context)


@login_required(login_url='login')
def insLaudo(request):
    if request.method == 'GET':
        form = LaudoForm()
        form_material_factory = inlineformset_factory(
            Laudo, LaudoMaterial, form=LaudoMaterialForm, extra=2)
        form_material = form_material_factory()
        context = {
            'form': form,
            'form_material': form_material,
        }
        return render(request, 'ins_laudo.html', context)
    elif request.method == 'POST':
        form = LaudoForm(request.POST)
        form_material_factory = inlineformset_factory(
            Laudo, LaudoMaterial, form=LaudoMaterialForm)
        form_material = form_material_factory(request.POST)
        if form.is_valid() and form_material.is_valid():
            laudo = form.save(commit=False)
            laudo.profissional = request.user
            laudo.save()
            form_material.instance = laudo
            form_material.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Laudo salvo com sucesso!')
            return redirect(reverse('laudos'))
        else:
            context = {
                'form': form,
                'form_material': form_material,
            }
            messages.add_message(request, constants.ERROR,
                                 'Aconteceu um erro!')
            return redirect(reverse('ins_laudo'))
