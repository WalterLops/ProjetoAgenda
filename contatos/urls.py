from django.urls import path
from . import views # o ponto sisginifica que está pegando a pasta nomeApp

urlpatterns = [
    path('', views.index, name='contatos'),
    path('<int:id_contato>', views.info_contato, name='info_contato')
]