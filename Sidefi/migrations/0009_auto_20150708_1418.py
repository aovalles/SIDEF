# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0008_auto_20150703_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='alturaReferencia',
            field=models.SmallIntegerField(verbose_name=b'Altura - Puntaje Z'),
        ),
        migrations.AlterField(
            model_name='visita',
            name='imcReferencia',
            field=models.SmallIntegerField(verbose_name=b'IMC - Puntaje Z'),
        ),
        migrations.AlterField(
            model_name='visita',
            name='pesoReferencia',
            field=models.SmallIntegerField(verbose_name=b'Peso - Puntaje Z '),
        ),
    ]
