# -*- coding: utf-8 -*-
from aldryn_client import forms

class Form(forms.BaseForm):
    templates = forms.CharField(
        'List of additional templates (comma separated)',
        required=False,
    )

    def to_settings(self, data, settings):
        settings['DJANGOCMS_AUDIO_TEMPLATES'] = cleaned_data['templates']
        return settings
