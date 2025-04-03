from django.contrib import admin

from categoria.models import Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria_nome', 'categoria_descricao',)
    prepopulated_fields = {
        'slug' : ('categoria_nome',)
    }

admin.site.register(Categoria, CategoriaAdmin)
