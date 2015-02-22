#This is the engine for the flashcards
import pygame, random, sys
from pygame.locals import *
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
	displaySurface = pygame.display.set_mode((windowwidth, windowheight)) #, pygame.FULLSCREEN)
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
			elif actions['key'] == "s" and 'shift' in actions['mods'] and 'ctrl' in actions['mods']:
				import speech
				if speech.speechOn:
					speech.speechOn = False
				else:
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
64: ['ctrl'],
320: ['ctrl'],
1: ['shift'],
257: ['shift'],
65: ['ctrl', 'shift'],
256: ['alt'],
257: ['alt', 'shift'],
321: ['ctrl', 'alt', 'shift']
}



if __name__ == '__main__':
	main()