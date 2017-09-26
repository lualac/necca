# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

from blog import models

from django.shortcuts import render

class MembroListView(generic.ListView):

    model = models.Membro
    template_name = 'blog/membros.html'

class ProjetosListView(generic.ListView):

    model = models.Projetos
    template_name = 'blog/projetos.html'


class ProjetoDetailsView(generic.DetailView):

    model = models.Projetos
    template_name = 'blog/projeto.html'

class PublicacoesListView(generic.ListView):

    model = models.Publicacao
    template_name = 'blog/publicacoes.html'


class contatoDetailsView(generic.DetailView):

    model = models.contato
    template_name = 'blog/contato.html'

    def get_object(self):
        pk = 1
        return get_object_or_404 (models.contato,pk=pk)


class LinhaDetailsView(generic.DetailView):

    model = models.LinhaDePesquisa
    template_name = 'blog/linhadepesquisa1.html'


    def get_context_data(self, **kwargs):
        context = super(LinhaDetailsView, self).get_context_data(**kwargs)
        context['membros'] = models.Membro.objects.filter(projetos__linha_dp=context['object']).distinct()
        return context

class indexListView(generic.ListView):

    model = models.Projetos
    template_name = 'blog/index.html'

    def get_queryset(self):
        return models.Projetos.objects.all()

    def get_context_data(self, **kwargs):
        context = super(indexListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['lp_list'] = models.LinhaDePesquisa.objects.all()
        return context
