# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-28 18:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaunchRock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('sign_date', models.DateTimeField(default=datetime.datetime.now)),
                ('ip', models.GenericIPAddressField()),
                ('http_refer', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
