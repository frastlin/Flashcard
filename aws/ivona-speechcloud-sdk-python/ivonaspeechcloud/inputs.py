#coding: utf-8
"""Contains simple classes that are used to perform requests."""


class Input(object):
    def __init__(self, data=None, data_type=None):
        self.data = data
        self.data_type = data_type


class OutputFormat(object):
    def __init__(self, codec=None, sample_rate=None):
        self.codec = codec
        self.sample_rate = sample_rate


class Parameters(object):
    def __init__(self, rate=None, volume=None, sentence_break=None, paragraph_break=None):
        self.rate = rate
        self.volume = volume
        self.sentence_break = sentence_break
        self.paragraph_break = paragraph_break


class Voice(object):
    def __init__(self, name=None, language=None, gender=None):
        self.name = name
        self.language = language
        self.gender = gender
