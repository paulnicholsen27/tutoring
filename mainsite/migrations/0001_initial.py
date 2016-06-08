# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('opening_content', models.TextField()),
                ('extended_content', models.TextField(blank=True, null=True)),
                ('published', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]