# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext, ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_attributes_field.fields import AttributesField

from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField


"""
The user should be able to add an "Audio Player" plugin that serves as
a wrapper rendering the player and its options.

The "Audio Player" plugin allows to add either a single "File" or a reference
to a "Folder" as children.
"""


# mp3 is supported by all major browsers
ALLOWED_EXTENSIONS = getattr(
    settings,
    'DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS',
    ['mp3', 'ogg'],
)


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = getattr(
        settings,
        'DJANGOCMS_AUDIO_TEMPLATES',
        False,
    )
    if choices:
        return choices
    return []


@python_2_unicode_compatible
class AudioPlayer(CMSPlugin):
    DEFAULT_CHOICE = 'standard'

    # ``TEMPLATE_CHOICES`` allows you to select different templates on a per
    # plugin basis. Simply copy the ``standard`` folder from within
    # ``/templates/djangocms_audio/`` and add them to your ``STYLE_CHOICES``.
    TEMPLATE_CHOICES = [
        ('default', _('Default')),
    ]

    # The label will be displayed as help text within the structure board view.
    template = models.CharField(
        verbose_name=_('Template'),
        choices=TEMPLATE_CHOICES + get_templates(),
        default=DEFAULT_CHOICE,
        max_length=50,
    )
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=200,
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True,
    )
    # This enables you to add additional properties such as data attributes.
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
    )

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class AudioFile(CMSPlugin):
    """
    Render a single file attaching additional meta information.
    """
    audio_file = FilerFileField(
        verbose_name=_('File'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    text_title = models.CharField(
        verbose_name=_('Title'),
        blank=True,
        max_length=200,
    )
    text_description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
    )
    text_transcript = models.TextField(
        verbose_name=_('Text transcript'),
        blank=True,
        help_text=_('Provide a text transcript for accessibility support.'),
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
    )

    def __str__(self):
        if self.audio_file_id and self.audio_file.label:
            return self.audio_file.label
        return '%s' % self.pk

    def clean(self):
        if (self.audio_file and
            self.audio_file.extension not in ALLOWED_EXTENSIONS):
            raise ValidationError(
                ugettext('Incorrect file type: %s.') %
                self.audio_file.extension
            )
        pass

    def get_short_description(self):
        if self.audio_file_id and self.audio_file.label:
            return self.audio_file.label
        return ugettext('<file is missing>')

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey, it's required to copy over
        # the reference from the instance to the new plugin.
        self.audio_file = oldinstance.audio_file


@python_2_unicode_compatible
class AudioFolder(CMSPlugin):
    """
    Render files contained in a folder, only ALLOWED_EXTENSIONS are considered.
    If you desire more customisation (title name, description) use the
    File plugin.
    """
    audio_folder = FilerFolderField(
        verbose_name=_('Folder'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        help_text=_('Applied to all audio file instances.'),
    )

    def __str__(self):
        if self.audio_folder_id and self.audio_folder.name:
            return self.audio_folder.name
        return '%s' % self.pk

    def get_short_description(self):
        if self.audio_folder_id and self.audio_folder.name:
            return self.audio_folder.name
        return ugettext('<folder is missing>')

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey, it's required to copy over
        # the reference from the instance to the new plugin.
        self.audio_folder = oldinstance.audio_folder
