# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-06-06 00:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vip',
            options={'ordering': ['level']},
        ),
    ]
