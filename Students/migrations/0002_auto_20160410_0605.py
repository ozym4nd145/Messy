# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 00:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='me',
            new_name='name',
        ),
    ]