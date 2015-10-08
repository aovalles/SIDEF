# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0010_auto_20150709_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individuo',
            name='eliminado',
        ),
        migrations.RemoveField(
            model_name='visita',
            name='eliminado',
        ),
        migrations.AddField(
            model_name='individuo',
            name='activo',
            field=models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Si'), (b'N', b'No')]),
        ),
        migrations.AddField(
            model_name='visita',
            name='activo',
            field=models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Si'), (b'N', b'No')]),
        ),
    ]
