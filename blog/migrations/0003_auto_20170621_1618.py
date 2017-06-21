# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170621_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projetos',
            options={'verbose_name': 'Publicacao', 'verbose_name_plural': 'plublicacaos'},
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 6, 21, 16, 18, 45, 958600)),
        ),
    ]
