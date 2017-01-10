#A module to handle creating of files and importing of decks
import os
from importlib import import_module
import file_contents

def run():
	"""Run this function to get the creation and or import of all decks from 'decks_in_python'. Note that folder names should have a / after them."""
	d1 = "my_decks/"
	d2 = "decks_in_python/"
	d3 = "voice_files/tmp/"
	d4 = "sounds/"
	if not os.path.exists(d1):
		os.makedirs(d1)
	if not os.path.exists(d2):
		os.makedirs(d2)
	if not os.path.exists(d3):
		os.makedirs(d3)
	if not os.path.exists(d4):
		os.makedirs(d4)

	file_list = os.listdir(d1)
	if not file_list:
		file_maker(d1, 'My Decks.txt', file_contents.example_deck)
		file_maker(d1, 'How to Make Decks.html', file_contents.readme_script)


	file_list = os.listdir(d2)
	if not file_list:
		file_maker(d2, 'my_cards.txt', file_contents.my_cards)
		file_maker(d2, 'readme.html', file_contents.readme_python)
		file_list = os.listdir(d2)
	return file_importer(file_list, d2)

def file_importer(l, d):
	"""Will go through all the python files and import the deck_lists"""
	decks = []
	for file in l:
		if file.endswith('.py'):
			file = "%s%s" % (d, file)
			decks += importer(file)
	return decks

def importer(file):
	"""Will exec the contents of each file and return the contents of deck_list"""
	f = open(file).read()
	exec f
	try:
		if isinstance(deck_list, (tuple, list, set)):
			return deck_list
	except:
		return []



#not used
def importer_not_used(file):
	"""A function without error messages that will import all modules in the selected dir and return their decks list"""
	try:
		path_name = "decks_in_python." + file.split('.')[0]
		mod = import_module(path_name)
		decks = mod.deck_list
	except:
		return []
	if isinstance(decks, (list, tuple, set)):
		return decks
	else:
		return []

#not used
def importer_with_error_messages(file):
	"""trys to import decks and append them to a list, if not it will return an error detailing what went wrong"""
#	try:
	mod = import_module(file.split('.')[0])
#	except:
#		print "%s can not have a space in its name" % file
#		return []
	try:
		l = mod.deck_list
	except:
		print "%s is missing a deck_list list. please place the line:\ndeck_list = [deckname] at the bottom of your file" % file
		return []
	if isinstance(l, (list, tuple, set)):
		return l
	else:
		print "%s is not a list, please make it a list" % filename
		return []

#not used
def copyer2(d):
	"""This is a less cluttered form of copyer below but slightly slower. to run this you need to import: from shutal import copy2"""
	name = "my_cards.py"
	d += name
	copy2(name, d)

#not used because we are using exec
def init_creator(dir_list):
	"""will create an __init__.py file each place in the list"""
	for i in dir_list:
		if i[len(i)-1] != '/':
			i += '/'
		i += "__init__.py"
		f = open(i, 'wb')
		f.close()

def file_maker(d, new_filename, text):
	"""Will take the contents from file_contents and put it into a file with the text."""
	d += new_filename
	new_file = open(d, 'wb')
	new_file.write(text)
	new_file.close()




#Not used
def copyer(d, filename):
	"""copies files"""
	file = open(filename, 'rb')
	d += filename
	file2 = open(d, 'wb')
	file2.write(file.read())
	file.close()
	file2.close()

if __name__ == '__main__':
	import time
#	time.sleep(1)
#	t1 = time.clock()
#	l = run()
#	print time.clock() - t1

#	for d in l:
#		print d.title
#	import my_decks.decks_in_python.amy_cards
#	print my_decks.decks_in_python.amy_cards.deck_list
