# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-05-02 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dating_sex',
            field=models.CharField(choices=[('男性', '男性'), ('女性', '女性')], default='女', max_length=8, verbose_name='匹配的性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=256, verbose_name='个人形象'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_day',
            field=models.IntegerField(default=1, verbose_name='出生日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_month',
            field=models.IntegerField(default=1, verbose_name='出生月'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_year',
            field=models.IntegerField(default=2000, verbose_name='出生年'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=32, verbose_name='常居地'),
        ),
    ]