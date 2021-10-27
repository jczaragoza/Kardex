from django.forms import *
from core.erp.models import Curso, Persona, Estado, Municipio


class CursoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curso'].widget.attrs['autofocus'] = True

    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'curso': TextInput(
                attrs={
                    'placeholder': 'Ingrese el curso'
                }
            ),
            'categoria': TextInput(
                attrs={
                    'placeholder': 'Ingrese la categoria'
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese la descripción'
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


class TestForm(Form):
    estados = ModelChoiceField(queryset=Estado.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
    municipios = ModelChoiceField(queryset=Municipio.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))