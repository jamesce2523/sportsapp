# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0003_auto_20150323_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='gender',
            field=models.CharField(default='m', max_length=1),
            preserve_default=False,
        ),
    ]
