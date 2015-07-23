# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0004_auto_20150618_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visita',
            name='individuo',
        ),
        migrations.AddField(
            model_name='visita',
            name='individuo',
            field=models.ForeignKey(default=1, to='Sidefi.Individuo'),
            preserve_default=False,
        ),
    ]
