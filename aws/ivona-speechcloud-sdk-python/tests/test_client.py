#coding: utf-8
import unittest
from mock import Mock, patch
from ivonaspeechcloud.authentication import AuthenticatedParams
from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_GET, METHOD_POST

MockRequestPerformer = Mock()


class TestClient(unittest.TestCase):
    ACCESS_KEY = 'a'
    SECRET_KEY = 's'
    NOW_DATE = "20140606T101737Z"

    SPEECH = 'speech'

    def setUp(self):
        self.MockRequestPerformer = Mock()
        self.sut = SpeechCloudClient(self.ACCESS_KEY, self.SECRET_KEY, self.MockRequestPerformer)

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_create_speech_get(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        self.sut.create_speech(self.SPEECH, method=METHOD_GET)
        self.MockRequestPerformer.make_request.assert_called_once_with('tts.eu-west-1.ivonacloud.com', '/CreateSpeech', 'GET', AuthenticatedParams({}, {'X-Amz-Credential': 'a/20140606/eu-west-1/tts/aws4_request', 'X-Amz-Signature': '8d70bea439ffb5327cb9335a22b0a99d9f81426ea170b3ad830e4d7c54bc509e', 'X-Amz-Algorithm': 'AWS4-HMAC-SHA256', 'X-Amz-Date': '20140606T101737Z', 'Input.Data': 'speech', 'X-Amz-SignedHeaders': 'host'}, None))

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_create_speech_post(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        self.sut.create_speech(self.SPEECH, method=METHOD_POST)
        self.MockRequestPerformer.make_request.assert_called_once_with('tts.eu-west-1.ivonacloud.com', '/CreateSpeech', 'POST', AuthenticatedParams({'X-Amz-Date': '20140606T101737Z', 'Authorization': 'AWS4-HMAC-SHA256 Credential=a/20140606/eu-west-1/tts/aws4_request, SignedHeaders=host, Signature=3f98001a865bc3f0e8404cd09aed5974a1c33cb780b33ddf6671326792b22a2d'}, {}, '{"Input": {"Data": "speech"}}'))

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_create_speech_url(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        self.sut.create_speech_url(self.SPEECH)
        self.MockRequestPerformer.get_full_path.assert_called_once_with('tts.eu-west-1.ivonacloud.com', '/CreateSpeech', 'GET', AuthenticatedParams({}, {'X-Amz-Algorithm': 'AWS4-HMAC-SHA256', 'X-Amz-SignedHeaders': 'host', 'X-Amz-Credential': 'a/20140606/eu-west-1/tts/aws4_request', 'X-Amz-Date': '20140606T101737Z', 'X-Amz-Signature': '8d70bea439ffb5327cb9335a22b0a99d9f81426ea170b3ad830e4d7c54bc509e', 'Input.Data': 'speech'}, None))

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_list_voices_get(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        self.sut.list_voices(method=METHOD_GET)
        self.MockRequestPerformer.make_request.assert_called_once_with('tts.eu-west-1.ivonacloud.com', '/ListVoices', 'GET', AuthenticatedParams({}, {'X-Amz-Algorithm': 'AWS4-HMAC-SHA256', 'X-Amz-SignedHeaders': 'host', 'X-Amz-Date': '20140606T101737Z', 'X-Amz-Signature': 'b17a2ff485b1af570bcaa7693f0efff6c701c1af7578e0b2e8cd00c5a1670ab7', 'X-Amz-Credential': 'a/20140606/eu-west-1/tts/aws4_request'}, None))

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_list_voices_post(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        self.sut.list_voices(method=METHOD_POST)
        self.MockRequestPerformer.make_request.assert_called_once_with('tts.eu-west-1.ivonacloud.com', '/ListVoices', 'POST', AuthenticatedParams({'X-Amz-Date': '20140606T101737Z', 'Authorization': 'AWS4-HMAC-SHA256 Credential=a/20140606/eu-west-1/tts/aws4_request, SignedHeaders=host, Signature=ccc1c8e3486cb048ff47c96d208e2ff06f6dc55044a4861688e839393f3b9fb1'}, {}, '{}'))

    @patch('ivonaspeechcloud.authenticationhelper.AuthenticationHelper.formatted_now')
    def test_list_voices_url(self, datetime_now_mock):
        datetime_now_mock.return_value = self.NOW_DATE
        self.sut.list_voices_url()
        self.MockRequestPerformer.get_full_path.assert_called_once_with('tts.eu-west-1.ivonacloud.com', '/ListVoices', 'GET', AuthenticatedParams({}, {'X-Amz-Credential': 'a/20140606/eu-west-1/tts/aws4_request', 'X-Amz-SignedHeaders': 'host', 'X-Amz-Algorithm': 'AWS4-HMAC-SHA256', 'X-Amz-Signature': 'b17a2ff485b1af570bcaa7693f0efff6c701c1af7578e0b2e8cd00c5a1670ab7', 'X-Amz-Date': '20140606T101737Z'}, None))