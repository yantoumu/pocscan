# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 07:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chtscan', '0004_auto_20160408_0440'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=set([('method', 'host', 'uri')]),
        ),
    ]
