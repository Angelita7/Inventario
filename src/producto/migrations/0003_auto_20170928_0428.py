# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='ganancia',
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
