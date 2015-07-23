# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Altura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('edad', models.IntegerField()),
                ('dem3', models.DecimalField(verbose_name=b'-3de', max_digits=5, decimal_places=2)),
                ('dem2', models.DecimalField(verbose_name=b'-2de', max_digits=5, decimal_places=2)),
                ('dem1', models.DecimalField(verbose_name=b'-1de', max_digits=5, decimal_places=2)),
                ('mediana', models.DecimalField(max_digits=5, decimal_places=2)),
                ('de1', models.DecimalField(verbose_name=b'+1de', max_digits=5, decimal_places=2)),
                ('de2', models.DecimalField(verbose_name=b'+2de', max_digits=5, decimal_places=2)),
                ('de3', models.DecimalField(verbose_name=b'+3de', max_digits=5, decimal_places=2)),
            ],
            options={
                'ordering': ['edad'],
                'verbose_name_plural': 'Altura para la edad',
            },
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60, blank=True)),
                ('telefono', models.CharField(max_length=11, blank=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Centros',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60, blank=True)),
                ('telefono', models.CharField(max_length=11, blank=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Distritos',
            },
        ),
        migrations.CreateModel(
            name='IMC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('edad', models.IntegerField()),
                ('dem3', models.DecimalField(verbose_name=b'-3de', max_digits=5, decimal_places=2)),
                ('dem2', models.DecimalField(verbose_name=b'-2de', max_digits=5, decimal_places=2)),
                ('dem1', models.DecimalField(verbose_name=b'-1de', max_digits=5, decimal_places=2)),
                ('mediana', models.DecimalField(max_digits=5, decimal_places=2)),
                ('de1', models.DecimalField(verbose_name=b'+1de', max_digits=5, decimal_places=2)),
                ('de2', models.DecimalField(verbose_name=b'+2de', max_digits=5, decimal_places=2)),
                ('de3', models.DecimalField(verbose_name=b'+3de', max_digits=5, decimal_places=2)),
            ],
            options={
                'ordering': ['edad'],
                'verbose_name_plural': 'Indice de masa corporal para la edad',
            },
        ),
        migrations.CreateModel(
            name='Individuo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha de Nac.')),
                ('centro', models.ForeignKey(to='Sidefi.Centro')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('edad', models.IntegerField()),
                ('dem3', models.DecimalField(verbose_name=b'-3de', max_digits=5, decimal_places=2)),
                ('dem2', models.DecimalField(verbose_name=b'-2de', max_digits=5, decimal_places=2)),
                ('dem1', models.DecimalField(verbose_name=b'-1de', max_digits=5, decimal_places=2)),
                ('mediana', models.DecimalField(max_digits=5, decimal_places=2)),
                ('de1', models.DecimalField(verbose_name=b'+1de', max_digits=5, decimal_places=2)),
                ('de2', models.DecimalField(verbose_name=b'+2de', max_digits=5, decimal_places=2)),
                ('de3', models.DecimalField(verbose_name=b'+3de', max_digits=5, decimal_places=2)),
            ],
            options={
                'ordering': ['edad'],
                'verbose_name_plural': 'Peso para la edad',
            },
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60, blank=True)),
                ('telefono', models.CharField(max_length=11, blank=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Regionales',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_auth', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.CharField(max_length=12, blank=True)),
                ('extension', models.CharField(max_length=12, blank=True)),
                ('celular', models.CharField(max_length=12, blank=True)),
                ('es_digitador', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Perfiles de usuarios',
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.PositiveSmallIntegerField(verbose_name=b'Edad')),
                ('pesoVisita', models.DecimalField(verbose_name=b'Peso', max_digits=5, decimal_places=2)),
                ('alturaVisita', models.DecimalField(verbose_name=b'Altura', max_digits=5, decimal_places=2)),
                ('imcVisita', models.DecimalField(verbose_name=b'IMC', max_digits=5, decimal_places=2)),
                ('fecha_creada', models.DateTimeField(editable=False)),
                ('fecha_modificada', models.DateTimeField()),
                ('alturaReferencia', models.ForeignKey(verbose_name=b'Altura de referencia', to='Sidefi.Altura')),
                ('imcReferencia', models.ForeignKey(verbose_name=b'IMC de referencia', to='Sidefi.IMC')),
                ('individuo', models.ManyToManyField(to='Sidefi.Individuo')),
                ('pesoReferencia', models.ForeignKey(verbose_name=b'Peso de referencia', to='Sidefi.Peso')),
            ],
            options={
                'ordering': ['fecha_creada'],
                'verbose_name_plural': 'Visitas',
            },
        ),
        migrations.AddField(
            model_name='regional',
            name='encargado',
            field=models.ManyToManyField(to='Sidefi.UserProfile'),
        ),
        migrations.AddField(
            model_name='distrito',
            name='encargado',
            field=models.ManyToManyField(to='Sidefi.UserProfile'),
        ),
        migrations.AddField(
            model_name='distrito',
            name='regional',
            field=models.ForeignKey(to='Sidefi.Regional'),
        ),
        migrations.AddField(
            model_name='centro',
            name='distrito',
            field=models.ForeignKey(to='Sidefi.Distrito'),
        ),
        migrations.AddField(
            model_name='centro',
            name='encargado',
            field=models.ManyToManyField(to='Sidefi.UserProfile'),
        ),
    ]
