# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visita',
            options={'ordering': ['creada'], 'verbose_name_plural': 'Visitas'},
        ),
        migrations.RemoveField(
            model_name='visita',
            name='fecha_creada',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='fecha_modificada',
        ),
        migrations.AddField(
            model_name='visita',
            name='creada',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 0, 34, 35, 630625, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visita',
            name='modificada',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 0, 34, 43, 277055, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
