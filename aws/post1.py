import sys, os, base64, datetime, hashlib, hmac
import requests
import logging

import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

#You must initialize logging or you will not see debug output
logging.basicConfig()
logging.getLogger()
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

#***request values***
method = 'POST'
service = 'tts'
host = 'tts.eu-west-1.ivonacloud.com'
region = 'eu-west-1'
endpoint = 'https://tts.eu-west-1.ivonacloud.com/'

content_type = 'application/json'

x_amz_content = 'f43e25253839f2c3feae433c5e477d79f7dfafdc0e4af19a952adb44a60265ba'

request_parameters = '{"Input": {"Data":"Hello World"}}'


#Key functions:
def sign(key, msg):
	return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, date_stamp, regionName, serviceName):
	kDate = sign(('AWS4' + key).encode('utf-8'), date_stamp)
	kRegion = sign(kDate, regionName)
	kService = sign(kRegion, serviceName)
	kSigning = sign(kService, 'aws4_request')
	return kSigning

#Keys:
#access_key = os.environ.get('AWS_ACCESS_KEY_ID')
#secret_key = os.environ.get('AWS_ACCESS_KEY_ID')
access_key = 'GDNAJQO7QNIHPQHRRY4A'
secret_key = 'RWAMvzQjB4PB76HEHkwOQP9cEpuU62nrP+I6PFff'


#create a date for headers and the credential string
t = datetime.datetime.utcnow()
amz_date = t.strftime('%Y%m%dT%H%M%SZ')
date_stamp = t.strftime('%Y%m%d') # date w/o time, used in credential scope


#***task 1: creat a canonical task***
canonical_uri = '/CreateSpeech'

canonical_querystring = ''

#not sure about this, but I have:
#'x-amz-content-sha256:' + x_amz_content + '\n'  
canonical_headers = 'content-type:' + content_type + '\n' + 'host:' + host + '\n' + 'x-amz-date:' + amz_date + '\n'

signed_headers = 'content-type;host;x-amz-date'

payload_hash = hashlib.sha256(request_parameters).hexdigest()

canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

#create the string to sign
#match the algorithm to the hashing algorithm you use, either SHA-1 or SHA-256 (recommended)
algorithm = 'AWS4-HMAC-SHA256'
credential_scope = date_stamp + '/' + region + '/' + service + '/' + 'aws4_request'
string_to_sign = algorithm + '\n' + amz_date + '\n' + credential_scope + '\n' + hashlib.sha256(canonical_request).hexdigest()

#calculate the signiture
#create the signing key using the function defined above.
signing_key = getSignatureKey(secret_key, date_stamp, region, service)

# sign the string_to_sign using the signing_key.
signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

#add signing information to the request
#put the signiture information in a header named authorization.
authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature


#The headers must be included in the canonical_headers and signed_headers values, as noted earlier.
#order here is not significant.
#python note: the 'host' header is added automatically by the python 'requests' library.
headers = {'Content-Type': content_type, 'X-Amz-Date': amz_date, 'Authorization': authorization_header}

#***Send the request***
print 'begin request+++'
print 'request url = ' + endpoint

r = requests.post(endpoint, data=request_parameters, headers=headers)

print 'response+++'
print 'response code: %d' % r.status_code
print r.text

