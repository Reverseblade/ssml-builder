# -*- coding: utf-8 -*-

import unittest
from ssml_builder.core import SSML


class TestSSML(unittest.TestCase):

    def test_say_as(self):
        ssml = SSML.say_as(value='12345', interpret_as='cardinal')
        self.assertEqual(ssml, '<say-as interpret-as="cardinal">12345</say-as>')

        ssml = SSML.say_as(value='12345', interpret_as='digits')
        self.assertEqual(ssml, '<say-as interpret-as="digits">12345</say-as>')

        ssml = SSML.say_as(value='hello', interpret_as='spell-out')
        self.assertEqual(ssml, '<say-as interpret-as="spell-out">hello</say-as>')

    def test_prosody(self):
        ssml = SSML.prosody(value="all medium")
        self.assertEqual(ssml, '<prosody rate="medium" pitch="medium" volume="medium">all medium</prosody>')

        ssml = SSML.prosody(value="x-fast", rate='x-fast')
        self.assertEqual(ssml, '<prosody rate="x-fast" pitch="medium" volume="medium">x-fast</prosody>')

        ssml = SSML.prosody(value="slow x-high", rate='slow', pitch='x-high')
        self.assertEqual(ssml, '<prosody rate="slow" pitch="x-high" volume="medium">slow x-high</prosody>')

        ssml = SSML.prosody(value="70% low x-soft", rate='70%', pitch='low', volume='x-soft')
        self.assertEqual(ssml, '<prosody rate="70%" pitch="low" volume="x-soft">70% low x-soft</prosody>')

    def test_sub(self):
        ssml = SSML.sub(value="Al", alias="aluminum")
        self.assertEqual(ssml, '<sub alias="aluminum">Al</sub>')

        ssml = SSML.sub(value="Mg", alias="magnesium")
        self.assertEqual(ssml, '<sub alias="magnesium">Mg</sub>')

    def test_lang(self):
        ssml = SSML.lang(value="Paris", lang="fr-FR")
        self.assertEqual(ssml, '<lang xml:lang="fr-FR">Paris</lang>')

    def test_voice(self):
        ssml = SSML.voice(value="I am not a real human.", name="Kendra")
        self.assertEqual(ssml, '<voice name="Kendra">I am not a real human.</voice>')

    def test_pause(self):
        ssml = SSML.pause(time="3s")
        self.assertEqual(ssml, '<break time="3s"/>')

#
# if __name__ == "__main__":
#     unittest.main()


