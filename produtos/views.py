from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from categoria.models import Categoria
from produtos.models import Produto

# Create your views here.

def visualizarloja(request, categoria_slug=None):
    categorias = None
    produtos = None
    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = Produto.objects.all().filter(categoria = categorias, esta_disponivel=True)
    else:
        produtos = Produto.objects.all().filter(esta_disponivel=True)
        contexto = {
            'produtos' : produtos
        }
            

    return render(request, 'loja/loja.html', contexto)

