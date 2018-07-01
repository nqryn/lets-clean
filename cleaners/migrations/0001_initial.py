# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('quality_score', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
