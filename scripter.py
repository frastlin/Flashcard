#This is for the processing of the scripting language.
#A file for the processing of scripts
import os
import decks
from io import open as op

card_list = []
current_deck = None

def run():
	"""Runs the processing of decks from the scripted txt files"""
	d = "my_decks/"
	file_list = os.listdir(d)
	file_list = [d + f for f in file_list if f.endswith(".txt")]
#	file_list = [open(f).read() for f in file_list]
#	[translate(f.split("\n")) for f in file_list]
	for f in file_list:
		with open(f, encoding='latin-1') as file_text:
			translate(file_text.read())

def translate(file):
	"""will translate the script into python code"""
	todo = ""
	contents = ""
	file = file.split("\n")
	for l in file:
		if ":" in l:
			l = l.split(":", 1)
			l_word = l[0].lower().strip()
			if l_word in ['title', 'text', 'media']:
				todo += l_word
			else:
				contents += l[0] + ":"
			contents += l[1] + "\n"
		elif l:
			contents += l + "\n"
	print(todo)
	print(contents)

class Card(object):
	"""Is the template we fill to add a card."""
	def __init__(self):
		self.front_text = ""
		self.back_text = ""
		self.front_media = ""
		self.back_media = ""

def add_deck(card_list):
	"""Will add a card to the deck using the add_card function"""
	[current_deck.add_card(front_text=c.front_text, back_text=c.back_text, front_media=c.front_media, back_media=c.back_media) for c in card_list]

def title(text):
	global current_card
	current_card = Card()
	


function_dict = {
'title': title,
}

#run()