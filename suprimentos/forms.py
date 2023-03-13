from django import forms
from .models import ProcessoLicitatorio, Material


class ProcessoLicitatorioForm(forms.ModelForm):
    class Meta:
        model = ProcessoLicitatorio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
