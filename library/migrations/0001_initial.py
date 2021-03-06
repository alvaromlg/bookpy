# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('datehelper_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='utils.DateHelper')),
                ('name', models.CharField(max_length=100)),
            ],
            bases=('utils.datehelper',),
        ),
        migrations.CreateModel(
            name='BookCase',
            fields=[
                ('datehelper_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='utils.DateHelper')),
                ('book_case_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=2000)),
            ],
            bases=('utils.datehelper',),
        ),
    ]
