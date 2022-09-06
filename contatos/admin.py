from email.policy import default
from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin): # informações especiais no painel administrativo
        list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar') # lista de atributos que vão aparecer por linha de registrando
        list_display_links = ('id', 'nome', 'sobrenome') # onde vão aparecer links clicáveis para editar um registro
        #list_filter = ('nome', 'sobrenome') # campos para ordenação e filtagem
        list_per_page = 10 # número de resultados por página
        search_fields = ('nome', 'sobrenome', 'telefone') # eses campos servem para fazer busca de registros no campo de pesquisa da parte administrativa
        list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
