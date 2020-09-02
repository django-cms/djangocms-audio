from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class AudioPlayerPlugin(CMSPluginBase):
    model = models.AudioPlayer
    name = _('Audio player')
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
        context = super().render(context, instance, placeholder)
        context['audio_template'] = instance.template
        return context

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/audio_player.html'.format(instance.template)


class AudioFilePlugin(CMSPluginBase):
    model = models.AudioFile
    name = _('File')
    module = _('Audio player')
    allow_children = True
    require_parent = True
    parent_classes = ['AudioPlayerPlugin']
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


class AudioTrackPlugin(CMSPluginBase):
    model = models.AudioTrack
    name = _('Track')
    module = _('Audio player')
    require_parent = True
    parent_classes = ['AudioFilePlugin']

    fieldsets = [
        (None, {
            'fields': (
                'kind',
                'src',
                'srclang',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'label',
                'attributes',
            )
        })
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_audio/{}/track.html'.format(context['audio_template'])


plugin_pool.register_plugin(AudioPlayerPlugin)
plugin_pool.register_plugin(AudioFilePlugin)
plugin_pool.register_plugin(AudioFolderPlugin)
plugin_pool.register_plugin(AudioTrackPlugin)
