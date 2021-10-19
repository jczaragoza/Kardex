from django.conf.urls import url
from django.urls import path
from core.erp.views.category.views import *

app_name = 'kardex'

urlpatterns = [
    path('list/', PersonaListView.as_view(), name='category_list'),
    path('add/', PersonaCreateView.as_view(), name='category_create'),
    path('update/<int:pk>/', PersonaUpdateView.as_view(), name='category_update'),
    path('delete/<int:pk>/', PersonaDeleteView.as_view(), name='category_delete'),
    path('form/', PersonaFormView.as_view(), name='category_form'),
]

