# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 13:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170621_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 9, 5, 10, 8, 51, 493808)),
        ),
    ]
