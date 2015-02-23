#This is for the processing of the scripting language.
#A file for the processing of scripts
import os, random
import decks
from voice import Voice
from io import open as op

deck_list = []
current_deck = decks.Deck(title="You for got a title")
current_card = None

def run():
	"""Runs the processing of decks from the scripted txt files"""
	d = "my_decks/"
	file_list = os.listdir(d)
	file_list = [d + f for f in file_list if f.endswith(".txt")]
	for f in file_list:
		with open(f) as file_text:
			translate(file_text.read())
		manage_decks()
	return deck_list

def manage_decks(title="You for got a title"):
	"""Will renew decks and make sure there is a fresh deck and fresh current_card. It will also append the deck if needed to the deck_list"""
	global current_deck, current_card
	if current_deck.card_list:
		deck_list.append(current_deck)
	current_deck = decks.Deck(title=title)
	current_card = None

def render_formatting(text):
	"""Will place all the lovely backslash characters in the text"""
	if " \\n " in text:
		t = text.split(" \\n ")
		text = '\n'.join(t)
	if " \\t " in text:
		t = text.split(" \\t ")
		text = "\t".join(t)
	return text

def valid_characters(text):
	"""Will remove any invalid characters for windows naming skeems and replace : with -"""
	valid_characters = "<>:\"/\\|?*"
	for i in valid_characters:
		if i == ":":
			text = text.replace(i, "-")
		else:
			text = text.replace(i, "")
	return text

def translate(file):
	"""will translate the script into python code"""
	current_function = None
	file = file.split("\n")
	for l in file:
		if ":" in l:
			l = l.split(":", 1)
			l_word = l[0].lower().strip()
			if l_word in ['title', 'text', 'media', 'voice']:
				current_function = l_word
				l = l[1]
			else:
				l = l[0] + ":" + l[1]

		if l.strip():
			if not current_function:
				current_function = "text"
				title(l)
			else:
				current_function = function_dict[current_function](l)
	TEXT("")

class Card(object):
	"""Is the template we fill to add a card."""
	def __init__(self, front_text):
		self.front_text = front_text
		self.back_text = ""
		self.front_media = ""
		self.back_media = ""
		self.front_voice = None
		self.back_voice = None
		self.front_settings = {}
		self.back_settings = {}

	def add(self):
		if self.front_text and self.back_text:
			self.front_settings['voice'] = self.front_voice
			self.back_settings['voice'] = self.back_voice
			current_deck.add_card(front_text=self.front_text, back_text=self.back_text, front_media=self.front_media, back_media=self.back_media, front_settings=self.front_settings, back_settings=self.back_settings)

def title(text):
	"""Calls the manage_decks which creates a new deck with the title of the passed text. It then returns 'text'"""
	text = valid_characters(text)
	manage_decks(text)
	return "text"

def TEXT(text):
	"""It is uppercase because I'm using text everywhere and this is the master function for text"""
	global current_card
	text = render_formatting(text)
	if current_card and current_card.front_text and current_card.back_text:
		current_card.add()
		current_card = None
	if text:
		if not current_card:
			current_card = Card(text)
		else:
			current_card.back_text = text
	return "text"

def media(text):
	"""Adds media if there is some"""
	text = text.lstrip().rstrip()
	text = text.replace("\\", "/")
	if current_card.back_text:
		current_card.back_media = text
	else:
		current_card.front_media = text
	return "text"

def voice(text):
	"""Will add the voice settings to the card"""
	v = Voice()
	text = text_into_dict(text)
	lan = text.get("language")
	gen = text.get("gender")
	name = text.get("name")
	if lan == "English":lan = "American English"
	if not lan and not name:lan = "American English"
	if lan in v.list_type("language"):
		v.language = lan
	if gen in ["Male", "Female"]:
		v.gender = gen
	name_list = v.list_type("name")
	if name in name_list:
		v.name = name
	else:
		v.name = name_list[0]
	v.make_voice()
	if current_card.back_text:
		current_card.back_voice = v
	else:
		current_card.front_voice = v
	return "text"

def text_into_dict(text):
	"""Will take a string and take out the equals and trailing spaces from it and turn it into a dict with the key in all lowercase"""
	text = text.split(",")
	text = [i.split("=") for i in text]
	text = [(i[0].lstrip().rstrip().lower(), i[1].lstrip().rstrip().title()) for i in text if len(i) == 2 and i[1]]
	return dict(text)



function_dict = {
'title': title,
'text': TEXT,
'media': media,
'voice': voice,
}


if __name__ == "__main__":
	"""
*note*
the top of decks.py needs to look like:

import random, cards, display
from speech import speak as spk
#from text import text_wrap as txt
from pygame import mixer
mixer.pre_init(22050,-16, 2, 400)
mixer.init()

#for testing and so is the numbered out import above
def txt(*args):
	print("fix deck.py and remove this function")
"""
	"""
	d = run()
	for a in d:
		print("New deck")
		print(a.title)
		for c in a.card_list:
			print(c[0].text)
			print(c[1].text)
"""

#v = voice("name=emma")
#
#print(v.current_voice)
#
#v.speak("I am an Ivona text to speech voice")
#import time
#time.sleep(3)

"""
fix letter reading
add the ability to reverse cards
Make a counter that can be reset that says how many cards have been done sense the last reset or sense the deck has began
Make it so you can use both right and left controll when arrowing through the cards

"""