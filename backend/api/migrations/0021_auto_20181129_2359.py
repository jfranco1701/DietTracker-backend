# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20181128_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='food',
        ),
        migrations.AddField(
            model_name='favorite',
            name='calories',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='favorite',
            name='carbs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='favorite',
            name='fat',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='favorite',
            name='fiber',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='favorite',
            name='foodname',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AddField(
            model_name='favorite',
            name='measure',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AddField(
            model_name='favorite',
            name='protein',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='favorite',
            name='sugars',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
    ]
