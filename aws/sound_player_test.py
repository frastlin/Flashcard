#coding: utf-8
#Is a sound player
#Our imports, from mostly the ivona python API
import pygame, time
from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_POST
from ivonaspeechcloud.inputs import Voice, OutputFormat
from credentials import access_key, secret_key

#Our constants, for Ivona:
language = "en-GB"
text = "I am very happy"
file = "tmp/test1.ogg"

#Starting pygame
pygame.mixer.pre_init(22050,-16, 2, 400)
pygame.mixer.init()

#Our function for creating speech
def speech():
	"""Will produce a file with the selected text from above and in the voice above"""
	client = SpeechCloudClient(access_key, secret_key)
	res = client.create_speech(text, output_format=OutputFormat(codec="OGG"), voice=Voice(language=language), method=METHOD_POST)
	with open(file, 'wb') as f:
		[f.write(chunk) for chunk in res.chunks]

if __name__ == '__main__':
	speech()

	pygame.mixer.music.load(file)
	pygame.mixer.music.play()

#	s = pygame.mixer.Sound(file)
#	s.play()

	time.sleep(3)
