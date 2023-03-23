from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

# Create a your view here

from .models import Usuario

from .forms import CreationFormUser, UsuarioForm

from .decorators import unauthenticated_user, admin_only


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos!')
        else:
            login(request, user)
            return redirect('index')
    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
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
@admin_only
def usuarios(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'usuarios.html', context)


@login_required(login_url='login')
@admin_only
def disableUsuario(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return redirect(reverse('usuarios'))


@login_required(login_url='login')
@admin_only
def enableUsuario(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return redirect(reverse('usuarios'))


@login_required(login_url='login')
def perfilUsuario(request, id):
    user = request.user
    if request.method == 'GET':
        userform = CreationFormUser(instance=user)
        usuarioform = Usuario()
        context = {
            'userform': userform,
            'usuarioform': usuarioform,
        }
        return render(request, 'profile.html', context)
    elif request.method == 'POST':
        userform = CreationFormUser(request.POST, instance=user)
        if userform.is_valid():
            return extrair_forms_usuarios(userform, id, request)


def extrair_forms_usuarios(form, id, request):
    # Gambiarra para manter administrador
    old_user = User.objects.get(id=id)
    print(old_user.is_staff)
    usuario_f = form.save(commit=False)
    usuario_f.first_name = form.cleaned_data['first_name']
    usuario_f.last_name = form.cleaned_data['last_name']
    usuario_f.username = form.cleaned_data['username']
    usuario_f.email = form.cleaned_data['email']
    usuario_f.password1 = form.cleaned_data['password1']
    usuario_f.password2 = form.cleaned_data['password2']

    usuario_f.save()
    print('salvou o formulario primeiro')

    alt_user = User.objects.get(id=id)
    print('Esse é o antigo ainda:', old_user.is_staff)
    print('Esse é o novo:', alt_user.is_staff)

    if old_user.is_staff is True and alt_user.is_staff is False:
        alt_user.is_staff = True
        print('Esse era adm:', alt_user.is_staff)
    elif old_user.is_staff is False and alt_user.is_staff is False:
        alt_user.is_staff = False
        print('Esse nao era adm:', alt_user.is_staff)

    alt_user.save()
    print('Salvou o ultimo form')

    messages.add_message(request, constants.SUCCESS,
                         'Usuario alterado com sucesso')
    return redirect(reverse('perfil_usuario', kwargs={'id': id}))
