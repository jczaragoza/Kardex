from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator

from core.erp.models import Estado, Persona
from core.erp.forms import PersonaForm


def category_list(request):
    data = {
        'title': 'Listado de Alumnos',
        'personas': Persona.objects.all()
    }
    return render (request, 'category/list.html', data)


class PersonaListView(ListView):
    model = Persona
    template_name = 'category/list.html'

    #def get_queryset(self):
    #    return Persona.objects.filter(curp__startswith='C')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name':'Juan'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ' Listado de Alumnos'
        context['create_url'] = reverse_lazy('kardex:category_create')
        context['list_url'] = reverse_lazy('kardex:category_list')
        context['entity'] = 'Alumnos'
        return context


class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('kardex:category_list')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear de Alumno'
        context['entity'] = 'Alumnos'
        context['list_url'] = reverse_lazy('kardex:category_list')

        return context
