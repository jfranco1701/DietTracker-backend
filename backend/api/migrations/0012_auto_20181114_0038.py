# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_food_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
