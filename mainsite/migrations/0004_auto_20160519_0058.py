# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 00:58
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20160515_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='extended_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='opening_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]