from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista.html', {'alunos': alunos})

def criar_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        Aluno.objects.create(nome=nome, matricula=matricula)
        return redirect('lista_alunos')
    return render(request, 'aluno_form.html')

def detalhe_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'aluno_detalhe.html', {'aluno': aluno})

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.matricula = request.POST.get('matricula')
        aluno.save()
        return redirect('lista_alunos')
    return render(request, 'aluno_form.html', {'aluno': aluno})

def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'aluno_confirm_delete.html', {'aluno': aluno})
