# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-08 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180807_1354'),
        ('course', '0003_auto_20180808_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrganization', verbose_name='课程机构'),
        ),
    ]
