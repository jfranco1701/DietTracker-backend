# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20181127_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='food',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='quantity',
        ),
        migrations.AddField(
            model_name='food',
            name='meal',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='foodinfo', to='api.Meal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]