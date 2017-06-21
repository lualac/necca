# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170621_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projetos',
            options={'verbose_name': 'Publicacao', 'verbose_name_plural': 'Publicacao'},
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 6, 21, 16, 19, 44, 106357)),
        ),
    ]
