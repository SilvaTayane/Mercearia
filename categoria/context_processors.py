from categoria.models import Categoria

# método utilizado para compartilhar objetos de forma GLOBALIZADA no projeto
def menu_categoria(request):
    lista_categoria = Categoria.objects.all()
    return dict(opcoes = lista_categoria)