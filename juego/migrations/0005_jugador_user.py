# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 22:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('juego', '0004_auto_20160815_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
