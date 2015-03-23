# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0002_auto_20150318_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(unique=True)),
                ('position', models.CharField(max_length=50)),
                ('hometown', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
                ('team', models.ForeignKey(related_name=b'players', to='basketball.Team')),
            ],
            options={
                'ordering': ('number', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Players',
        ),
    ]
