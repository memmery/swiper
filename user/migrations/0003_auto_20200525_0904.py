# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-05-25 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200502_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dating_sex',
            field=models.CharField(choices=[('男性', '男性'), ('女性', '女性')], default='女性', max_length=8, verbose_name='匹配的性别'),
        ),
    ]
