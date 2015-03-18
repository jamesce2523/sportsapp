# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='grade',
            field=models.CharField(max_length=50, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='players',
            name='hometown',
            field=models.CharField(default=2, unique=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='players',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
