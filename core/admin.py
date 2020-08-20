from django.contrib import admin
from core.models import Produto, Categoria, Tipo

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'tipo', 'preco', 'ativo')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', )

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo', )
