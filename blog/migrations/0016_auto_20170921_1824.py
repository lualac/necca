# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 21:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170921_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='index',
            options={'verbose_name': 'Index', 'verbose_name_plural': 'Index'},
        ),
        migrations.RemoveField(
            model_name='index',
            name='LinhaDePesquisa',
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 9, 21, 18, 24, 31, 640890)),
        ),
    ]
