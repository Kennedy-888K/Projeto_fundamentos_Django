from django.shortcuts import render

# Create your views here.

def tarefas_home(request):
    contexto = {
        'nome': 'Bruno'
    }
    return render(request, 'pagetarefas/home.html', contexto)

def tarefas_adicionar(request):
    return render(request, 'pagetarefas/adicionar.html')