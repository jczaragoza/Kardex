from django.forms import *
from core.erp.models import Persona


class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curp'].widget.attrs['autofocus'] = True

    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'curp': TextInput(
                attrs={
                    'placeholder': 'Ingrese tu CURP'
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese tu nombre'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data