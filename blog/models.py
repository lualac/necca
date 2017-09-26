# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
#from django.utils import timezone

@python_2_unicode_compatible
class Membro (models.Model):
    nome = models.CharField(max_length=255)
    cnpq = models.TextField()
    foto = models.FileField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nome

@python_2_unicode_compatible
class LinhaDePesquisa (models.Model):
      nome = models.CharField(max_length=255)
      descricao = models.CharField(max_length=255)
      icone = models.FileField(blank=True, null=True)

      def __str__(self):
          return self.nome

@python_2_unicode_compatible
class Projetos (models.Model):
    linha_dp = models.ForeignKey('LinhaDePesquisa', related_name='projetos')
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    membros = models.ManyToManyField(Membro, related_name='projetos')
    data = models.DateField()

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Projetos'
        verbose_name_plural = 'Projetos'

@python_2_unicode_compatible
class Publicacao (models.Model):
    nome = models.CharField(max_length=255)
    membros = models.ManyToManyField(Membro)
    projeto = models.ForeignKey('Projetos')
    conteudo = models.TextField()
    data = models.DateField(default=datetime.now())
    arquivo = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Publicacao'
        verbose_name_plural = 'Publicacoes'

@python_2_unicode_compatible
class contato (models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mensagem = models.TextField()


    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Contanto'
        verbose_name_plural = 'Contato'
