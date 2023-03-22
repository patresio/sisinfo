from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

# Create a your view here

from .forms import CreationFormUser


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos!')

    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def cadastroUsuario(request):
    form = CreationFormUser()
    if request.method == 'POST':
        form = CreationFormUser(request.POST)
        if form.is_valid():
            print('formulario valido')
            user = form.save()

            messages.add_message(request, constants.SUCCESS,
                                 'Conta criada com sucesso.')
            return redirect(reverse('cadastro_usuario'))
    context = {
        'form': form,
    }
    return render(request, 'cadastro.html', context)


@login_required(login_url='login')
def usuarios(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'usuarios.html', context)


@login_required(login_url='login')
def disableUsuario(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return redirect(reverse('usuarios'))


@login_required(login_url='login')
def enableUsuario(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return redirect(reverse('usuarios'))
