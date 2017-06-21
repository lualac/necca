# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacao',
            name='membro',
        ),
        migrations.AddField(
            model_name='publicacao',
            name='membros',
            field=models.ManyToManyField(to='blog.Membro'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 6, 21, 16, 9, 42, 516887)),
        ),
    ]
