# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 03:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_auto_20171022_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='codigo_compra',
            new_name='codigoCompra',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='id_producto',
            new_name='idProducto',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='nit_proveedor',
            new_name='nitProveedor',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='valor_compra',
            new_name='valorCompra',
        ),
    ]