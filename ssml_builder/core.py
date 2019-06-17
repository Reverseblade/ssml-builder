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
    def prosody(value, rate):
        """
        <prosody>
        :param value:
        :param rate:
        :return:
        """
        return '<prosody rate="{}">{}</prosody>'.format(rate, value)

    @staticmethod
    def sub(value, alias):
        """
        <sub>
        :param alias:
        :param value:
        :self.speech +=:
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
        return '<lang xml:lang="{}"/>{}</lang>'.format(lang, value)

    @staticmethod
    def voice(value, name):
        """
        <voice>
        :param value:
        :param name:
        :return:
        """
        return '<voice name="{}"/>{}</voice>'.format(name, value)

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

    def prosody(self, value, rate):
        """
        <prosody>
        :param value:
        :param rate:
        :return:
        """
        self.speech += '<prosody rate="{}">{}</prosody>'.format(rate, value)
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

    # def lang(self, value, lang, option='default'):
    #     """
    #     <lang>
    #     :param value:
    #     :param lang:
    #     :param option:
    #     :return:
    #     """
    #
    #     if option is '':
    #     else:
    #         self.speech += '<lang xml:lang="{}"/>{}</lang>'.format(lang, value)
    #     return self

    def voice(self, value, name):
        """
        <voice>
        :param value:
        :param name:
        :return:
        """
        self.speech += '<voice name="{}"/>{}</voice>'.format(name, value)
        return self

    def pause(self, time):
        """
        <break>
        :param time:
        :return:
        """
        self.speech += '<break time="{}"/>'.format(time)
        return self


