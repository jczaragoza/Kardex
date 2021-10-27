from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.models import Estado, Persona
from core.erp.forms import PersonaForm


class PersonaListView(ListView):
    model = Persona
    template_name = 'alumno/list.html'

    # def get_queryset(self):
    #    return Persona.objects.filter(curp__startswith='C')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Persona.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Listado de Alumnos'
        context['create_url'] = reverse_lazy('kardex:alumno_create')
        context['list_url'] = reverse_lazy('kardex:alumno_list')
        context['entity'] = 'Alumnos'
        return context


class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'alumno/create.html'
    success_url = reverse_lazy('kardex:alumno_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear de Alumno'
        context['entity'] = 'Alumnos'
        context['list_url'] = reverse_lazy('kardex:alumno_list')
        context['action'] = 'add'
        return context


class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'alumno/create.html'
    success_url = reverse_lazy('kardex:alumno_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Datos de Alumno'
        context['entity'] = 'Alumnos'
        context['list_url'] = reverse_lazy('kardex:alumno_list')
        context['action'] = 'edit'
        return context


class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'alumno/delete.html'
    success_url = reverse_lazy('kardex:alumno_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar  Alumno'
        context['entity'] = 'Alumnos'
        context['list_url'] = reverse_lazy('kardex:alumno_list')
        return context


class PersonaFormView(FormView):
    form_class = PersonaForm
    template_name = 'alumno/create.html'
    success_url = reverse_lazy('kardex:alumno_list')

    def form_valid(self, form):
        print(form.is_valid())
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Alumnos'
        context['entity'] = 'Alumnos'
        context['list_url'] = reverse_lazy('kardex:alumno_list')
        context['action'] = 'add'
        return context