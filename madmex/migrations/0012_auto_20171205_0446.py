# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 04:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madmex', '0011_auto_20171205_0445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Footprints',
            new_name='Footprint',
        ),
    ]