from django.db import models
from django.conf import settings
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
        ('standard', _('Standard')),
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
    # This enables you to add additional properties such as data attributes.
    attributes = AttributesField()

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class File(CMSPlugin):
    """
    Render a single file attaching additional meta information.
    """
    file = FilerFileField(
        verbose_name=_('File'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    is_published = models.BooleanField(
        verbose_name=_('Is Published'),
        default=True,
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
        verbose_name=_('Text Transcript'),
        blank=True,
        help_text=_('Provide a text transcript for accessibility support.'),
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
    )

    def __str__(self):
        if self.file_id and self.file.label:
            return self.file.label
        return '%s' % self.pk

    def get_short_description(self):
        if self.file_id and self.file.label:
            return self.file.label
        return ugettext('<file doesn\'t exist>')

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey (icon), it's required to copy over
        # the reference to the Icon instance to the new plugin.
        self.file = oldinstance.file


@python_2_unicode_compatible
class Folder(CMSPlugin):
    """
    All mp3 files inside a chosen filer folder will be rendered.
    If you desire more customisation (title name, description) use the
    File plugin.
    """
    folder = FilerFolderField(
        verbose_name=_('Folder'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    is_published = models.BooleanField(
        verbose_name=_('Is Published'),
        default=True,
    )

    def __str__(self):
        if self.folder_id and self.folder.name:
            return self.folder.name
        return '%s' % self.pk

    def get_short_description(self):
        if self.folder_id and self.folder.name:
            return self.folder.name
        return ugettext('<folder doesn\'t exist>')

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey (icon), it's required to copy over
        # the reference to the Icon instance to the new plugin.
        self.folder = oldinstance.folder
