# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0023_auto_20170109_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='provider',
            field=models.CharField(default=b'dhru', max_length=16, choices=[(b'', b''), (b'dhru', b'DHRU'), (b'naksh', b'Naksh Soft'), (b'gsm', b'Gsm Genie')]),
        ),
    ]
