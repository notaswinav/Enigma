# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0013_remove_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='clue',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='images',
            field=models.ManyToManyField(blank=True, to='oth.Image'),
        ),
    ]
