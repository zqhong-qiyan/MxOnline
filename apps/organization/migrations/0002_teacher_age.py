# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-20 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=27, max_length=50, verbose_name='讲师年龄'),
        ),
    ]
