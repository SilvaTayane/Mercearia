from django.contrib import admin

# Register your models here.
class ProdutosAdmin(admin.ModelAdmin):
    list_display= ('produtos_nome', 'slug', 'estoque', 'esta_disponivel', '')
