# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_audio.models import AudioPlayer


class AudioPlayerTestCase(TestCase):

    def setUp(self):
        AudioPlayer.objects.create(
            template='default',
            label='audio',
        )

    def test_audio_player_instance(self):
        """Audio player instance has been created"""
        player = AudioPlayer.objects.get(label='audio')
        self.assertEqual(player.label, 'audio')
