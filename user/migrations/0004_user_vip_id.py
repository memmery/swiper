# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-06-06 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200525_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vip_id',
            field=models.IntegerField(default=1, verbose_name='vip ID'),
        ),
    ]