import django.db.models.deletion
from django.db import migrations, models

import djangocms_attributes_field.fields
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='djangocms_audio_audiofile', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('text_title', models.CharField(max_length=200, verbose_name='Title', blank=True)),
                ('text_description', models.TextField(verbose_name='Description', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('audio_file', filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', to='filer.File', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AudioFolder',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='djangocms_audio_audiofolder', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, help_text='Is applied to all audio file instances.', verbose_name='Attributes', blank=True)),
                ('audio_folder', filer.fields.folder.FilerFolderField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Folder', to='filer.Folder', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AudioPlayer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='djangocms_audio_audioplayer', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default='default', max_length=50, verbose_name='Template', choices=[('default', 'Default')])),
                ('label', models.CharField(max_length=200, verbose_name='Label', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AudioTrack',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='djangocms_audio_audiotrack', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('kind', models.CharField(max_length=50, verbose_name='Kind', choices=[('subtitles', 'Subtitles'), ('captions', 'Captions'), ('descriptions', 'Descriptions'), ('chapters', 'Chapters')])),
                ('srclang', models.CharField(help_text='Examples: "en" or "de" etc.', max_length=10, verbose_name='Source language', blank=True)),
                ('label', models.CharField(max_length=200, verbose_name='Label', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('src', filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Source file', to='filer.File', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
