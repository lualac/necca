# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170621_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projetos',
            options={'verbose_name': 'Projetos', 'verbose_name_plural': 'Projetos'},
        ),
        migrations.AlterModelOptions(
            name='publicacao',
            options={'verbose_name': 'Publicacao', 'verbose_name_plural': 'Publicacoes'},
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 6, 21, 16, 21, 27, 964734)),
        ),
    ]
