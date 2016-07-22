# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class AudioPlayerPlugin(CMSPluginBase):
    model = models.AudioPlayer
    name = _('Audio Player')
    allow_children = True
    child_classes = ['FilePlugin', 'FolderPlugin']

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/player.html'.format(instance.template)


class FilePlugin(CMSPluginBase):
    model = models.File
    name = _('File')
    require_parent = True
    parent_classes = ['AudioPlayerPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'file',
                'text_title',
                'is_published',
            )
        }),
        (_('Advanced Settings'), {
            'classes': ('collapse',),
            'fields': (
                'text_description',
                'text_transcript',
                'attributes',
            )
        })
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/file.html'.format(
            instance.parent.get_plugin_instance()[0].template)


class FolderPlugin(CMSPluginBase):
    model = models.Folder
    name = _('Folder')
    require_parent = True
    parent_classes = ['AudioPlayerPlugin']

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/folder.html'.format(
            instance.parent.get_plugin_instance()[0].template)


plugin_pool.register_plugin(AudioPlayerPlugin)
plugin_pool.register_plugin(FilePlugin)
plugin_pool.register_plugin(FolderPlugin)
