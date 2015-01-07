#This is the screen that comes up when people first start the program
import menus
from speech import speak as spk

main_menu = menus.Menu(options=["begin", "exit"], title="Main Menu", loops=False)
settings = ['Speech:  on',]
settings_menu = menus.Menu(options=settings)

current_screen = "start"

def main(actions):
	global current_screen
	if current_screen == "start":
		r = main_menu.run(key=actions['key'], mouse_position=(actions['mousex'], actions['mousey']), mouse_clicked=actions['mouseClicked'])
		if r:current_screen = r
	elif current_screen == "exit":
		spk("Exeting!")
		return "exit"
	elif current_screen == "begin":
		current_screen = "start"
		return "choose_deck"
	elif current_screen == "settings":
		r = settings_menu.run(key=actions['key'], mouse_position=(actions['mousex'], actions['mousey']), mouse_clicked=actions['mouseClicked'])
		if r:
			r = settings_mod(r)
			current_screen = "settings"
			return r

	return "start"

def settings_mod(r):
	"""This is for the modification of settings"""
	if "Speech:" in r:
		settings[0] = yesNo(r, 'Speech:  on', 'Speech:  off')
		r = "settings"
		import speech
		if "off" in settings[0]:
			speech.speechOn = False
		else:
			speech.speechOn = True
	elif r == "exit":
		r = "start"
	return r

def yesNo(choice, option1, option2):
	"""Will check what option choice is and swap it, so that if it is yes, it will return no and if it is no, it will return yes."""
	if choice == option1:
		return option2
	else:
		return option1
