# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sidefi', '0009_auto_20150708_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altura',
            name='de1',
            field=models.DecimalField(verbose_name=b'+1de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='altura',
            name='de2',
            field=models.DecimalField(verbose_name=b'+2de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='altura',
            name='de3',
            field=models.DecimalField(verbose_name=b'+3de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='altura',
            name='dem1',
            field=models.DecimalField(verbose_name=b'-1de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='altura',
            name='dem2',
            field=models.DecimalField(verbose_name=b'-2de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='altura',
            name='dem3',
            field=models.DecimalField(verbose_name=b'-3de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='altura',
            name='mediana',
            field=models.DecimalField(max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='imc',
            name='de1',
            field=models.DecimalField(verbose_name=b'+1de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='imc',
            name='de2',
            field=models.DecimalField(verbose_name=b'+2de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='imc',
            name='de3',
            field=models.DecimalField(verbose_name=b'+3de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='imc',
            name='dem1',
            field=models.DecimalField(verbose_name=b'-1de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='imc',
            name='dem2',
            field=models.DecimalField(verbose_name=b'-2de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='imc',
            name='dem3',
            field=models.DecimalField(verbose_name=b'-3de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='imc',
            name='mediana',
            field=models.DecimalField(max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='peso',
            name='de1',
            field=models.DecimalField(verbose_name=b'+1de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='peso',
            name='de2',
            field=models.DecimalField(verbose_name=b'+2de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='peso',
            name='de3',
            field=models.DecimalField(verbose_name=b'+3de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='peso',
            name='dem1',
            field=models.DecimalField(verbose_name=b'-1de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='peso',
            name='dem2',
            field=models.DecimalField(verbose_name=b'-2de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='peso',
            name='dem3',
            field=models.DecimalField(verbose_name=b'-3de', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='peso',
            name='mediana',
            field=models.DecimalField(max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='visita',
            name='alturaVisita',
            field=models.DecimalField(verbose_name=b'Altura', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='visita',
            name='imcVisita',
            field=models.DecimalField(verbose_name=b'IMC', max_digits=4, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='visita',
            name='pesoVisita',
            field=models.DecimalField(verbose_name=b'Peso', max_digits=4, decimal_places=1),
        ),
    ]
