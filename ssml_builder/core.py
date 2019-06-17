# -*- coding: utf-8 -*-


class SSML:

    @staticmethod
    def say_as(value, interpret_as):
        """
        <say_as>
        :param value:
        :param interpret_as:
        :return:
        """
        return '<say-as interpret-as="{}">{}</say-as>'.format(interpret_as, value)

    @staticmethod
    def prosody(value, rate='medium', pitch='medium', volume='medium'):
        """
        <prosody>
        :param value:
        :param rate:
        :param pitch:
        :param volume:
        :return:
        """
        return '<prosody rate="{rate}" pitch="{pitch}" volume="{volume}">{value}' \
               '</prosody>'.format(rate=rate, pitch=pitch, volume=volume, value=value)

    @staticmethod
    def sub(value, alias):
        """
        <sub>
        :param alias:
        :param value:
        """
        return '<sub alias="{}">{}</sub>'.format(alias, value)

    @staticmethod
    def lang(value, lang):
        """
        <lang>
        :param value:
        :param lang:
        :param option:
        :return:
        """
        return '<lang xml:lang="{}">{}</lang>'.format(lang, value)

    @staticmethod
    def voice(value, name):
        """
        <voice>
        :param value:
        :param name:
        :return:
        """
        return '<voice name="{}">{}</voice>'.format(name, value)

    @staticmethod
    def pause(time):
        """
        <break>
        :param time:
        :return:
        """
        return '<break time="{}"/>'.format(time)


class Speech:

    def __init__(self):
        self.speech = ""

    def speak(self):
        """
        <speak>
        :return:
        """
        return '<speak>{}</speak>'.format(self.speech)

    def say(self, value):
        """
        add text
        :return:
        """
        self.speech += value
        return self

    def say_as(self, value, interpret_as):
        """
        <say_as>
        :param value:
        :param interpret_as:
        :return:
        """
        self.speech += '<say-as interpret-as="{}">{}</say-as>'.format(interpret_as, value)
        return self

    def prosody(self, value, rate='medium', pitch='medium', volume='medium'):
        """
        <prosody>
        :param value:
        :param rate:
        :param pitch:
        :param volume:
        :return:
        """
        self.speech += '<prosody rate="{rate}" pitch="{pitch}" volume="{volume}">' \
                       '{value}</prosody>'.format(rate=rate, pitch=pitch, volume=volume, value=value)
        return self

    def sub(self, value, alias):
        """
        <sub>
        :param alias:
        :param value:
        :self.speech +=:
        """
        self.speech += '<sub alias="{}">{}</sub>'.format(alias, value)
        return self

    def lang(self, value, lang):
        """
        <lang>
        :param value:
        :param lang:
        :param option:
        :return:
        """

        self.speech += '<lang xml:lang="{}">{}</lang>'.format(lang, value)
        return self

    def voice(self, value, name):
        """
        <voice>
        :param value:
        :param name:
        :return:
        """
        self.speech += '<voice name="{}">{}</voice>'.format(name, value)
        return self

    def pause(self, time):
        """
        <break>
        :param time:
        :return:
        """
        self.speech += '<break time="{}"/>'.format(time)
        return self


