# -*- coding: utf-8 -*-
from aldryn_client import forms
from django.template.defaultfilters import slugify


class Form(forms.BaseForm):
    templates = forms.CharField(
        'List of additional templates (comma separated)',
        required=False,
    )
    extensions = forms.CharField(
        'List of allowed extensions, default "mp3, ogg" when empty (comma separated)',
        required=False,
    )

    def clean(self, value):
        for x in value.split(','):
            yield (slugify(x.strip()), x)

    def to_settings(self, data, settings):
        settings['DJANGOCMS_AUDIO_TEMPLATES'] = self.clean(templates)
        if data[extensions]:
            settings['DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS'] = self.clean(extensions)
        return settings
