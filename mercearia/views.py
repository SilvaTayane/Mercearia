from django.shortcuts import render


def visualizarHome (request):
    produtos = Produtos.objects.all()
    contexto = [
        'produtos' : produtos
    ]
    return render(request, 'home.html')