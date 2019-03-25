# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0005_auto_20170913_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RenameField(
            model_name='sensors',
            old_name='sensor1',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='sensors',
            old_name='sensor2',
            new_name='temperature',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]