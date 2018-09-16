# -*- coding: utf-8 -*-


class Speech:

    def __init__(self):
        self.speech = ""

    def speak(self):
        """
        <speak>タグで囲う
        :return:
        """
        return '<speak>{}</speak>'.format(self.speech)

    def say(self, value):
        """
        テキストの追加
        :return:
        """
        self.speech += value
        return self

    def say_as(self, value, interpret_as):
        """
        <say_as>タグで囲う
        :param value:
        :param interpret_as:
        :return:
        """
        self.speech += '<say-as interpret-as="{}">{}</say-as>'.format(interpret_as, value)
        return self

    def prosody(self, value, rate):
        """
        <prosody>タグで囲う
        :param value:
        :param rate:
        :return:
        """
        self.speech += '<prosody rate="{}">{}</prosody>'.format(rate, value)
        return self

    def sub(self, alias, value):
        """
        <sub>タグで囲う
        :param alias:
        :param value:
        :self.speech +=:
        """
        self.speech += '<sub alias="{}">{}</sub>'.format(alias, value)
        return self

    def pause(self, time):
        """
        <break>タグを生成
        :param time:
        :return:
        """
        self.speech += '<break time="{}"/>'.format(time)
        return self
