# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0011_auto_20150712_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individuo',
            name='activo',
            field=models.CharField(max_length=1, choices=[(b'S', b'Si'), (b'N', b'No')]),
        ),
    ]
