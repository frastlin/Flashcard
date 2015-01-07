#This is for the processing of the scripting language.
#A file for the processing of scripts
import os

def run():
	"""Runs the processing of decks from the scripted txt files"""
	d = "my_decks/"
	file_list = os.listdir(d)
	file_list = [d + f for f in file_list if f.endswith(".txt")]
	file_list = [open(f).read() for f in file_list]
	[translate(f.split("\n")) for f in file_list]

def translate(file):
	"""will translate the script into python code"""
	todo = ""
	for l in file:
		if ":" in l:
			l_list = l.split(":")
			l_word = l_list[0].lower().strip()
		if l_word in ['name', 'text', 'media', 'voice']:
			todo = l_word
	print todo






run()