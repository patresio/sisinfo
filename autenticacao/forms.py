from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreationFormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'password1', 'password2',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
