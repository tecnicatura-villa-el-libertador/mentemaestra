# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('juego', '0005_jugador_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='user',
        ),
        migrations.AddField(
            model_name='jugador',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.Session'),
        ),
    ]
