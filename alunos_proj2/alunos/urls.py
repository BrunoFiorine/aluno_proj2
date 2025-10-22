from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.criar_aluno, name='criar_aluno'),
    path('<int:id>/', views.detalhe_aluno, name='detalhe_aluno'),
    path('<int:id>/editar/', views.editar_aluno, name='editar_aluno'),
    path('<int:id>/excluir/', views.excluir_aluno, name='excluir_aluno'),
]
