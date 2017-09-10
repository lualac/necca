from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^contato', views.contato),
    url(r'^login', views.login),
    url(r'^membros', views.membros),
    url(r'^projetos', views.projetos),
    url(r'^projeto', views.projeto),
    url(r'^publicacoes', views.publicacoes),
    url(r'^acessibilidade', views.linha01),
    url(r'^sustentabilidadedoedificio', views.linha02),
    url(r'^sustentabilidadeespacosurbanos', views.linha03),
]
