#This deals with the creation or editing of menus
import os, collections
import typer, menus, decks, cards, voice, colors, create_cards

screen = []
menu_list = {}

#self.default_back = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': (0, 0, 0), 'cards_repeat': True, 'different_consecutive_cards': 1, 'random': False}


def run(actions, deck):
	"""Call this function with the argument of a deck object in order to have it listed for edit"""
	deck = first_run(deck)
	if screen[0] == "main_menu":
		s = menu_list["main_menu"].run(key=actions['key'], mouse_clicked=actions['mouseClicked'], mouse_position=(actions['mousex'], actions['mousey']))
	elif "Title" in screen[0]:
		s = titler(actions, deck)
	elif screen[0] == "Global Deck Options":
		s = options_run(actions, deck)

	elif screen[0] == "Add New Card":
		s = create_cards.run(actions, deck)
		if s and s != "main_menu":
			pass

	elif "exit" in screen[0]:
		screen[0] = "main_menu"
		return ("choose_deck", deck)

	if s:screen[0] = s
	return ("create_deck", deck)

def first_run(deck):
	"""Creates decks and checks if there is a deck or not."""
	if not deck:
		deck = decks.Deck()
	if "main_menu" not in menu_list:
		menu_list.update({"main_menu": menus.Menu(options=["Title:  %s" % deck.title, "Global Deck Options", "Save Deck", "Add New Card"])})
		screen.append("main_menu")
	return deck

def titler(actions, deck):
	"""Creates and modifies the deck.title elament"""
	s = texter(actions, "title", default_text=deck.title, title="Title:  ")
	if s:
		deck.title = s
		menu_list['main_menu'].options[0] = "Title:  %s" % deck.title
		s = "main_menu"
	return s

def yesNo(choice, options=["Yes", "No"], result_list=[]):
	"""You pass a list and this will loop through the options and return the next one from the choice. if you pass results it will return both in a tuple."""
	o = options.index(choice)
	o += 1
	if o > len(options) - 1:
		o = 0
	if result_list:
		return (options[o], result_list[o])
	else:
		return options[o]

def ttn(b):
	"""Will change True and False into Yes and No respectivly"""
	if b:
		return "Yes"
	else:
		return "No"

def texter(actions, name, title="", default_text="", character_sets=[]):
	"""You pass the name of the thing you wish to have text for and it is either added to the menu_list or ran"""
	if menu_list.get(name):
		t = menu_list[name].run(actions)
	else:
		if character_sets:
			menu_list.update({name: typer.Typer(title=title, current_string=default_text, valid_characters=character_sets)})
		else:
			menu_list.update({name: typer.Typer(title=title, current_string=default_text)})
		t = None
	return t

def options_run(actions, deck):
	"""Creates and runs the menu for the Global Deck Options"""
	if len(screen) >= 2:
		options_sub_run(actions, deck)
	elif "global_deck_options" not in menu_list:
		menu_list.update({"global_deck_options": menus.Menu(options=["Random:  %s" % ttn(deck.default_back['random']), "Cards Repeat:  %s" % ttn(deck.default_back['cards_repeat']), "There is %s cards before a card repeats" % deck.default_back['different_consecutive_cards'], "Default Front", "Default Back"], title="Global Deck Options", persistent=2, center=False, top_left_corner=(50, 50))})
	else:
		s = menu_list["global_deck_options"].run(key=actions['key'], mouse_clicked=actions['mouseClicked'], mouse_position=(actions['mousex'], actions['mousey']))
		if s:screen.append(s)

