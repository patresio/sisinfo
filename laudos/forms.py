from django import forms
from django.forms import inlineformset_factory

from .models import Laudo, LaudoMaterial


class LaudoForm(forms.ModelForm):
    class Meta:
        model = Laudo
        fields = '__all__'
        exclude = ['data_criacao', 'profissional',]

    def __init__(self, *args, **kwargs):
        super(LaudoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LaudoMaterialForm(forms.ModelForm):
    id = forms.IntegerField()

    class Meta:
        model = LaudoMaterial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['numero_laudo'].label = ''
        self.fields['numero_laudo'].widget = forms.HiddenInput()

        self.fields['id'].label = ''
        self.fields['id'].widget = forms.HiddenInput()


LaudoMaterialFormset = inlineformset_factory(
    Laudo,
    LaudoMaterial,
    form=LaudoMaterialForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
