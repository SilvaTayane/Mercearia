from django.shortcuts import redirect, render

from carrinho.models import Carrinho, ItemCarrinho
from produtos.models import Produto

# Create your views here.

# Verifica se o carrinho já existe na sessão
def getCarId(request):
    carSession = request.session.session_key
    if not carSession:
        carSession = request.session.create()
    return carSession

    
def visualizarCarrinho(request):
    return render(request, 'loja/carrinho.html')


# Adiciona o produto ao carrinho
def adicionarCarrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    try:
        carrinho = Carrinho.objects.get(
            car_id=getCarId(request)
            )
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(
            car_id=getCarId(request)
            )
    carrinho.save()

    try:
        car_item = ItemCarrinho.objetcs.get(produto=produto, carrinho=carrinho)
        car_item.quantidade += 1 
        car_item.save()
    except ItemCarrinho.DoesNotExist:
        car_item = ItemCarrinho.objects.create(
            produto = produto,
            quant = 1,
            carrinho = carrinho,
        )
        car_item.save()
    return redirect('carrinho')
