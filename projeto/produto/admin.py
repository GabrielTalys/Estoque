from django.contrib import admin
from models import Produto
 
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ( #campos que querem que apareca no display(nc)
        '__str__',
        'ncm'
        'preco'
        'estoque'
        'estoque_minimo'
    ) 
    search_fields = ('produto',) #campo de busca(nc)
    list_filter = search_fields = ('importado',) #filtro(nc)

