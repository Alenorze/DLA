# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20171102_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default='page-slug'),
        ),
    ]
