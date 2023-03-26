from django import forms

from .models import Laudo, LaudoMaterial


class LaudoForm(forms.ModelForm):
    class Meta:
        model = Laudo
        fields = '__all__'
        exclude = ['identificacao', 'profissional', 'data_criacao']

    def __init__(self, *args, **kwargs):
        super(LaudoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LaudoMaterialForm(forms.ModelForm):
    class Meta:
        model = LaudoMaterial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
