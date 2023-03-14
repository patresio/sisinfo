from django import forms
from django.forms import CheckboxSelectMultiple

from .models import ProcessoLicitatorio, Material, CPUCompleto


class ProcessoLicitatorioForm(forms.ModelForm):
    class Meta:
        model = ProcessoLicitatorio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MaterialForm(forms.ModelForm):
    required_css_class = 'required'

    proc_licitatorio = forms.ModelChoiceField(
        label='Processo',
        queryset=None,
    )

    class Meta:
        model = Material
        fields = '__all__'
        exclude = ('status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Filtra os processos ativos
        processos_ativos = ProcessoLicitatorio.objects.filter(status='1')

        self.fields['proc_licitatorio'].queryset = processos_ativos

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CPUCompletoForm(forms.ModelForm):
    class Meta:
        model = CPUCompleto
        fields = '__all__'
        exclude = ('status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'