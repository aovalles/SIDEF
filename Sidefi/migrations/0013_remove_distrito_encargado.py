# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0012_auto_20150724_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distrito',
            name='encargado',
        ),
    ]
