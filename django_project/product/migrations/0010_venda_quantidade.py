# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-26 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_venda_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='quantidade',
            field=models.IntegerField(null=True),
        ),
    ]