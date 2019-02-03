# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20161120_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='level',
            field=models.CharField(default=b'1', max_length=1, null=True, blank=True, choices=[(b'Level 1 ', b'1'), (b'Level 2 ', b'2'), (b'Level 3 ', b'3'), (b'Level 4 ', b'4'), (b'Level 5 ', b'5')]),
        ),
        migrations.AlterField(
            model_name='shop',
            name='rank',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
