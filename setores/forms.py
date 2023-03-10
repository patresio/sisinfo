from django import forms

from .models import Setor


class SetorForm(forms.ModelForm):

    class Meta:
        model = Setor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'