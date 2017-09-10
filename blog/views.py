from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html', {})

def contato(request):
    return render(request, 'blog/contato.html', {})

def login(request):
    return render(request, 'blog/login.html', {})

def membros(request):
    return render(request, 'blog/membros.html', {})

def projetos(request):
    return render(request, 'blog/projetos.html', {})

def projeto(request):
    return render(request, 'blog/projeto.html', {})

def publicacoes(request):
    return render(request, 'blog/publicacoes.html', {})

def linha01(request):
    return render(request, 'blog/linhadepesquisa1.html', {})

def linha02(request):
    return render(request, 'blog/linhadepesquisa2.html', {})

def linha03(request):
    return render(request, 'blog/linhadepesquisa3.html', {})
