from django.urls import path
from Site import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre-a-empresa', views.institucional, name='institucional'),
    path('contato-shopping', views.contato, name='contato' ),
    path('cadastro-shopping', views.cadastro, name='cadastro'),
    path('produtos', views.produto_lista, name='produto_lista'),
    path('produto', views.produto_detalhe, name='produto_detalhes')
]

