from django.db import models
from datetime import datetime
#from django.utils import timezone

class Membro (models.Model):
    nome = models.CharField(max_length=255)
    cnpq = models.TextField()
    foto = models.FileField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nome

class LinhaDePesquisa (models.Model):
      nome = models.CharField(max_length=255)
      icone = models.CharField(max_length=255)

      def __str__(self):
          return self.nome

class Projetos (models.Model):
    linha_dp = models.ForeignKey('LinhaDePesquisa')
    nome = models.CharField(max_length=255)
    membros = models.ManyToManyField(Membro)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Projetos'
        verbose_name_plural = 'Projetos'


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
