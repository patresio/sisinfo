from django import forms
from .models import Diretoria

class DiretoriaForm(forms.ModelForm):

    class Meta:
        model = Diretoria
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'