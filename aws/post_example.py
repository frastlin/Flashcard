#aws 4 signing example
#dynamoDB API (CreateTable)
# see: http://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
#this version makes a POST request and passes request parameters
# in the body (payload) of the request.
#an Authorization header.
import sys, os, base64, datetime, hashlib, hmac
import requests #pip install requests


#***request values***
method = 'POST'
service = 'dynamodb'
host = 'dynamodb.us-west-2.amazonaws.com'
region = 'us-west-2'
endpoint = 'https://dynamodb.us-west-2.amazonaws.com/'

#POST requests use a content type header.
#for dynamoDB, the content is JSON.
content_type = 'application/x-amz-json-1.0'
#dynamoDB requires an x-amz-target that has this format:
#DynamoDB_<API version>.<operationName>
amz_target = 'DynamoDB_20120810.CreateTable'

#request parameters for CreateTable--passed in a JSON block.
request_parameters = '{'
request_parameters += '"KeySchema": [{"KeyType": "HASH", "AttributeName": "Id"}],'
request_parameters += '"TableName": "TestTable", "AttributeDefinitions": [{"AttributeName": "Id", "AttributeType": "S"}],'
request_parameters += '"ProvisionedThroughput": {"WriteCapacityUnits": 5, "ReadCapacityUnits": 5}'
request_parameters += '}'

#key derivation functions. See:
# http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python

def sign(key, msg):
	return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, date_stamp, regionName, serviceName):
	kDate = sign(('AWS4' + key).encode('utf-8'), date_stamp)
	kRegion = sign(kDate, regionName)
	kService = sign(kRegion, serviceName)
	kSigning = sign(kService, 'aws4_request')
	return kSigning

#read AWS access key from env. variables or configuration file.
#best practice is not to embed credentials in code.
#access_key = os.environ.get('AWS_ACCESS_KEY_ID')
#secret_key = os.environ.get('AWS_ACCESS_KEY_ID')

if access_key is None or secret_key is None:
	print 'no access key is available.'
	sys.exit()

#create a date for headers and the credential string
t = datetime.datetime.utcnow()
amz_date = t.strftime('%Y%m%dT%H%M%SZ')
date_stamp = t.strftime('%Y%m%d') # date w/o time, used in credential scope


#***task 1: creat a canonical task***
# http://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html

# step 1 is to define the verb, (POST GET).-- already done.

# step 2: create canonical uri--the part of the uri from domain to query
#string (use '/' if no path)
canonical_uri = '/'

#step 3: create the canonical query string. in this example, request
# parameters are passed in the body of the request and the query string is blank.
canonical_querystring = ''

#step 4: create the canonical headers.
#must be trimmed and lower-case and sorted in ASCII order.
# note that there is a trailing '\n'.
canonical_headers = 'content-type:' + content_type + '\n' + 'host:' + host + '\n' + 'x-amz-date:' + amz_date + '\n' + 'x-amz-target:' + amz_target + '\n'

#step 5: create the list of signed headers. This lists the headers
#in the canonical_headers list, delimited with ";" and in alpha order.
# note: the request can include any headers; canonical_headers and signed_headers
#include those that you want to be included in the hash of the request.
#"Host" and "x-amz-date" are always required.
#for DynamoDB, content-type and x-amz-target are also required.
signed_headers = 'content-type;host;x-amz-date;x-amz-target'

#step 6: create payload hash. In this example, the payload (body of the request)
# contains the request parameters.
payload_hash = hashlib.sha256(request_parameters).hexdigest()

#step 7: combine elements to create create canonical request
canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

#***task 2: create the string to sign***
#match the algorithm to the hashing algorithm you use, either SHA-1 or SHA-256 (recommended)
algorithm = 'AWS4-HMAC-SHA256'
credential_scope = date_stamp + '/' + region + '/' + service + '/' + 'aws4_request'
string_to_sign = algorithm + '\n' + amz_date + '\n' + credential_scope + '\n' + hashlib.sha256(canonical_request).hexdigest()

#***task 3: calculate the signiture***
#create the signing key using the function defined above.
signing_key = getSignatureKey(secret_key, date_stamp, region, service)

# sign the string_to_sign using the signing_key.
signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

#***task 4: add signing information to the request***
#put the signiture information in a header named authorization.
authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature


#for DynamoDB, the request can include any headers, but must include "host", "x-amz-date",
# "x-amz-target", "content-type" and "Authorization". Except for the Authorization, header,
#The headers must be included in the canonical_headers and signed_headers values, as noted earlier.
#order here is not significant.
#python note: the 'host' header is added automatically by the python 'requests' library.
headers = {'Content-Type': content_type, 'X-Amz-Date': amz_date, 'X-Amz-Target': amz_target, 'Authorization': authorization_header}

#***Send the request***
print 'begin request+++'
print 'request url = ' + endpoint

r = requests.post(endpoint, data=request_parameters, headers=headers)

print 'responce+++'
print 'response code: %d' % r.status_code
print r.text
