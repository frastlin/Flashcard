#coding: utf-8
import json

import unittest
from ivonaspeechcloud.const import METHOD_GET, METHOD_POST
from ivonaspeechcloud.inputs import Input, OutputFormat, Parameters, Voice
from ivonaspeechcloud.request import CreateSpeechRequest


class TestRequest(unittest.TestCase):
    # parameters below might not be accepted by the SpeechCloud but it does not matter here
    SPEECH = 'speech'
    DATA_TYPE = 'text/plain'
    CODEC = 'mp3'
    RATE1 = '22050'
    RATE2 = '10000'
    VOLUME = '5'
    SENTENCE_BREAK = '10000'
    PARAGRAPH_BREAK = '10000'
    VOICE_NAME = 'jacek'
    VOICE_GENDER = 'male'
    VOICE_LANGUAGE = 'pl-PL'

    def test_get_request_one_parameter(self):
        req = CreateSpeechRequest(Input(self.SPEECH),
                                  method=METHOD_GET)
        res = req.get_qs_params()
        self.assertDictEqual(res, {'Input.Data': self.SPEECH})

    def test_get_request_all_parameters(self):
        req = self._full_request(METHOD_GET)
        res = req.get_qs_params()

        self.assertEqual(res['Input.Data'], self.SPEECH)
        self.assertEqual(res['Input.Type'], self.DATA_TYPE)
        self.assertEqual(res['OutputFormat.Codec'], self.CODEC)
        self.assertEqual(res['OutputFormat.SampleRate'], self.RATE1)
        self.assertEqual(res['Parameters.Rate'], self.RATE2)
        self.assertEqual(res['Parameters.Volume'], self.VOLUME)
        self.assertEqual(res['Parameters.ParagraphBreak'], self.PARAGRAPH_BREAK)
        self.assertEqual(res['Parameters.SentenceBreak'], self.SENTENCE_BREAK)
        self.assertEqual(res['Voice.Name'], self.VOICE_NAME)
        self.assertEqual(res['Voice.Language'], self.VOICE_LANGUAGE)
        self.assertEqual(res['Voice.Gender'], self.VOICE_GENDER)

    def test_post_request_all_parameters(self):
        req = self._full_request(METHOD_POST)
        res = json.loads(req.get_post_payload())

        self.assertEqual(res['Input']['Data'], self.SPEECH)
        self.assertEqual(res['Input']['Type'], self.DATA_TYPE)
        self.assertEqual(res['OutputFormat']['Codec'], self.CODEC)
        self.assertEqual(res['OutputFormat']['SampleRate'], self.RATE1)
        self.assertEqual(res['Parameters']['Rate'], self.RATE2)
        self.assertEqual(res['Parameters']['Volume'], self.VOLUME)
        self.assertEqual(res['Parameters']['ParagraphBreak'], self.PARAGRAPH_BREAK)
        self.assertEqual(res['Parameters']['SentenceBreak'], self.SENTENCE_BREAK)
        self.assertEqual(res['Voice']['Name'], self.VOICE_NAME)
        self.assertEqual(res['Voice']['Language'], self.VOICE_LANGUAGE)
        self.assertEqual(res['Voice']['Gender'], self.VOICE_GENDER)

    def test_post_request_one_parameter(self):
        req = CreateSpeechRequest(Input(self.SPEECH))
        res = json.loads(req.get_post_payload())
        self.assertDictEqual(res, {'Input': {'Data': self.SPEECH}})

    def _full_request(self, method):
        return CreateSpeechRequest(input_txt=Input(self.SPEECH, self.DATA_TYPE),
                            output_format=OutputFormat(self.CODEC, self.RATE1),
                            parameters=Parameters(self.RATE2, self.VOLUME, self.SENTENCE_BREAK,
                                                  self.PARAGRAPH_BREAK),
                            voice=Voice(self.VOICE_NAME, self.VOICE_LANGUAGE, self.VOICE_GENDER),
                            method=method)
