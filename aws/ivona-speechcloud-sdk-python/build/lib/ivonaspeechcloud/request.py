#coding: utf-8

from collections import defaultdict
import json

from ivonaspeechcloud.const import METHOD_GET, METHOD_POST

DEFAULT_ENDPOINT = "tts.eu-west-1.ivonacloud.com"
DEFAULT_REGION_NAME = "eu-west-1"


class BaseRequest(object):
    """Base SpeechCloud request"""

    URL_PATH = ''

    def __init__(self, method=METHOD_POST, endpoint=None, region_name=None, headers=None):
        self.method = method
        self.headers = headers if headers is not None else {}
        self.port = 443
        self.protocol = "https"
        self.auth_path = "/" + self.URL_PATH
        self.endpoint = endpoint if endpoint else DEFAULT_ENDPOINT
        self.region_name = region_name if region_name else DEFAULT_REGION_NAME
        self.host = self.endpoint

    def _get_params(self):
        """This method should be overriden to construct dict object containing request parameters."""
        raise NotImplementedError()

    def get_qs_params(self):
        """Returns query string dict object or empty object for POST requests."""
        if self.method == METHOD_POST:
            return {}
        return self._get_params()

    def get_post_payload(self):
        """Returns payload as a string or empty string for GET requests."""
        if self.method == METHOD_GET:
            return ""
        params = self._get_params()
        res = defaultdict(dict)
        for key, val in params.items():
            splitted = key.split(".")
            res[splitted[0]][splitted[1]] = val
        return json.dumps(res)


class CreateSpeechRequest(BaseRequest):
    """Request class for creating speech."""

    GET_PARAM_INPUT_DATA = "Input.Data"
    GET_PARAM_INPUT_TYPE = "Input.Type"
    GET_PARAM_OUTPUT_FORMAT_CODEC = "OutputFormat.Codec"
    GET_PARAM_OUTPUT_FORMAT_SAMPLE_RATE = "OutputFormat.SampleRate"
    GET_PARAM_PARAMETERS_RATE = "Parameters.Rate"
    GET_PARAM_PARAMETERS_VOLUME = "Parameters.Volume"
    GET_PARAM_PARAMETERS_PARAGRAPH_BREAK = "Parameters.ParagraphBreak"
    GET_PARAM_PARAMETERS_SENTENCE_BREAK = "Parameters.SentenceBreak"
    GET_PARAM_VOICE_NAME = "Voice.Name"
    GET_PARAM_VOICE_LANGUAGE = "Voice.Language"
    GET_PARAM_VOICE_GENDER = "Voice.Gender"

    URL_PATH = "CreateSpeech"

    def __init__(self, input_txt, output_format=None, parameters=None, voice=None, method=METHOD_POST,
                 endpoint=None, region_name=None, headers=None):
        assert input_txt is not None

        super(CreateSpeechRequest, self).__init__(method, endpoint, region_name, headers)

        self.input = input_txt
        self.output_format = output_format
        self.parameters = parameters
        self.voice = voice

    def _get_params(self):
        params = {
            self.GET_PARAM_INPUT_DATA: self.input.data,
            self.GET_PARAM_INPUT_TYPE: self.input.data_type,
            self.GET_PARAM_OUTPUT_FORMAT_CODEC: self.output_format.codec if self.output_format else None,
            self.GET_PARAM_OUTPUT_FORMAT_SAMPLE_RATE: self.output_format.sample_rate if self.output_format else None,
            self.GET_PARAM_PARAMETERS_RATE: self.parameters.rate if self.parameters else None,
            self.GET_PARAM_PARAMETERS_VOLUME: self.parameters.volume if self.parameters else None,
            self.GET_PARAM_PARAMETERS_SENTENCE_BREAK: self.parameters.sentence_break if self.parameters else None,
            self.GET_PARAM_PARAMETERS_PARAGRAPH_BREAK: self.parameters.paragraph_break if self.parameters else None,
            self.GET_PARAM_VOICE_NAME: self.voice.name if self.voice else None,
            self.GET_PARAM_VOICE_LANGUAGE: self.voice.language if self.voice else None,
            self.GET_PARAM_VOICE_GENDER: self.voice.gender if self.voice else None
        }
        return dict(filter(lambda x: x[1] is not None, params.items()))


class ListVoicesRequest(BaseRequest):
    """Request class for listing voices."""

    GET_PARAM_VOICE_NAME = "Voice.Name"
    GET_PARAM_VOICE_LANGUAGE = "Voice.Language"
    GET_PARAM_VOICE_GENDER = "Voice.Gender"

    URL_PATH = "ListVoices"

    def __init__(self, voice=None, method=METHOD_POST, endpoint=None, region_name=None, headers=None):
        super(ListVoicesRequest, self).__init__(method, endpoint, region_name, headers)

        self.voice = voice

    def _get_params(self):
        params = {
            self.GET_PARAM_VOICE_NAME: self.voice.name if self.voice else None,
            self.GET_PARAM_VOICE_LANGUAGE: self.voice.language if self.voice else None,
            self.GET_PARAM_VOICE_GENDER: self.voice.gender if self.voice else None
        }
        return dict(filter(lambda x: x[1] is not None, params.items()))
