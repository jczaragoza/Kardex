from django.conf.urls import url
from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.alumno.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.test.views import TestView

app_name = 'kardex'

urlpatterns = [
    # Cursos
    path('cursos/list/', CursoListView.as_view(), name='category_list'),
    path('cursos/add/', CursoCreateView.as_view(), name='category_create'),
    path('cursos/update/<int:pk>/', CursoUpdateView.as_view(), name='category_update'),
    path('cursos/delete/<int:pk>/', CursoDeleteView.as_view(), name='category_delete'),
    path('cursos/form/', CursoFormView.as_view(), name='category_form'),
    # Alumnos
    path('alumnos/list/', PersonaListView.as_view(), name='alumno_list'),
    path('alumnos/add/', PersonaCreateView.as_view(), name='alumno_create'),
    path('alumnos/update/<int:pk>/', PersonaUpdateView.as_view(), name='alumno_update'),
    path('alumnos/delete/<int:pk>/', PersonaDeleteView.as_view(), name='alumno_delete'),
    path('alumnos/form/', PersonaFormView.as_view(), name='alumno_form'),
    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #Test
    path('test/', TestView.as_view(), name='test'),
]

