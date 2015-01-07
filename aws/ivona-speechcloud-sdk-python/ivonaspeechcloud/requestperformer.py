#coding: utf-8

import requests
from six.moves.urllib.parse import urlencode

from ivonaspeechcloud.const import METHOD_GET, METHOD_POST
from ivonaspeechcloud.exceptions import FailedRequestException


class Result(object):
    """It is returned as a result after performing speechcloud request."""

    def __init__(self, response):
        self.response = response

    @property
    def headers(self):
        """Returns response headers as a dict."""
        return self.response.headers

    @property
    def chunks(self):
        """Generator making it possible to obtain chunks of data as they come."""
        for chunk in self.response.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

    @property
    def json(self):
        """Returns a result as JSON if possible."""
        return self.response.json()


class BaseRequestPerformer(object):
    def make_request(self, host, path, method, headers, qs_params, payload, stream=True):
        """This method should be overridden in subclasses. It is responsible for performing actual request.

        It should return Result object in case of a success or raise FailedRequestException in case of an error.
        """
        raise NotImplementedError()

    def generate_qs(self, qs_params):
        return urlencode(list(qs_params.items()))

    def get_full_path(self, endpoint, url_path, method, auth_params):
        base_url = "https://{0}{1}".format(endpoint, url_path)
        if method == METHOD_GET:
            return "{0}?{1}".format(base_url, self.generate_qs(auth_params.query_string))
        elif method == METHOD_POST:
            return base_url


class DefaultRequestPerformer(BaseRequestPerformer):
    def make_request(self, host, path, method, auth_params, stream=True):
        full_path = self.get_full_path(host, path, method, auth_params)
        if method == METHOD_GET:
            res = requests.get(full_path, stream=stream)
        elif method == METHOD_POST:
            res = requests.post(full_path, data=auth_params.payload, headers=auth_params.headers, stream=stream)

        if res.status_code == 200:
            return Result(res)
        else:
            raise FailedRequestException(res.status_code, res.text)
