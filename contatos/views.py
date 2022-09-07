from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q


def index(request):
    #contatos = Contato.objects.all()
    contatos = Contato.objects.order_by('nome')
    paginator = Paginator(contatos, 15)
    
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/index.html', {
        'contatos':contatos
    })
    
    
def info_contato(request, id_contato):
    # obtem o erro correto após inconsistência na página
    contato = get_object_or_404(Contato, id=id_contato) 
    
    if not contato.mostrar:
        print(contato.mostrar)
        raise Http404()
    
    return render(request, 'contatos/info_contato.html', {
        'contato':contato
    })

def busca(request):
    termo = request.GET.get('termo')
    print(termo)
    
    contatos = Contato.objects.order_by('nome').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        mostrar=True
    )
    print(contatos.query)
    paginator = Paginator(contatos, 15)
    
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/busca.html', {
        'contatos':contatos
    })