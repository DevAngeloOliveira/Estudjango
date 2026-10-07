from django.urls import path

from . import views

app_name = 'aulas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alunos/', views.alunos, name='alunos'),
]
