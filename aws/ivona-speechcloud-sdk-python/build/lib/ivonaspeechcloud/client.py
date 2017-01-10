#coding: utf-8

from ivonaspeechcloud.authentication import HmacAuthV4Handler
from ivonaspeechcloud.authentication import Credentials
from ivonaspeechcloud.const import METHOD_POST, METHOD_GET
from ivonaspeechcloud.request import CreateSpeechRequest, ListVoicesRequest
from ivonaspeechcloud.inputs import Input
from ivonaspeechcloud.requestperformer import DefaultRequestPerformer


class SpeechCloudClient(object):
    """Client for the SpeechCloud. It contains method for getting list of voices as well as creating actual speech.
    Each of these methods has a counterpart for generating the url.

    You can find example usages is the samples package.
    """

    def __init__(self, access_key, secret_key, request_performer=None, endpoint=None, region_name=None):
        """Constructs the client. It requires access_key ans secret_key.

        Request performer can be supplied here and will be used instead of default one.
        """
        self.request_performer = request_performer if request_performer else DefaultRequestPerformer()
        self.endpoint = endpoint
        self.region_name = region_name
        self.provider = Credentials(access_key, secret_key)

    def _prepare_create_speech(self, input_txt, output_format=None, parameters=None, voice=None, method=METHOD_POST):
        assert input_txt is not None

        if not hasattr(input_txt, 'data'):
            input_txt = Input(input_txt)

        req = CreateSpeechRequest(input_txt, output_format, parameters, voice, method, endpoint=self.endpoint,
                                  region_name=self.region_name)
        return req, HmacAuthV4Handler(req, self.provider).authenticated_request_params()

    def create_speech(self, input_txt, output_format=None, parameters=None, voice=None, method=METHOD_POST):
        """Performs request to perform speech synthesis."""
        req, auth_params = self._prepare_create_speech(input_txt, output_format=output_format,
                                                       parameters=parameters, voice=voice,
                                                       method=method)
        return self.request_performer.make_request(req.host, req.auth_path, method, auth_params)

    def create_speech_url(self, input_txt, output_format=None, parameters=None, voice=None):
        """Generate a URL that can be used to perform speech synthesis."""
        req, auth_params = self._prepare_create_speech(input_txt, output_format=output_format,
                                                       parameters=parameters, voice=voice,
                                                       method=METHOD_GET)
        return self.request_performer.get_full_path(req.host, req.auth_path, METHOD_GET, auth_params)

    def _prepare_list_voices(self, voice=None, method=METHOD_POST):
        req = ListVoicesRequest(voice, method, endpoint=self.endpoint, region_name=self.region_name)
        return req, HmacAuthV4Handler(req, self.provider).authenticated_request_params()

    def list_voices(self, voice=None, method=METHOD_POST):
        """Performs request to obtain a list of voices."""
        req, auth_params = self._prepare_list_voices(voice=voice, method=method)
        return self.request_performer.make_request(req.host, req.auth_path, method, auth_params)

    def list_voices_url(self, voice=None):
        """Generates URL to get a list of voices directly."""
        req, auth_params = self._prepare_list_voices(voice=voice, method=METHOD_GET)
        return self.request_performer.get_full_path(req.host, req.auth_path, METHOD_GET, auth_params)
