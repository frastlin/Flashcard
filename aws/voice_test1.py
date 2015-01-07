#coding: utf-8
"""List voices example: there is an example to get German and polish voices and a direct url."""

from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_GET, METHOD_POST
from ivonaspeechcloud.inputs import Voice
from credentials import access_key, secret_key

language_de = "de-DE"
language_pl = "pl-PL"

def sample_list_voices():
	client = SpeechCloudClient(access_key, secret_key)

	res = client.list_voices(voice=Voice(language=language_pl), method=METHOD_GET)
	print(res.json)

	res = client.list_voices(voice=Voice(language=language_de), method=METHOD_POST)
	print(res.json)

	print(client.list_voices_url(voice=Voice(language=language_pl)))


if __name__ == '__main__':
	sample_list_voices()
