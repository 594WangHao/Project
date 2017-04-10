# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_data_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='remarks',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='备注信息'),
            preserve_default=False,
        ),
    ]