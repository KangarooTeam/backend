# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20180527_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Автор'),
        ),
    ]