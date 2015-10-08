# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0006_auto_20150619_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='codigo',
            field=models.ForeignKey(verbose_name=b'Codigo de la visita', to='Sidefi.Parametros'),
        ),
    ]
