# -*- coding: utf-8 -*-

import unittest
from ssml_builder.core import Speech


class TestSpeech(unittest.TestCase):

    def test_say_as(self):
        speech = Speech()
        ssml = speech.say_as(value='12345', interpret_as='cardinal', is_nested=True)
        self.assertEqual(ssml, '<say-as interpret-as="cardinal">12345</say-as>')

        ssml = speech.say_as(value='12345', interpret_as='digits', is_nested=True)
        self.assertEqual(ssml, '<say-as interpret-as="digits">12345</say-as>')

        ssml = speech.say_as(value='hello', interpret_as='spell-out', is_nested=True)
        self.assertEqual(ssml, '<say-as interpret-as="spell-out">hello</say-as>')

        speech.say_as(value='hello', interpret_as='spell-out')
        self.assertEqual(speech.speak(), '<speak><say-as interpret-as="spell-out">hello</say-as></speak>')

        speech.say_as(value='hello', interpret_as='spell-out')
        self.assertEqual(speech.speak(), '<speak><say-as interpret-as="spell-out">hello</say-as>'
                                         '<say-as interpret-as="spell-out">hello</say-as></speak>')

    def test_prosody(self):
        speech = Speech()

        ssml = speech.prosody(value="all medium", is_nested=True)
        self.assertEqual(ssml, '<prosody rate="medium" pitch="medium" volume="medium">all medium</prosody>')

        ssml = speech.prosody(value="x-fast", rate='x-fast', is_nested=True)
        self.assertEqual(ssml, '<prosody rate="x-fast" pitch="medium" volume="medium">x-fast</prosody>')

        ssml = speech.prosody(value="slow x-high", rate='slow', pitch='x-high', is_nested=True)
        self.assertEqual(ssml, '<prosody rate="slow" pitch="x-high" volume="medium">slow x-high</prosody>')

        ssml = speech.prosody(value="70% low x-soft", rate='70%', pitch='+50%', volume='x-soft', is_nested=True)
        self.assertEqual(ssml, '<prosody rate="70%" pitch="+50%" volume="x-soft">70% low x-soft</prosody>')

    def test_sub(self):
        speech = Speech()

        ssml = speech.sub(value="Al", alias="aluminum", is_nested=True)
        self.assertEqual(ssml, '<sub alias="aluminum">Al</sub>')

        ssml = speech.sub(value="Mg", alias="magnesium", is_nested=True)
        self.assertEqual(ssml, '<sub alias="magnesium">Mg</sub>')

    def test_lang(self):
        speech = Speech()

        ssml = speech.lang(value="Paris", lang="fr-FR", is_nested=True)
        self.assertEqual(ssml, '<lang xml:lang="fr-FR">Paris</lang>')

    def test_voice(self):
        speech = Speech()

        ssml = speech.voice(value="I am not a real human.", name="Kendra", is_nested=True)
        self.assertEqual(ssml, '<voice name="Kendra">I am not a real human.</voice>')

    def test_pause(self):
        speech = Speech()

        ssml = speech.pause(time="3s", is_nested=True)
        self.assertEqual(ssml, '<break time="3s"/>')

    def test_whisper(self):
        speech = Speech()

        ssml = speech.whisper("I am not a real human.", is_nested=True)
        self.assertEqual(ssml, '<amazon:effect name="whispered">I am not a real human.</amazon:effect>')

    def test_audio(self):
        speech = Speech()
        ssml = speech.audio('soundbank://soundlibrary/transportation/amzn_sfx_car_accelerate_01', is_nested=True)
        self.assertEqual(ssml, '<audio src="soundbank://soundlibrary/transportation/amzn_sfx_car_accelerate_01" />')

    def test_emphasis(self):
        speech = Speech()

        speech.add_text('I already told you I ')
        speech.emphasis('really like', 'strong')
        speech.add_text(' that person')

        self.assertEqual(speech.speak(), '<speak>I already told you I <emphasis level="strong">really like</emphasis>'
                                         ' that person</speak>')

    def test_p(self):
        speech = Speech()
        speech.p("This is the first paragraph. There should be a pause after this text is spoken.")
        speech.p("This is the second paragraph.")

        self.assertEqual(speech.speak(), '<speak><p>This is the first paragraph. There should be a pause after'
                                         ' this text is spoken.</p><p>This is the second paragraph.</p></speak>')
