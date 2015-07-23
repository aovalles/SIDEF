# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0007_auto_20150619_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='individuo',
            name='eliminado',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='parametros',
            name='rangoEdad',
            field=models.CharField(default=-104, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visita',
            name='eliminado',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
    ]
