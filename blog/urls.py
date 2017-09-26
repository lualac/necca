from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.indexListView.as_view(), name = 'index'),
    url(r'^projetos/(?P<pk>[0-9]+)/$', views.ProjetoDetailsView.as_view(), name='projeto'),
    url(r'^projetos', views.ProjetosListView.as_view(), name='projetos'),
    url(r'^publicacoes', views.PublicacoesListView.as_view(), name = 'publicacoes'),
    url(r'^membros', views.MembroListView.as_view(), name = 'Membro'),
    url(r'^areas/(?P<pk>[0-9]+)/$', views.LinhaDetailsView.as_view(), name='LinhaDePesquisa'),
    url(r'^contato', views.contatoDetailsView.as_view(), name='Contato'),

]
