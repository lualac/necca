# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinhaDePesquisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('icone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('cnpq', models.TextField()),
                ('foto', models.FileField(null=True, upload_to=b'', blank=True)),
                ('biografia', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('linha_dp', models.ForeignKey(to='blog.LinhaDePesquisa')),
                ('membros', models.ManyToManyField(to='blog.Membro')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('data', models.DateField(default=datetime.datetime(2017, 6, 21, 16, 5, 26, 848925))),
                ('arquivo', models.FileField(null=True, upload_to=b'', blank=True)),
                ('membro', models.ForeignKey(to='blog.Membro')),
                ('projeto', models.ForeignKey(to='blog.Projetos')),
            ],
        ),
    ]
