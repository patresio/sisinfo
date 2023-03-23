from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff != True:
            messages.add_message(request, constants.ERROR,
                                 'Você não tem autorização de administrador.')
            return redirect('index')

        if request.user.is_staff == True:
            return view_func(request, *args, **kwargs)

    return wrapper_function
