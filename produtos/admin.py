from django.contrib import admin

from produtos.models import Produto

# Register your models here.
class ProdutosAdmin(admin.ModelAdmin):
    list_display= ('produto_nome', 'slug', 'estoque', 'esta_disponivel', 'categoria')
    prepopulated_fields = {
        'slug' : ('produto_nome',)
    }

admin.site.register(Produto, ProdutosAdmin)
