# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-11 19:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0009_auto_20171007_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensors',
            name='rainfall',
            field=models.CharField(default=datetime.datetime(2017, 10, 11, 19, 20, 18, 962243, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
