#coding: utf-8
#Module for dealing with Ivona voices and the speech.
import os, voice_lists, menus, pygame
from ivonaspeechcloud.client import SpeechCloudClient
from ivonaspeechcloud.const import METHOD_POST
from ivonaspeechcloud.inputs import Voice as vw
from ivonaspeechcloud.inputs import  OutputFormat
from credentials import access_key, secret_key
import pygame
music = pygame.mixer.music

class Voice:
	"""Class for setting a voice and running it"""

	def __init__(self, language=None, gender=None, name=None, current_voice={}):
		self.language = language
		self.gender = gender
		self.name = name
		self.current_voice = current_voice


		#These are our operation variables:
		self.client = SpeechCloudClient(access_key, secret_key)
		self.menu_list = {}
		self.current_screen = "language"
		self.voice_list = []

	def choose_voice(self, actions):
		"""Will choose all parameters for a voice"""
		if self.current_screen == "language":
			s = self.menu_run(actions, "language_menu", self.list_type('language'), "Choose a Language")
			if s:
				if s == "exit":return "exit"
				else:
					self.language = s
					self.current_screen = "gender"
		elif self.current_screen == "gender":
			s = self.menu_run(actions, "gender_menu", self.list_type('gender'), "Choose a Gender")
			if s:
				if s == "exit":
					self.current_screen = "language"
					self.menu_list["gender_menu"] = None
				else:
					self.gender = s
					self.current_screen = "name"
		elif self.current_screen == "name":
			s = self.menu_run(actions, "name_list", self.list_type('name'), "Choose a name from the following voices")
			if s == "exit":
				self.current_screen = "gender"
				self.menu_list["name_list"] = None
			elif s and s != "None":
				self.name = s
				self.list_type("dict")
				if actions['key'] == "space":
					self.speak(text="Hello, I am %s, an Ivona text to speech voice" % s, current_voice=self.current_voice)
					self.gender = None
					self.name = None
					self.language = None
				else:
					return "done"
			elif s == "None":
				self.name = None
				self.current_voice = {}
				return "exit2"


	def list_type(self, type):
		"""The type can either be "language", "gender", "name" or "dict" and it will return a list of each one"""
		if not self.voice_list:
			self.voice_list = self.list_voices()
		if type == "language":
			s = sorted(set(voice_lists.languages.get(v['Language'], v['Language']) for v in self.voice_list))
		elif type == "gender":
			s = set(f['Gender'] for f in self.voice_list)
		elif type == "name":
			s = self.voice_list
			if self.language and self.language != "All":
				s = [f for f in s if f['Language'] == voice_lists.languages2[self.language]]
			if self.gender and self.gender != "All":
				s = [f for f in s if f['Gender'] == self.gender]
			s = set(f['Name'] for f in s)
		elif type == "dict":
			s = self.voice_list
			if self.language and self.language != "All":
				s = [f for f in s if f['Language'] == voice_lists.languages2[self.language]]
			if self.gender and self.gender != "All":
				s = [f for f in s if f['Gender'] == self.gender]
			s = [f for f in s if f['Name'] == self.name]
			self.current_voice = s[0]
			self.language = voice_lists.languages[s[0]['Language']]
			self.gender = s[0]['Gender']
			self.name = s[0]['Name']
			return s[0]
		return list(s)

	def menu_run(self, actions, name, options, title, choice=None):
		"""Will run a menu with the name of name"""
		if self.menu_list.get(name) and name != "name_menu":
			choice = self.menu_list[name].run(key=actions['key'], mouse_clicked=actions['mouseClicked'], mouse_position=(actions['mousex'], actions['mousey']))
		else:
			if self.current_screen != "name":
				options.insert(0, "All")
				self.menu_list[name] = menus.Menu(options=options, title=title, persistent=3)
			else:
				options.insert(0, "None")
				self.menu_list[name] = menus.Menu(options=options, keys=["up", "down", ["escape", "backspace"], ["return", "space"]], title=title, persistent=3)
		return choice

	def list_voices(self):
		"""Will return a dict of voices from either the internet or the saved list"""
		try:
			res = self.client.list_voices(method=METHOD_POST)
			return res.json['Voices']
		except:
			return voice_lists.voice_dict['Voices']

	def speak(self, text="Hello World", current_voice=None, path="tmp"):
		"""pass in text if you wish it spoken and a dict that you wished passed as well as the path within the voice_files folder you wish the files to be"""
		self.run_check(path)
		if not current_voice:
			current_voice = self.current_voice
		if text.strip():
			try:
				res = self.client.create_speech(text, output_format=OutputFormat(codec="OGG"), voice=vw(language=current_voice.get('language'), gender=current_voice.get('Gender'), name=current_voice.get('Name')), method=METHOD_POST)
				path = "voice_files/%s/%s_%s_%s_%s.ogg" % (path, current_voice.get('Language'), current_voice.get('Gender'), current_voice.get('Name'), text[0:100])
				try:
					music.load(path)
				except:
					with open(path, "wb") as f:
						[f.write(chunk) for chunk in res.chunks]
					music.load(path)
				music.play()
				return path
			except:
				print("You are not connected to the internet")
				return ""
	def run_check(self, path):
		"""Checks that pygame is initialised and that the path is there"""
		path = "voice_files/%s/" % path
		if not pygame.mixer.get_init():
			pygame.mixer.pre_init(22050,-16, 2, 400)
			pygame.mixer.init()
		if not os.path.exists(path):
			os.makedirs(path)



if __name__ == '__main__':
	v = Voice()
#	print(v.voice_list)
	v.language = 'American English'
	v.gender = 'Male'
#	print(v.list_type("name"))
	v.speak()
	import time
	time.sleep(2)

#Then add the font options, including the 
