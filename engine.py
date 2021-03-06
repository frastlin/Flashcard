#This is the engine for the flashcards
import pygame, random, sys
from pygame.locals import *
import speech
from speech import speak as spk
#our program spacific modules:
import display, start, decker, create_decks, logger

logger.start("Starting flashcard")

fps = 30
windowwidth = 640
windowheight = 480


def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	displaySurface = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
	pygame.display.set_caption('Flashcards')
	play = True
	current_screen = "start"

	#stuff for testing pirpuses:


	#a dict with all the commands that go on
	actions = {
		'mousex': 0,
		'mousey': 0,
		'key': None,
		'mouseClicked': False,
		'mods': []
		}

	while play:
		actions['mouseClicked'] = False
		actions['key'] = None
		actions['mods'] = []
		actions['mousey'] = 0
		actions['mousex'] = 0

		#Event handling loop
		for event in pygame.event.get():
			if event.type == MOUSEMOTION:
				actions['mousex'], actions['mousey'] = event.pos
			elif event.type == MOUSEBUTTONUP:
				actions['mousex'], actions['mousey'] = event.pos
				actions['mouseClicked'] = True
			elif event.type == KEYDOWN:
				actions['key'] = pygame.key.name(event.key)
				actions['mods'] = mod_id.get(pygame.key.get_mods(), [])

			if event.type == QUIT or current_screen == "exit" or ('alt' in actions['mods'] and actions['key'] == 'f4'):
				#The reason why we have sys.exit() here is because otherwise the display below throws an error because the video is not initalised
				pygame.quit()
				sys.exit()
			elif actions['key'] == "s" and 'ctrl' in actions['mods']:
				if speech.speechOn:
					speech.spk("Turnning off speech, press ctrl+s to turn it back on")
					speech.speechOn = False
				else:
					speech.spk("Turnning on speech, press ctrl+s to turn it off")
					speech.speechOn = True



		#These next lines are program spacific and really make our program run.
		if current_screen == "start":
			current_screen = start.main(actions)
		elif current_screen == "choose_deck":
			current_screen, current_deck = decker.choose_deck(actions)
		elif current_screen == "cards":
			current_screen = current_deck.run(actions)
		elif current_screen == "create_deck" or current_screen == "edit_deck":
			current_screen, current_deck = create_decks.run(actions, current_deck)

		rect_list = display.renderer(displaySurface)

		#Redraw the screen and wait a clock tick
		if rect_list:
			pygame.display.update(rect_list)
		display.event_queue.tick(fpsClock.tick(fps))

mod_id = {
64: ['left ctrl', 'ctrl'],
320: ['left ctrl', 'ctrl'],
1: ['left shift', 'shift'],
257: ['left shift', 'shift'],
256: ['left alt', 'alt'],
2: ['right shift', 'shift'],
128: ['right ctrl', 'ctrl'],
65: ['left ctrl', 'ctrl', 'left shift', 'shift'],
66: ['left ctrl', 'ctrl', 'right shift', 'shift'],
257: ['left alt', 'alt', 'left shift', 'shift'],
129: ['right ctrl', 'ctrl', 'left shift', 'shift'],
130: ['right ctrl', 'ctrl', 'right shift', 'shift'],
321: ['left ctrl', 'ctrl', 'left alt', 'alt', 'left shift', 'shift'],
322: ['left ctrl', 'ctrl', 'left alt', 'alt', 'right shift', 'shift'],
258: ['left alt', 'alt', 'right shift', 'shift'],
384: ['left alt', 'alt', 'right ctrl', 'ctrl'],
386: ['left alt', 'alt', 'right ctrl', 'ctrl', 'right shift', 'shift'],
}

if __name__ == '__main__':
	main()