def options_sub_run(actions, deck):
	"""goes through the global_deck_options and changes them"""
	if screen[1] == "exit":
		screen[0] = "main_menu"
	elif "Random" in screen[1]:
		deck.default_back['random'] = yesNo(deck.default_back['random'], [True, False])
		menu_list["global_deck_options"].options[0] = "Random:  %s" % ttn(deck.default_back['random'])
	elif "Cards Repeat:" in screen[1]:
		deck.default_back['cards_repeat'] = yesNo(deck.default_back['cards_repeat'], [True, False])
		menu_list["global_deck_options"].options[1] = "Cards Repeat:  %s" % ttn(deck.default_back['cards_repeat'])
	elif "a card repeats" in screen[1]:
		s = texter(actions, "different_consecutive_cards", title="Cards before repeating:  ", default_text=str(deck.default_back['different_consecutive_cards']), character_sets=['numbers'])
		if s:
			deck.default_back['different_consecutive_cards'] = s
			menu_list["global_deck_options"].options[2] = "There is %s cards before a card repeats" % deck.default_back['different_consecutive_cards']
		else:
			return 0
	elif screen[1] == "Default Front":
		s = default_side(actions, deck.default_front, "Default Front")
		if s:pass
		else:return 0
	elif screen[1] == "Default Back":
		s = default_side(actions, deck.default_back, "Default Back")
		if s:pass
		else:return 0
	screen.pop()

def default_side(actions, side, name):
	"""Will list the side's default options"""
	if len(screen) >= 3:
		deck_default_runner(actions, side, name)
	elif not name in menu_list:
		menu_list.update({name: menus.Menu(options=['Voice', 'Font', 'Background'], title=name)})
	else:
		s = menu_list[name].run(key=actions['key'], mouse_clicked=actions['mouseClicked'], mouse_position=(actions['mousex'], actions['mousey']))
		if s:screen.append(s)

def deck_default_runner(actions, side, name):
	"""runs the side and changes settings"""
	if len(screen) >= 4:
		fonter(actions, side)
	elif "Voice" in screen[2]:
		if not side.get('voice'):side['voice'] = voice.Voice()
		else:
			s = side['voice'].choose_voice(actions)
			if s == "done":
				menu_list[name].options[0] = "Voice: %s %s %s" % (side['voice'].language, side['voice'].gender, side['voice'].name)
			elif s == "exit2":
				menu_list[name].options[0] = "Voice"
			if s:
				screen.pop()
	elif screen[2] == "Font":
		menus.add_menu(actions=actions, dict=menu_list, result_list=screen, name="choose_font", title="Font Settings", options=['Size: %s' % side['font']['size'], 'Color', 'Font File'])
	elif "Background" in screen[2]:
		if not menu_list.get("color_list"):
			z = {}
			z.update(colors.colors_list1)
			[z.update({i: {'default_font': {'font_color': z[i]}, 'highlighted_font': {'font_color': z[i]}}}) for i in z]
			menu_list['color_list'] = collections.OrderedDict(sorted(z.items()))
		s = menus.add_menu(options=menu_list['color_list'], persistent=2, actions=actions, dict=menu_list, name="background_menu", title="Pick a background color")
		if s:
			if s != "exit":
				side['font_background'] = s
				side['background'] = s
				menu_list[name].options[2] = "Background: %s" % s
			screen.pop()
	elif screen[2] == "exit":
		screen.pop(2)
		screen[1] = "global_deck_options"

def fonter(actions, side):
	"""Controlls the font adding for each deck"""
	if "Size:" in screen[3]:
		f = texter(actions, name="font_size", title="Size of font out of 150:  ", default_text=str(side['font']['size']), character_sets=['numbers'])
		if f and f != "exit" and int(f) <= 150:
			menu_list["choose_font"].options[0] = 'Size: %s' % f
			side['font']['size'] = f
			screen.pop()
	elif "Color" in screen[3]:
		if not menu_list.get("color_list"):
			z = {}
			z.update(colors.colors_list1)
			[z.update({i: {'default_font': {'font_color': z[i]}, 'highlighted_font': {'font_color': z[i]}}}) for i in z]
			menu_list['color_list'] = collections.OrderedDict(sorted(z.items()))
		s = menus.add_menu(options=menu_list['color_list'], persistent=2, actions=actions, dict=menu_list, name="color_menu", title="Pick a font color")
		if s:
			if s != "exit":
				menu_list["choose_font"].options[1] = 'Color: %s' % s
				side['font']['font_color'] = s
			screen.pop()
	elif "Font" in screen[3]:
		s = menus.add_menu(options=[f for f in os.listdir(".") if ".ttf" in f], title="Choose a Font file", persistent=2, actions=actions, dict=menu_list, name="font_file")
		if s:
			if s != "exit":
				side['font']['font'] = s
			screen.pop()
