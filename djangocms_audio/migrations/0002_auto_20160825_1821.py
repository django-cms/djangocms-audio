# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_audio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='text_title',
            field=models.CharField(max_length=255, verbose_name='Title', blank=True),
        ),
        migrations.AlterField(
            model_name='audioplayer',
            name='label',
            field=models.CharField(max_length=255, verbose_name='Label', blank=True),
        ),
        migrations.AlterField(
            model_name='audioplayer',
            name='template',
            field=models.CharField(default=b'default', max_length=255, verbose_name='Template', choices=[(b'default', 'Default')]),
        ),
        migrations.AlterField(
            model_name='audiotrack',
            name='kind',
            field=models.CharField(max_length=255, verbose_name='Kind', choices=[(b'subtitles', 'Subtitles'), (b'captions', 'Captions'), (b'descriptions', 'Descriptions'), (b'chapters', 'Chapters')]),
        ),
        migrations.AlterField(
            model_name='audiotrack',
            name='label',
            field=models.CharField(max_length=255, verbose_name='Label', blank=True),
        ),
        migrations.AlterField(
            model_name='audiotrack',
            name='srclang',
            field=models.CharField(help_text='Examples: "en" or "de" etc.', max_length=255, verbose_name='Source language', blank=True),
        ),
    ]
