import sys, os, base64, datetime, hashlib, hmac
import requests

method = 'POST'
service = '/CreateSpeech'
host = 'tts.eu-west-1.ivonacloud.com'
region = 'us-east-1'
endpoint = 'https://tts.eu-west-1.ivonacloud.com/'


#x-amz-date
t = datetime.datetime.utcnow()
amz_date = t.strftime('%Y%m%dT%H%M%SZ')
date_stamp = t.strftime('%Y%m%d')

#Authorisation:
algorithm = 'AWS4-HMAC-SHA256'
#put access_key here
credential_scope = date_stamp + '/' + region + '/' + service + '/' + 'aws4_request'


authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature


request_parameters = {
	"Input": {
		"Data": "Hello to the world",
		"Type": "text/plain"
	},

	"OutputFormat": {
		"Codec": "MP3",
		"SampleRate": "22050",
	},

	"Parameters": {
		"Rate": "medium",
		"Volume": "medium",
		"SentenceBreak": 400,
		"ParagraphBreak": 650,
	},

	"Voice": {
		"Name": "Salli",
		"Language": "en-US",
		"Gender": "Female",
	}
}



print 'begin request+++'
print 'request url = ' + endpoint

r = requests.post(endpoint, data=request_parameters, headers=headers)

print 'responce+++'
print 'response code: %d' % r.status_code
print r.text
