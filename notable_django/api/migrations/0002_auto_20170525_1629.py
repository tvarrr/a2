# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='title',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='note',
            name='body',
        ),
        migrations.AddField(
            model_name='note',
            name='key',
            field=models.CharField(default='default', max_length=60),
        ),
    ]
