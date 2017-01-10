#coding: utf-8
"""create speech example. It uses several requests using both get and post. There is an example of generating a direct url as well."""

from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_GET, METHOD_POST, RES_HEADER_TTS_REQUEST_CHARACTERS, RES_HEADER_TTS_REQUEST_ID, RES_HEADER_REQUEST_ID
from ivonaspeechcloud.inputs import Voice, OutputFormat
from credentials import access_key, secret_key

language_de = "de-DE"
language_en = "en-GB"
language_pl = "pl-PL"

german_text = "Ich bin gã¼cklich."
english_text = "I am happy"
polish_text = "Jestem szczä™›liwy."

file_path_post_de = "tmp/speech_post_de.mp3"
file_path_post_en = "tmp/speech_post_en.mp3"
file_path_get_pl = "tmp/speech_get_pl.ogg"

def sample_create_speech():
	client = SpeechCloudClient(access_key, secret_key)

	#get request with language_filtering (pl):
	res = client.create_speech(polish_text, output_format=OutputFormat(codec="OGG", sample_rate="22050"), voice=Voice(language=language_pl), method=METHOD_GET)
	with open(file_path_get_pl, "wb") as f:
		a = ""
		for chunk in res.chunks:
			a += chunk
		f.write(a)

	#post request with language filtering (de):
	res = client.create_speech(german_text, voice=Voice(language=language_de), method=METHOD_POST)
	#method get direct url to the speech
	print("rec_url", client.create_speech_url(german_text, voice=Voice(language=language_de)))
	with open(file_path_post_de, "wb") as f:
		for chunk in res.chunks:
			f.write(chunk)

	#post request with language filtering (en):
	res = client.create_speech(english_text, voice=Voice(language=language_en), method=METHOD_POST)
	with open(file_path_post_en, 'wb') as f:
		for chunk in res.chunks:
			f.write(chunk)

	print("response info for the last request:")
	print("\tCharacters used: " + res.headers[RES_HEADER_TTS_REQUEST_CHARACTERS])
	print("\tTTS request id: " + res.headers[RES_HEADER_TTS_REQUEST_ID])
	print("\tRequest id: " + res.headers[RES_HEADER_REQUEST_ID])

if __name__ == '__main__':
	sample_create_speech()
#	except:
#		print("You need to be connected to the internet")