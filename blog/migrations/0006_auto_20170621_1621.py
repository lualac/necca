# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170621_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 6, 21, 16, 21, 36, 285656)),
        ),
    ]
