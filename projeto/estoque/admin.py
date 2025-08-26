from django.contrib import admin
from models import Estoque, EstoqueItens



@admin.register(Estoque)
class EstoqueAdmin(admin.HotelAdmin):
    list_display = ('__str__', 'nf') #nf= nota fiscal
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'



# Register your models here.
