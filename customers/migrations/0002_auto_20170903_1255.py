# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-03 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
