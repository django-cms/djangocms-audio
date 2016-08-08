# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):
    templates = forms.CharField(
        'List of additional templates (comma separated)',
        required=False,
    )
    extensions = forms.CharField(
        'List of allowed extensions, default "mp3, ogg" when empty (comma separated)',
        required=False,
    )

    def clean(self):
        data = super(Form, self).clean()
        data['templates'] = [item.strip() for item in data['templates'].split(',')]
        data['extensions'] = [item.strip() for item in data['extensions'].split(',')]
        return data

    def to_settings(self, data, settings):
        # validate aldryn settings
        if data['templates']:
            settings['DJANGOCMS_AUDIO_TEMPLATES'] = [(item, item) for item in data['templates']]
        if data['extensions']:
            settings['DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS'] = data['extensions']
        return settings
