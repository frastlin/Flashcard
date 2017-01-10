#coding: utf-8
"""
Handles authentication required by the SpeechCloud.
Please see the documentaion available on:
http://www.ivona.com/speech-cloud
"""
from collections import namedtuple

from six.moves.urllib.parse import quote
from ivonaspeechcloud.authenticationhelper import AuthenticationHelper
from ivonaspeechcloud.const import METHOD_GET, METHOD_POST


class Credentials(object):
    """Contains secret_key and access_key."""

    def __init__(self, access_key, secret_key):
        self.secret_key = secret_key
        self.access_key = access_key


AuthenticatedParams = namedtuple('AuthenticatedRequest', ['headers', 'query_string', 'payload'])


class HmacAuthV4Handler(object):
    """Implements Version 4 HMAC authorization."""

    PARAM_NAME_AUTH = 'Authorization'
    PARAM_NAME_SIGNATURE = "X-Amz-Signature"
    PARAM_NAME_CREDENTIAL = "X-Amz-Credential"
    PARAM_NAME_SIGNED_HEADERS = "X-Amz-SignedHeaders"
    PARAM_NAME_ALGORITHM = "X-Amz-Algorithm"
    PARAM_NAME_DATE = "X-Amz-Date"

    def __init__(self, req, credentials):
        """Params:
        req - Request object of ivonaspeechcloud.request.BaseRequest type
        credentials - Credential pair object of ivonaspeechcloud.authentication.Credentials type
        """
        self.credentials = credentials
        self.req = req

    def authenticated_request_params(self):
        """Computes signature for the request and returns a named tuple containing
        headers, query string and a payload. Headers and query string are of type
        dict and payload is a string or None.

        Returned parameters can be used to build the actual request.
        """
        req = self.req

        formatted_now = AuthenticationHelper.formatted_now()
        # taking only a date part of datetime
        timestamp = formatted_now[0:8]

        headers_to_sign = AuthenticationHelper.headers_to_sign(req)
        scope = AuthenticationHelper.scope(self.credentials, timestamp, self.req.region_name)
        signed_headers = AuthenticationHelper.signed_headers(headers_to_sign)

        req_qs = req.get_qs_params()
        if req.method == METHOD_GET:
            req_qs.update({
                self.PARAM_NAME_DATE: formatted_now,
                self.PARAM_NAME_ALGORITHM: AuthenticationHelper.HASH_ALGORITHM,
                self.PARAM_NAME_SIGNED_HEADERS: signed_headers,
                self.PARAM_NAME_CREDENTIAL: scope
            })

        canonical_request = AuthenticationHelper.canonical_request(req, req.method, req_qs)
        string_to_sign = AuthenticationHelper.string_to_sign(timestamp, self.req.region_name, canonical_request,
                                                             formatted_now)
        signature = AuthenticationHelper.signature(self.credentials, string_to_sign, timestamp, self.req.region_name)

        if req.method == METHOD_GET:
            req_qs.update({
                self.PARAM_NAME_SIGNATURE: signature,
            })

            return AuthenticatedParams(headers={}, query_string=req_qs, payload=None)
        elif req.method == METHOD_POST:
            headers = {
                self.PARAM_NAME_AUTH: ', '.join(['%s Credential=%s' % (AuthenticationHelper.HASH_ALGORITHM, scope),
                                                 'SignedHeaders=%s' % signed_headers,
                                                 'Signature=%s' % signature]),
                self.PARAM_NAME_DATE: formatted_now}
            return AuthenticatedParams(headers=headers, query_string={}, payload=req.get_post_payload())
