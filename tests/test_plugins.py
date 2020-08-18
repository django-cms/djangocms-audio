from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_audio.cms_plugins import (
    AudioFilePlugin, AudioFolderPlugin, AudioPlayerPlugin, AudioTrackPlugin,
)

from .helpers import get_filer_file, get_filer_folder


class AudioPlayerPluginsTestCase(CMSTestCase):

    def setUp(self):
        self.language = "en"
        self.home = create_page(
            title='home',
            template='page.html',
            language=self.language,
        )
        self.home.publish(self.language)
        self.page = create_page(
            title='content',
            template='page.html',
            language=self.language,
        )
        self.page.publish(self.language)
        self.placeholder = self.page.placeholders.get(slot="content")
        self.superuser = self.get_superuser()
        self.audio_file = get_filer_file("test_file.mp3")
        self.track_file = get_filer_file("test_track.vtt")

    def tearDown(self):
        self.page.delete()
        self.home.delete()
        self.superuser.delete()
        self.audio_file.delete()
        self.track_file.delete()

    def test_player_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=AudioPlayerPlugin.__name__,
            language=self.language,
        )
        self.assertEqual(plugin.plugin_type, "AudioPlayerPlugin")

    def test_file_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=AudioFilePlugin.__name__,
            language=self.language,
        )
        self.assertEqual(plugin.plugin_type, "AudioFilePlugin")

    def test_folder_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=AudioFolderPlugin.__name__,
            language=self.language,
        )
        self.assertEqual(plugin.plugin_type, "AudioFolderPlugin")

    def test_track_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=AudioTrackPlugin.__name__,
            language=self.language,
        )
        self.assertEqual(plugin.plugin_type, "AudioTrackPlugin")

    def test_plugin_structure(self):
        request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        parent = add_plugin(
            placeholder=self.placeholder,
            plugin_type=AudioPlayerPlugin.__name__,
            language=self.language,
            template="default",
        )
        self.page.publish(self.language)
        self.assertEqual(parent.get_plugin_class_instance().name, "Audio player")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertIn(b"No audio file available.", response.content)

        child = add_plugin(
            target=parent,
            placeholder=self.placeholder,
            plugin_type=AudioFilePlugin.__name__,
            language=self.language,
            audio_file=self.audio_file,
        )
        self.page.publish(self.language)
        self.assertEqual(child.audio_file.label, "test_file.mp3")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertIn(b"<audio controls", response.content)
        self.assertNotIn(b"No audio file available.", response.content)
        self.assertContains(response, self.audio_file.label)

        track = add_plugin(
            target=child,
            placeholder=self.placeholder,
            plugin_type=AudioTrackPlugin.__name__,
            language=self.language,
            kind="subtitles",
            src=self.track_file,
            srclang=self.language,
        )
        self.page.publish(self.language)
        self.assertEqual(track.src.label, "test_track.vtt")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertIn(b"<track kind", response.content)
        self.assertNotIn(b"No audio file available.", response.content)
        self.assertContains(response, self.track_file.label)

        folder = add_plugin(
            target=parent,
            placeholder=self.placeholder,
            plugin_type=AudioFolderPlugin.__name__,
            language=self.language,
            audio_folder=get_filer_folder(),
        )
        self.page.publish(self.language)
        self.assertEqual(folder.audio_folder.name, "test_folder")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertContains(response, "No matching audio files were found in the specified folder.")
