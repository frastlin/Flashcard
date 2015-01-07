#coding: utf-8
"""
The documentaion describing authentication process is available on:
http://www.ivona.com/speech-cloud
"""

import hmac
import posixpath
from hashlib import sha256 as sha256
import datetime

import six

from six.moves.urllib.parse import quote
from ivonaspeechcloud.const import METHOD_POST


class AuthenticationHelper(object):
    AWS_REQUEST = 'aws4_request'
    SERVICE_NAME = "tts"
    HASH_ALGORITHM = 'AWS4-HMAC-SHA256'
    DATE_FORMAT = '%Y%m%dT%H%M%SZ'

    @staticmethod
    def _sign(key, msg, hex_digest=False):
        sig = hmac.new(key, msg.encode('utf-8'), sha256)
        return sig.hexdigest() if hex_digest else sig.digest()

    @staticmethod
    def host_header(http_request):
        """Generate Host header."""
        port = http_request.port
        secure = http_request.protocol == 'https'
        if (port == 80 and not secure) or (port == 443 and secure):
            return http_request.host
        return '%s:%s' % (http_request.host, port)

    @classmethod
    def formatted_now(cls):
        return datetime.datetime.utcnow().strftime(cls.DATE_FORMAT)

    @staticmethod
    def get_utf8_value(value):
        if isinstance(value, six.text_type):
            return value.encode('utf-8')
        else:
            return value

    @staticmethod
    def canonical_headers(headers_to_sign):
        """Return the headers that need to be included in the StringToSign
        in their canonical form by converting all header keys to lower
        case, sorting them in alphabetical order and then joining
        them into a string, separated by newlines.
        """
        canonical = []

        for header in headers_to_sign:
            c_name = header.lower().strip()
            c_value = ' '.join(headers_to_sign[header].strip().split())
            canonical.append('%s:%s' % (c_name, c_value))
        return '\n'.join(sorted(canonical))

    @staticmethod
    def signed_headers(headers_to_sign):
        return ';'.join(sorted([n.lower().strip() for n in headers_to_sign]))

    @staticmethod
    def canonical_uri(http_request):
        """Generates canonical URI from the request."""
        path = http_request.auth_path
        # Normalize the path
        # in windows normpath('/') will be '\\' so we change it back to '/'
        normalized = posixpath.normpath(path).replace('\\', '/')
        # Then urlencode whatever's left.
        encoded = quote(normalized)
        if len(path) > 1 and path.endswith('/'):
            encoded += '/'
        return encoded

    @staticmethod
    def payload_hash(http_request):
        """Computes hash of the payload."""
        return sha256(http_request.get_post_payload().encode('utf-8')).hexdigest()

    @classmethod
    def headers_to_sign(cls, http_request):
        """Select the headers from the request that need to be included
        in the StringToSign.
        """
        host_header_value = cls.host_header(http_request)
        headers_to_sign = {'Host': host_header_value}
        for name, value in http_request.headers.items():
            lname = name.lower()
            if lname.startswith('x-amz'):
                headers_to_sign[name] = value
        return headers_to_sign


    @classmethod
    def canonical_query_string(cls, method, qs_params):
        """Generates query string which is used for signing the request afterwards."""
        if method == METHOD_POST:
            return ""
        parts = []
        non_quote_chars = '-_.~'
        for param, value in sorted(list(qs_params.items())):
            utf8_value = cls.get_utf8_value(value)
            parts.append('%s=%s' % (quote(param, safe=non_quote_chars),
                                    quote(utf8_value, safe=non_quote_chars)))
        return '&'.join(parts)

    @classmethod
    def canonical_request(cls, http_request, method, qs_params):
        """Generates string from request which is signed afterwards."""
        headers_to_sign = cls.headers_to_sign(http_request)
        return '\n'.join(
            [method.upper(), cls.canonical_uri(http_request), cls.canonical_query_string(method, qs_params),
             cls.canonical_headers(headers_to_sign) + '\n', cls.signed_headers(headers_to_sign),
             cls.payload_hash(http_request)])

    @classmethod
    def credential_scope(cls, timestamp, region_name):
        """
        Generate credential scope string.
        """
        return '/'.join([timestamp, region_name, cls.SERVICE_NAME, cls.AWS_REQUEST])

    @classmethod
    def scope(cls, provider, timestamp, region_name):
        """
        Generate scope string.
        """
        return '{0}/{1}'.format(provider.access_key, cls.credential_scope(timestamp, region_name))

    @classmethod
    def string_to_sign(cls, timestamp, region_name, canonical_request, formatted_now):
        """Return the canonical StringToSign."""
        sts = [cls.HASH_ALGORITHM, formatted_now, cls.credential_scope(timestamp, region_name),
               sha256(canonical_request.encode('utf-8')).hexdigest()]
        return '\n'.join(sts)

    @classmethod
    def signature(cls, provider, string_to_sign, timestamp, region_name):
        """Computes the signature."""
        key = provider.secret_key
        k_date = cls._sign(('AWS4' + key).encode('utf-8'), timestamp)
        k_region = cls._sign(k_date, region_name)
        k_service = cls._sign(k_region, cls.SERVICE_NAME)
        k_signing = cls._sign(k_service, cls.AWS_REQUEST)
        return cls._sign(k_signing, string_to_sign, hex_digest=True)
