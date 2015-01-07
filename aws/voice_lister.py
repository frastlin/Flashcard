#coding: utf-8
from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_POST
from ivonaspeechcloud.inputs import Voice
from credentials import access_key, secret_key

def list_voices(language=None):
	"""Will return a dict of voices based off the language"""
	client = SpeechCloudClient(access_key, secret_key)

	res = client.list_voices(method=METHOD_POST)
	return res.json

s = str(list_voices())
f = open("output.txt", "w")
f.write(s)
f.close()