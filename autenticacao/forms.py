from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


from .models import Usuario


STATUS_CHOICE = (('True', 'Admininstrador'), ('False', 'Tecnico'))


class CreationFormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'password1', 'password2', 'is_staff']
        widgets = {
            'is_staff': forms.Select(
                choices=STATUS_CHOICE
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UsuarioForm(forms.Form):
    class Meta:
        model = Usuario
        fields = ['profile_pic',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
