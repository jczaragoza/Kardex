from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.models import Curso
from core.erp.forms import CursoForm


class CursoListView(ListView):
    model = Curso
    template_name = 'category/list.html'

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
                for i in Curso.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de cursos'
        context['create_url'] = reverse_lazy('kardex:category_create')
        context['list_url'] = reverse_lazy('kardex:category_list')
        context['entity'] = 'Cursos'
        return context


class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('kardex:category_list')

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
                data['error'] = 'No ha ingresado a ninguna opci??n'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = reverse_lazy('kardex:category_list')
        context['action'] = 'add'
        return context


class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('kardex:category_list')

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
                data['error'] = 'No ha ingresado a ninguna opci??n'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar datos del curso'
        context['entity'] = 'Cursos'
        context['list_url'] = reverse_lazy('kardex:category_list')
        context['action'] = 'edit'
        return context


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'category/delete.html'
    success_url = reverse_lazy('kardex:category_list')

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
        context['title'] = 'Borrar  Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = reverse_lazy('kardex:category_list')
        return context


class CursoFormView(FormView):
    form_class = CursoForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('kardex:category_list')

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
        context['title'] = 'Form | Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = reverse_lazy('kardex:category_list')
        context['action'] = 'add'
        return context