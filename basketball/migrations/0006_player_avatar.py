# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0005_auto_20150401_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='avatar',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
