# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportProcess',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('thunder_id', models.PositiveIntegerField(verbose_name='Thundering frame id', default=0, help_text='This value is being calculated by Manager when creating task', editable=False, unique=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImportProcessLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('level', models.PositiveSmallIntegerField(choices=[(100, 'DEBUG'), (300, 'INFO'), (500, 'WARNING'), (700, 'ERROR')], default=300)),
                ('message', models.TextField()),
                ('process', models.ForeignKey(to='importing.ImportProcess')),
            ],
        ),
    ]
