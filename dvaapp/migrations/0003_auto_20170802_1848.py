# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0002_auto_20170802_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tevent',
            name='arguments_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
