# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_profile_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='remote_addr',
            field=models.TextField(null=True, blank=True),
        ),
    ]
