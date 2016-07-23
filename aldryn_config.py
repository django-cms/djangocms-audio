# -*- coding: utf-8 -*-
from aldryn_client import forms
from django.template.defaultfilters import slugify


class Form(forms.BaseForm):
    templates = forms.CharField(
        'List of additional templates (comma separated)',
        required=False,
    )

    def clean(self, value):
        return slugify([x.strip() for x in value.split(',')])


    def to_settings(self, data, settings):
        settings['DJANGOCMS_AUDIO_TEMPLATES'] = clean(templates)
        return settings
