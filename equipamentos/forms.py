from django import forms

from .models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            print(field)
            field.widget.attrs['class'] = 'form-control'