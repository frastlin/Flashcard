#AWS version 4 get signing example

#EC2 api (DescribeRegions)

#see http://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html

#this version makes a get request and passes the signiture
#in the authorisation header.
import sys, os, base64, datetime, hashlib, hmac
import requests #pip install requests

#***request values***

method = 'POST'
service = '/CreateSpeech'
host = 'tts.eu-west-1.ivonacloud.com'
region = 'us-east-1'
endpoint = 'https://ec2.amazonaws.com'
request_parameters = 'Action=DescribeRegions&Version=2013-10-15'

#key derivation functions
#see: http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python

def sign(key, msg):
	return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
	kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
	kRegion = sign(kDate, regionName)
	kService = sign(kRegion, serviceName)
	kSigning = sign(kService, 'aws4_request')
	return kSigning

#read aws access key from env. Variables or configuration file. best is not
#To embed credentials in code.
#access_key = os.environ.get('AWS_ACCESS_KEY_ID')
#secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
access_key = 'GDNAJQO7QNIHPQHRRY4A'
secret_key = 'RWAMvzQjB4PB76HEHkwOQP9cEpuU62nrP+I6PFff'
if access_key is None or secret_key is None:
	print 'No access key is available.'
	sys.exit()

#Create a date for headers and the credential string
t = datetime.datetime.utcnow()
amzdate = t.strftime('%Y%m%dT%H%M%SZ')
datestamp = t.strftime('%Y%m%d')


#***Task 1, create a CANONICAL request***
# http://docs.aws.amazon.com/general/latest/gr/sigv4

#step one is to define the verb, GET, POST ect... already done.

#step 2, create canonical URI--the part of the URI from domain to query
#string, use '/' if no path
canonical_uri = '/CreateSpeech'
#canonical_uri = '/'

#step 3: create the canonical query string. in this example (a get request),
#request parameters are the query string. query string values must
# url incoded, (space=%20). The parameters must be sorted by name.
#for this example, the query string is pre-formatted in the request_parameters variable.
#canonical_querystring = request_parameters
canonical_querystring = """Input.Data=Does%20Mary%20have%20a%20little%20lamb%3F&Input.Type=text%2Fplain&
#  *~*

#step 4: create the canonical headers and signed headers. header names
# and value must be trimmed and lowercase and in ASCII order.
# note that there is a trailing \n.
canonical_headers = 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'

#step 5: create the list of signed headers. this lists the headers
#in the canonical_headers list, delimited with ";" and in alpha order.
# note: the request can include any headers; canonical_headers and
#signed_headers lists those that you want to be included in the
# hash of the request. "Host" and "x-amz-date" are always required.
signed_headers = 'host;x-amz-date'

#step 6: create payload hash (hash of the request body content). for get
#requests, the payload is an empty string ("").
payload_hash = hashlib.sha256('').hexdigest()

#step 7: combine elaments to create create canonical request
canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

#***task 2: create the string to sign***
#match the algorithm or the hashing algorithm you use, either SHA-1 or
#SHA-256 (recommended)
algorithm = 'AWS4-HMAC-SHA256'
credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
string_to_sign = algorithm + '\n' + amzdate + '\n' + credential_scope + '\n' + hashlib.sha256(canonical_request).hexdigest()

#***task 3: calculate the signiture***
#create the signing key using the function above.
signing_key = getSignatureKey(secret_key, datestamp, region, service)

#sign string_to_sign using the signing_key
signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

#***task 4: add signing information to the task***
#signing information can either be in a query string value or in
#a header named authorisation. This code shows how to use a header.
#create authorisation header and add to request headers 
authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

#The request can include any headers, but must include "host", "x-amz-date",
#and (for this scenario), "Authorization". "host" and "x-amz-date" must
#be included in the canonical_headers and signed_headers, as noted
#earlier. Order here is not significant.
#python note: The python 'host' header is added automatically by the python 'requests' library.
headers = {'x-amz-date':amzdate, 'Authorization':authorization_header}

#***Send the request***
request_url = endpoint + '?' + canonical_querystring

print "\n begin request..."
print "request url =" + request_url
r = requests.get(request_url, headers=headers)

print "\nresponce..."
print "responce code: %d\n" % r.status_code
print r.text
