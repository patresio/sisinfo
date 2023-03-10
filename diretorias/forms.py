from django import forms
from .models import Diretoria

class DiretoriaForm(forms.ModelForm):

    class Meta:
        model = Diretoria
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].widget.attrs.update({'placeholder': field})