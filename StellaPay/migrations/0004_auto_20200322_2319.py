# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-03-22 22:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('StellaPay', '0003_auto_20200322_2316'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='StellaPay_categories',
        ),
    ]
