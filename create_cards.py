#A module that is very close to the create_decks.py but this is for spacific cards.
import os, collections
import typer, menus, cards, voice, colors

screen = ["main_menu"]
menu_list = {}
sides = {"front": {"text": "Sample front text", "settings": {}, "media": ""}, "back": {"text": "Sample back text", "settings": {}, "media": ""}}

#self.default_back = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': (0, 0, 0), 'cards_repeat': True, 'different_consecutive_cards': 1, 'random': False}

def run(actions, deck):
	"""Call this function with the argument of a deck object in order to have it listed for edit"""
	if screen[0] == "main_menu":
		s = menus.add_menu(actions, options=["Front", "Back", "Reset", "Save Card"], title="Side Selection", dict=menu_list, name="main_menu")
		if s:
			if s == "exit":
				return "main_menu"
			screen[0] = s

	elif screen[0] == "Front":
		s = default_side(actions, sides['front'], "front")

	elif screen[0] == "Back":
		pass

	elif screen[0] == "Reset":
		pass

	elif screen[0] == "Save Card":
		pass

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

# *~*
def default_side(actions, side, name):
	"""Will list the side's default options"""
	if len(screen) >= 3:
		deck_default_runner(actions, side, name)
	elif not name in menu_list:
		menu_list.update({name: menus.Menu(options=['text: %s' % side['text'], 'Voice', 'Font', 'Background', 'Advanced'], title=name)})
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
			print(s)
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
