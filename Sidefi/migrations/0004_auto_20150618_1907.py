# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0003_parametros'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parametros',
            options={'verbose_name_plural': 'Parametros'},
        ),
        migrations.AlterField(
            model_name='parametros',
            name='fecha_ref',
            field=models.DateField(),
        ),
    ]
