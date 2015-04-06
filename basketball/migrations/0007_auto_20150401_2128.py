# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0006_player_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.IntegerField(),
        ),
    ]
