from django.conf import settings
from django.core.exceptions import ValidationError
from django.test import TestCase

from djangocms_audio.models import (
    AudioFile, AudioFolder, AudioPlayer, AudioTrack, get_extensions,
    get_templates,
)

from .helpers import get_filer_file, get_filer_folder


class AudioPlayerModelsTestCase(TestCase):

    def setUp(self):
        self.audio = get_filer_file("test_file.mp3")
        self.folder = get_filer_folder()

    def tearDown(self):
        if self.audio:
            self.audio.delete()
            del self.audio
            with self.assertRaises(AttributeError):
                print(self.audio)
        if self.folder:
            self.folder.delete()
            del self.folder
            with self.assertRaises(AttributeError):
                print(self.folder)

        AudioPlayer.objects.filter(pk=1).delete()
        self.assertEqual(len(AudioPlayer.objects.all()), 0)
        AudioFile.objects.filter(pk=1).delete()
        self.assertEqual(len(AudioFile.objects.all()), 0)
        AudioFolder.objects.filter(pk=1).delete()
        self.assertEqual(len(AudioFolder.objects.all()), 0)
        AudioTrack.objects.filter(pk=1).delete()
        self.assertEqual(len(AudioTrack.objects.all()), 0)

    def test_settings(self):
        self.assertEqual(get_extensions(), ['mp3', 'ogg'])
        settings.DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ["mp3", "wav", "flac"]
        self.assertEqual(get_extensions(), ["mp3", "wav", "flac"])

        self.assertEqual(get_templates(), [('default', 'Default')])
        settings.DJANGOCMS_AUDIO_TEMPLATES = [('feature', 'Feature')]
        self.assertEqual(get_templates(), [('default', 'Default'), ('feature', 'Feature')])

    def test_audio_player_instance(self):
        AudioPlayer.objects.create(
            template="default",
            label="audio",
            attributes="{'data-type, 'audio'}"
        )
        instance = AudioPlayer.objects.all()
        self.assertEqual(len(instance), 1)
        instance = AudioPlayer.objects.get(pk=1)
        self.assertEqual(instance.template, "default")
        self.assertEqual(instance.label, "audio")
        self.assertEqual(instance.attributes, "{'data-type, 'audio'}")
        self.assertEqual(instance.__str__(), "audio")
        instance.label = None
        self.assertEqual(instance.__str__(), "1")

    def test_audio_file_instance(self):
        AudioFile.objects.create(
            audio_file=self.audio,
            text_title="sample title",
            text_description="sample description",
            attributes="{'data-type, 'audio'}",
        )
        instance = AudioFile.objects.all()
        self.assertEqual(len(instance), 1)
        instance = AudioFile.objects.get(pk=1)
        self.assertEqual(instance.audio_file, self.audio)
        self.assertEqual(instance.text_title, "sample title")
        self.assertEqual(instance.text_description, "sample description")
        self.assertEqual(instance.attributes, "{'data-type, 'audio'}")
        self.assertEqual(instance.__str__(), "test_file.mp3")
        self.assertEqual(instance.audio_file.label, "test_file.mp3")
        self.assertEqual(instance.audio_file_id, 1)
        self.assertEqual(instance.clean(), None)
        self.assertEqual(instance.get_short_description(), "test_file.mp3")
        # test not allowed extension
        instance.audio_file = get_filer_file("test_file.mp4")
        with self.assertRaises(ValidationError):
            instance.clean()
        instance.audio_file = instance.audio_file.delete()
        # case when the file has been removed
        self.assertEqual(instance.__str__(), "1")
        self.assertEqual(instance.clean(), None)
        self.assertEqual(instance.get_short_description(), "<file is missing>")
        # old copy relation
        instance.copy_relations(instance)
        self.assertEqual(instance.audio_file, None)

    def test_audio_folder_instance(self):
        AudioFolder.objects.create(
            audio_folder=self.folder,
            attributes="{'data-type, 'audio'}",
        )
        instance = AudioFolder.objects.all()
        self.assertEqual(len(instance), 1)
        instance = AudioFolder.objects.get(pk=1)
        self.assertEqual(instance.audio_folder, self.folder)
        self.assertEqual(instance.attributes, "{'data-type, 'audio'}")
        self.assertEqual(instance.__str__(), "test_folder")
        self.assertEqual(instance.get_short_description(), "test_folder")
        # case when the folder has been removed
        instance.audio_folder = None
        self.assertEqual(instance.__str__(), "1")
        self.assertEqual(instance.get_short_description(), "<folder is missing>")
        # old copy relation
        instance.copy_relations(instance)
        self.assertEqual(instance.audio_folder, None)

    def test_audio_folder_instance_files(self):
        self.audio = get_filer_file(
            file_name="test_file.mp3",
            folder=self.folder
        )
        instance = AudioFolder.objects.create(
            audio_folder=self.folder,
        )
        self.assertEqual(instance.get_files(), [self.audio])
        self.audio.delete()
        self.audio = get_filer_file(
            file_name="test_file.mp4",
            folder=self.folder
        )
        self.assertEqual(instance.get_files(), [])

    def test_audio_track_instance(self):
        AudioTrack.objects.create(
            kind=AudioTrack.KIND_CHOICES[0][0],
            src=self.audio,  # should be .vtt normally
            srclang="en",
            label="track label",
            attributes="{'data-type, 'audio'}",
        )
        instance = AudioTrack.objects.all()
        self.assertEqual(len(instance), 1)
        instance = AudioTrack.objects.get(pk=1)
        self.assertEqual(instance.kind, "subtitles")
        self.assertEqual(instance.src, self.audio)
        self.assertEqual(instance.srclang, "en")
        self.assertEqual(instance.label, "track label")
        self.assertEqual(instance.attributes, "{'data-type, 'audio'}")
        self.assertEqual(instance.__str__(), "subtitles (en)")
        # case when the folder has been removed
        instance.srclang = None
        self.assertEqual(instance.__str__(), "subtitles")
