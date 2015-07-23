# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0005_auto_20150618_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametros',
            name='codigo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametros',
            name='descripcion',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametros',
            name='estatus',
            field=models.CharField(default=1, max_length=1, choices=[(b'C', b'Completa'), (b'I', b'Incompleta')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visita',
            name='codigo',
            field=models.ForeignKey(default=1, to='Sidefi.Parametros'),
            preserve_default=False,
        ),
    ]
