#This module has all the functions dealing with the management of decks
import menus, filer, scripter

deck_list = filer.run()
deck_list += scripter.run()

if not deck_list:
	import my_cards
	deck_list += my_cards.deck_list

deck_titles = [n.title for n in deck_list]
#deck_titles += ['Edit Deck', 'Create New Deck']

deck_menu = menus.Menu(deck_titles, title="Deck Menu")
editing = [False,]

def choose_deck(actions):
	"""This is the main and only function that is directly called for this module"""
	choice = deck_menu.run(key=actions['key'], mouse_clicked=actions['mouseClicked'], mouse_position=(actions['mousex'], actions['mousey']))
	if choice and choice not in ["exit", "Create New Deck", "Edit Deck"]:
		d = [de for de in deck_list if de.title == choice]
		if not editing[0]:
			return ("cards", d[0])
		else:
			refresh()
			return ("edit_deck", d[0])
	elif choice == "exit":
		if editing[0]:
			refresh()
			return ("choose_deck", None)
		else:
			return ("start", None)
	elif choice == "Create New Deck":
		return ("create_deck", None)
	elif choice == "Edit Deck":
		editing[0] = True
		deck_menu.options = deck_menu.options[:-2]
		deck_menu.title = "Choose a deck to edit"
		return ("choose_deck", None)
	else:
		return ("choose_deck", None)

def refresh():
	"""Refreshes deck_menu"""
	deck_menu.options = deck_titles
	deck_menu.title = "Deck Menu"
	editing[0] = False


