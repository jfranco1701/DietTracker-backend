# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weightdate',
            field=models.DateField(),
        ),
    ]