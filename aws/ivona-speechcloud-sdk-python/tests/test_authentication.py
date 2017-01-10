#coding: utf-8
import json

import unittest
from mock import patch
from ivonaspeechcloud.authentication import HmacAuthV4Handler, Credentials
from ivonaspeechcloud.const import METHOD_GET
from ivonaspeechcloud.inputs import Input
from ivonaspeechcloud.request import CreateSpeechRequest


class TestAuthentication(unittest.TestCase):
    ACCESS_KEY = "access_key"
    SECRET_KEY = "secret_key"
    NOW_DATE = "20140606T101737Z"

    TEXT_SPEECH = 'speech'

    provider = Credentials(ACCESS_KEY, SECRET_KEY)

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_authentication_post_request(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        req = CreateSpeechRequest(Input(self.TEXT_SPEECH))
        auth_result = HmacAuthV4Handler(req, self.provider).authenticated_request_params()
        headers = auth_result[0]
        query_string = auth_result[1]
        payload = json.loads(auth_result[2])

        self.assertIn('X-Amz-Date', headers)
        self.assertIn('Authorization', headers)

        self.assertIn('Input', payload)
        self.assertDictEqual(query_string, {})

        self.assertEqual(headers['Authorization'], 'AWS4-HMAC-SHA256 Credential=access_key/20140606/eu-west-1/tts/aws4_request, SignedHeaders=host, Signature=3dd697859d9450b1d4463c0474d18260902f6442687e2b9291f7eca7ab61c296')

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_authentication_get_request(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        req = CreateSpeechRequest(Input(self.TEXT_SPEECH), method=METHOD_GET)
        auth_result = HmacAuthV4Handler(req, self.provider).authenticated_request_params()
        headers = auth_result[0]
        query_string = auth_result[1]
        payload = auth_result[2]

        self.assertDictEqual(headers, {})
        self.assertEqual(payload, None)
        self.assertIn('Input.Data', query_string)
        self.assertIn('X-Amz-Algorithm', query_string)
        self.assertIn('X-Amz-Signature', query_string)
        self.assertIn('X-Amz-SignedHeaders', query_string)
        self.assertIn('X-Amz-Credential', query_string)

        self.assertEqual(query_string['Input.Data'], self.TEXT_SPEECH)
        self.assertEqual(query_string['X-Amz-Algorithm'], 'AWS4-HMAC-SHA256')
        self.assertEqual(query_string['X-Amz-Signature'], '28b9d8f36e16dac09f7bd3740c52993b40bb1c0d24078f0b3d4370425eefab05')
        self.assertEqual(query_string['X-Amz-SignedHeaders'], 'host')
        self.assertEqual(query_string['X-Amz-Credential'], 'access_key/20140606/eu-west-1/tts/aws4_request')
