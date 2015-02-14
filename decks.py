#This is our basic setup for decks
import random, cards, display
from speech import speak as spk
from text import text_wrap as txt
from pygame import mixer
mixer.pre_init(22050,-16, 2, 400)
mixer.init()

class Deck(object):
	default_settings = {'voice': None, 'font': {'size': 40, 'color': 'white', 'font': 'freesansbold.ttf'}, 'background': 'black', 'cards_repeat': True}

	def __init__(self, title="Default title"):
		"""The default options for a deck:
			title: name your deck!
			The below elaments are the default settings for the front and back of the deck. You can change each card's personal settings, but this is the default. If you change settings of the default, it will change all cards in the deck unless they have individual settings.
			Here are the items in the default dicts:

			voice: select a voice from one of the many ivona text to speech voices to be used on the front of the card. None will use nothing.
			font:will set this for all font if they are not changed. There are 3 options:
				'size' size of the font (titles and options will be 50% bigger and smaller respectivly to a point), 'color' is the color (either chosen from the colors module or give a rgb number), 'type' is a ttf file that is either default in pygame or part of the directory.
			background: color or picture of the background for the front
			cards_repeat: will a card be put back into the deck after being played or removed? True for put back in and False for removed.
			default_options_front: if you wish to have options like 'yes' and 'no' you can set them here.
			different_consecutive_cards: If cards are repeating, this will wait the number of cards before repeating the first card. *Note, if it is higher than the number of cards in the list, it will revert to 0.
			random: If you wish just to go through your cards in a row, put this as False, otherwise have a random choice.
		"""
		#Here are our default sides
		self.title = title
		self.default_front = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': 'black'}
		self.default_back = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': (0, 0, 0), 'cards_repeat': True, 'different_consecutive_cards': 1, 'random': False}

		#Our operation variables
		self.card_list = []
		self.card_history = []
		self.temp_card_list = []
		self.current_side = None
		self.current_card = None
		self.run_cards = []
		self.text = None
		self.media = None
		self.voice = None
		self.sides = (0, 1)
		self.current_character = 0
		self.current_word = 0

	def run(self, actions):
		"""Will check for keyboard input and run the side_run function"""
		key = actions['key']
		mouseClicked = actions['mouseClicked']
		mods = actions['mods']
		if key in ("escape", "backspace"):
			self.current_side = None
			display.change_background((0, 0, 0))
			return "choose_deck"
		elif key in ("return", "space") or mouseClicked or self.current_side == None:
			text = self.run_side()
			self.text = text
			if not self.voice:
				spk(text)
		elif key in ('up', 'down') and self.text:
			spk(self.text)
		elif key in ['left', 'right'] and not mods:
			text = self.text
			self.current_character = self.scroll(key, self.current_character, text)
			spk(text[self.current_character])
		elif key in ['left', 'right'] and mods:
			text = self.text.split(' ')
			self.current_word = self.scroll(key, self.current_word, text)
			self.current_character = self.text.index(text[self.current_word])
			spk(text[self.current_word])
		elif key in ['r', 'p']:
			if self.media:
				self.media.play()
			elif self.voice:
				mixer.music.stop()
				mixer.music.play()

			else:
				spk(self.text)



		return "cards"

	def run_side(self):
		"""This will run a card, just repeat it for the whole deck"""
		self.voice = None
		self.media = None
		self.current_character = 0
		self.current_word = 0
		side, settings = self.set_side()
		if side.media:
			side.media.play()
			self.media = side.media
		if settings.get('voice') and side.text:
			self.voice = settings['voice'].speak(side.text, path=self.title)
		if side.text:
			self.displayer(side.text, settings)
		return side.text

	def set_side(self):
		"""This will look at what the current side is, choose the correct card from the list, check what that card's settings are going to be, then returns both the card and the settings in a tuple"""
		settings = {}
		if self.current_side == 'back':
			side = self.current_card[self.sides[1]]
#			settings = self.set_settings(side, self.default_back)
#			[settings.update({s: self.default_front}) for s in self.default_front if s not in settings]
			[settings.update({i: self.default_back[i]}) for i in self.default_back]
			[settings.update({i: side.settings[i]}) for i in side.settings]


			self.current_side = 'front'
			#These 3 lines are to remove the repeat cards. I wasn't sure where to put it, so just put it here because it is with the back check.
			if settings.get('cards_repeat') == False:
				self.run_cards.append(self.current_card)
				self.card_list.remove(self.current_card)
			self.deck_check(settings)
		else: #elif self.current_side == 'front':
			if not self.current_card:
				self.current_card = random.choice(self.card_list)
			side = self.current_card[self.sides[0]]
