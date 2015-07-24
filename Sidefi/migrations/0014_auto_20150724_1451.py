# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0013_remove_distrito_encargado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centro',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
