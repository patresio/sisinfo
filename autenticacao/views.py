from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


from .forms import CreationFormUser


def cadastroUsuario(request):
    form = CreationFormUser()
    if request.method == 'POST':
        form = CreationFormUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cadastro'))
    context = {
        'form': form,
    }
    return render(request, 'cadastro.html', context)


def usuarios(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'usuarios.html', context)
