# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
