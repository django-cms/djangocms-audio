# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class AudioPlayerPlugin(CMSPluginBase):
    model = models.AudioPlayer
    name = _('Audio Player')
    allow_children = True
    child_classes = ['AudioFilePlugin', 'AudioFolderPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'template',
                'label',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        })
    ]

    def render(self, context, instance, placeholder):
        context = super(AudioPlayerPlugin, self).render(context, instance, placeholder)
        context['audio_template'] = instance.template
        return context

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/audio_player.html'.format(instance.template)


class AudioFilePlugin(CMSPluginBase):
    model = models.AudioFile
    name = _('File')
    module = _('Audio player')
    require_parent = True
    child_classes = ['AudioTrackPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'audio_file',
                'text_title',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'text_description',
                'attributes',
            )
        })
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/file.html'.format(context['audio_template'])


class AudioFolderPlugin(CMSPluginBase):
    model = models.AudioFolder
    name = _('Folder')
    module = _('Audio player')
    require_parent = True
    parent_classes = ['AudioPlayerPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'audio_folder',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        })
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/folder.html'.format(context['audio_template'])


plugin_pool.register_plugin(AudioPlayerPlugin)
plugin_pool.register_plugin(AudioFilePlugin)
plugin_pool.register_plugin(AudioFolderPlugin)