#			settings = self.set_settings(side, self.default_front)
#			[settings.update({s: self.default_front}) for s in self.default_front if s not in settings]
			[settings.update({i: self.default_front[i]}) for i in self.default_front]
			[settings.update({i: side.settings[i]}) for i in side.settings]

			self.current_side = 'back'
		return (side, settings)

	def deck_check(self, settings):
		"""This function returns a random card."""
		l = self.card_list
		card = self.random_check(settings, l)
		self.current_card = card

	def random_check(self, settings, l):
		"""This function returns the card, it checks if the card is random or not. if it is random, it calls a function to check if there are consecutive cards. if not, it changes temp_card_list to a number and adds a number each time till it reaches len(l)-1 and resets."""
		if settings['random']:
			self.consec_cards(settings['different_consecutive_cards'], l)
			random.shuffle(l)
			return l[0]
		else:
			#This section changes the temp_card_list to a number and uses it instead of creating a new fresh variable. Then every iteration it adds +1 to the variable before resetting it when it reaches the max.
			templ = self.temp_card_list
			if templ == []:
				templ = 0
			elif templ == len(l) - 1:
				templ = -1
			templ += 1
			self.temp_card_list = templ
			return l[templ]

	def consec_cards(self, consec, l):
		"""Appends already run cards to a temp card list and removes cards if the temp list gets too long"""
		if consec and consec < len(l) or self.temp_card_list:
			card = self.current_card
			templ = self.temp_card_list
			l.remove(card)
			templ.append(card)
			#This if statement checks the templ to see if it is longer than the consecutive number. if so, it adds the last item back into the card_list
			if len(templ) > consec:
				l.append(templ.pop(0))

	def set_settings(self, side, side_default):
		"""Checks the card to see if there are any local settings and if there are, uses them rather than the ones in default while using default for all settings that are not changed in local settings. The list comprehension at the bottom will add a dict entry from the default settings to the temp_settings if k is not already there."""
		temp_settings = side.settings
		if temp_settings == {}:
			temp_settings = side_default
		else:
			[temp_settings.update({k: side_default[k]}) for k in side_default if k not in temp_settings]
		return temp_settings

	def add_card(self, front_text=None, back_text=None, front_media=None, back_media=None, front_options=None, back_answers=None, front_settings={}, back_settings={}):
		"""This is the function that you call when you wish to add a card."""
		#Strange thing: if I have "front_voice" as an argument and convert a dict to a voice object in front_settings, all cards will get the voice object in their settings, not just one card.
		#These two lines convert the text pieces to unicode latin-1 characters so that stuff like axcented characters will be read by accessible_output
		if front_text:front_text = unicode(front_text, "latin-1", "ignore")
		if back_text:back_text = unicode(back_text, "latin-1", "ignore")
		if front_media:front_media = self.media_process(front_media)
		if back_media:back_media = self.media_process(back_media)
		side1 = cards.Side(text=front_text, media=front_media, settings=front_settings, options=front_options)
		side2 = cards.Side(text=back_text, media=back_media, settings=back_settings, options=back_answers)
		self.card_list.append((side1, side2))

	def media_process(self, media):
		"""Returns a media object"""
		m = mixer.Sound(media)
		return m

	def displayer(self, text, settings):
		"""The function that is in charge of rendering graphics for each card"""
		font_location = settings['font_location']
		font = settings['font']
		display.change_background(settings['background'])
		txt(text=text, settings=font, center=font_location['center'], xpos=font_location['xpos'], ypos=font_location['ypos'])

	def reverse(self):
		"""Will reverse the cards so the back will be first and the front will be last"""
		self.sides = (1, 0)

	def scroll(self, key, num, l):
		"""Will do a basic scrolling check to make sure the list is not being over-shot"""
		if key == 'right':
			num += 1
		elif key == 'left':
			num -= 1
		if num > len(l) - 1:
			return num - 1
		elif num < 0:
			return num + 1
		else:
			return num

if __name__ == '__main__':
	deck1 = Deck("deck1")
	c = deck1.add_card
	c("I like being the front", "I like being the back", front_settings={'voice': {"Language": "en-US", "Name": "Salli"}})
	c("I don't like being the front", "I don't like being the back")
	c("Being the front is OK", "Being the back is ok")
	c("I like being the only text ever!")

	for i in deck1.card_list:
		if i[0].settings.get('voice'):
			print(i[0].settings['voice'])
			print(i[0].text)
