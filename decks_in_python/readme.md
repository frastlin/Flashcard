<title>Read Me</title>

[script example](#script)
[code index](#index)

<p>Welcome to the deck scripts of the application.</p>

<h1>***WARNING!!!!!***</h1>
<p>DO NOT DO ANYTHING WITH THE FILES HERE UNLESS YOU KNOW PYTHON!!!</p>

<h1>Instructions for use:</h1>
first, you can put any files here, but a large number of .py files may slow down the program a little at startup as it searches through all the .py files for the line:  
deck_list = []  
Every file should have the above line with your decks inbetween the brackets [deck1, deck2, deck3, deck4]. You can have as many decks as you wish in a file. You can also create another folder inside this folder and store all your unfinished decks in it. The program will not see them.

<h1>What scripting options are there</h1>
You can create decks with:
all kinds of background colors (using rgb values), color of text, color of the background of the text...
you can add pictures to the background, you can add your own font files, you can add sounds and mp3, ogg or wav files to your programs, you can add options, key short-cuts, text to speech voices and all kinds of things to each side of the card.

<h2>The deck structure</h2>
There are global settings for each deck and then there are spacific settings for each card and then settings for each side of the card. The order of prefference is:
side,
card,
deck.
so if you set in the deck for all cards to have an orange background and you wanted card number 3 to have a green front and yellow background, you can do that.

<h1>code</h1>
Yeah yeah lets get to the good stuff!
### <a name="script">Scripts</a>

	import decks
	deck = decks.Deck

	deck1 = deck("Deck 1")
	c = deck1.add_card
	c(front_text="What is 1 + 1?", back_text="It is 2!")
	c("What is the meaning of life?", "I think you know")
	c("When is your birthday?", "It is sometime after the last one")

	deck_list = [deck1]

###What's going on?

	import decks
	deck = decks.Deck

The above two lines are importing the module decks into our script. The line below it is aliasing or assigning the name "deck" to the class inside the module decks that we imported.  

	deck1 = deck("Deck 1")
	c = deck1.add_card

Here we are making a deck named "deck1".  
In the second line we are making an alias "c" to be the deck1.add_card function.  

	c(front_text="What is 1 + 1?", back_text="It is 2!")
	c("What is the meaning of life?", "I think you know")
	c("When is your birthday?", "It is sometime after the last one")

Here we just added 3 cards.  

	deck_list = [deck1]

This final line tells the script all the decks we have in this module. Without the above line, you will have no decks imported.

#<a name="index">Scripting Index</a>
There are 3 ways of adding settings to decks:  
1. add the settings when you name your deck.
2. add them in an extra line
3. make different settings for each card.

##adding settings when you call the creation of the deck

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
			repeating: If cards are repeating, this will wait the number of cards before repeating the first card. *Note, if it is higher than the number of cards in the list, it will revert to 0.
			random: If you wish just to go through your cards in a row, put this as False, otherwise have a random choice.
		"""
		#Here are our default sides
		self.title = title
		self.default_front = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': 'black'}
		self.default_back = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': (0, 0, 0), 'cards_repeat': True, 'repeating': 1, 'random': True}
		#*note*, here is what the scripting deck_settings is, it is really a refference to the default_back.
		#'cards_repeat': True, 'repeating': 1, 'random': True

###default back settings
The default back settings are really the back settings and global settings in one. if you use the scripting language, you are used to using a shortcut to accessing the default back. The global options are

	#'cards_repeat': True, 'repeating': 1, 'random': True

`cards_repeat` is just saying if you would like the cards to come back after being played. You can change this on each card.  

repeating is saying how many cards till that card shows up in the deck again. This is because a random card is chosen when you have random selected and you don't really want to get the same card 3 times in a row.  

random is just what it sounds like, it calls a random.choice on the deck.  

##adding settings on a different line

if we wished to not have our deck be random we would have this line under the c = `deck1.add_card`  

	deck1.default_back['random'] = False

or we could also do:  

	deck1.update({'random': False})

Both are perfectly fine!

##adding settings to each card

in the `add_card` function there is a `back_settings` and `front_settings` argument.  
to change the size of the font on the back of the card you would type:

	c("What is the meaning of life?", "I think you know", back_settings={"font": {"size": 42}})

##`add_card` function

	def add_card(self, front_text=None, back_text=None, front_media=None, back_media=None, front_options=None, back_answers=None, front_settings={}, back_settings={}):

You can add text, media, settings and the other stuff has not been added yet. You don't need to fill out everything on settings, it will be put into the settings by an update when the card is called.

##Adding voices:
###dict of voices

	voice_dict = {'Voices': [
	{'Gender': 'Female', 'Language': 'en-US', 'Name': 'Salli'},
	 {'Gender': 'Male', 'Language': 'en-US', 'Name': 'Joey'},
	 {'Gender': 'Female', 'Language': 'da-DK', 'Name': 'Naja'},
	 {'Gender': 'Male', 'Language': 'da-DK', 'Name': 'Mads'},
	 {'Gender': 'Female', 'Language': 'de-DE', 'Name': 'Marlene'},
	 {'Gender': 'Male', 'Language': 'de-DE', 'Name': 'Hans'},
	 {'Gender': 'Female', 'Language': 'en-AU', 'Name': 'Nicole'},
	 {'Gender': 'Male', 'Language': 'en-AU', 'Name': 'Russell'},
	 {'Gender': 'Female', 'Language': 'en-GB', 'Name': 'Amy'},
	 {'Gender': 'Male', 'Language': 'en-GB', 'Name': 'Brian'},
	 {'Gender': 'Female', 'Language': 'en-GB', 'Name': 'Emma'},
	 {'Gender': 'Female', 'Language': 'en-GB-WLS', 'Name': 'Gwyneth'},
	 {'Gender': 'Male', 'Language': 'en-GB-WLS', 'Name': 'Geraint'},
	 {'Gender': 'Female', 'Language': 'cy-GB', 'Name': 'Gwyneth'},
	 {'Gender': 'Male', 'Language': 'cy-GB', 'Name': 'Geraint'},
	 {'Gender': 'Female', 'Language': 'en-IN', 'Name': 'Raveena'},
	 {'Gender': 'Male', 'Language': 'en-US', 'Name': 'Chipmunk'},
	 {'Gender': 'Male', 'Language': 'en-US', 'Name': 'Eric'},
	 {'Gender': 'Female', 'Language': 'en-US', 'Name': 'Ivy'},
	 {'Gender': 'Female', 'Language': 'en-US', 'Name': 'Jennifer'},
	 {'Gender': 'Male', 'Language': 'en-US', 'Name': 'Justin'},
	 {'Gender': 'Female', 'Language': 'en-US', 'Name': 'Kendra'},
	 {'Gender': 'Female', 'Language': 'en-US', 'Name': 'Kimberly'},
	 {'Gender': 'Female', 'Language': 'es-ES', 'Name': 'Conchita'},
	 {'Gender': 'Male', 'Language': 'es-ES', 'Name': 'Enrique'},
	 {'Gender': 'Female', 'Language': 'es-US', 'Name': 'Penelope'},
	 {'Gender': 'Male', 'Language': 'es-US', 'Name': 'Miguel'},
	 {'Gender': 'Female', 'Language': 'fr-CA', 'Name': 'Chantal'},
	 {'Gender': 'Female', 'Language': 'fr-FR', 'Name': 'Celine'},
	 {'Gender': 'Male', 'Language': 'fr-FR', 'Name': 'Mathieu'},
	 {'Gender': 'Female', 'Language': 'is-IS', 'Name': 'Dora'},
	 {'Gender': 'Male', 'Language': 'is-IS', 'Name': 'Karl'},
	 {'Gender': 'Female', 'Language': 'it-IT', 'Name': 'Carla'},
	 {'Gender': 'Male', 'Language': 'it-IT', 'Name': 'Giorgio'},
	 {'Gender': 'Female', 'Language': 'nb-NO', 'Name': 'Liv'},
	 {'Gender': 'Female', 'Language': 'nl-NL', 'Name': 'Lotte'},
	 {'Gender': 'Male', 'Language': 'nl-NL', 'Name': 'Ruben'},
	 {'Gender': 'Female', 'Language': 'pl-PL', 'Name': 'Agnieszka'},
	 {'Gender': 'Male', 'Language': 'pl-PL', 'Name': 'Jacek'},
	 {'Gender': 'Female', 'Language': 'pl-PL', 'Name': 'Ewa'},
	 {'Gender': 'Male', 'Language': 'pl-PL', 'Name': 'Jan'},
	 {'Gender': 'Female', 'Language': 'pl-PL', 'Name': 'Maja'},
	 {'Gender': 'Female', 'Language': 'pt-BR', 'Name': 'Vitoria'},
	 {'Gender': 'Male', 'Language': 'pt-BR', 'Name': 'Ricardo'},
	 {'Gender': 'Male', 'Language': 'pt-PT', 'Name': 'Cristiano'},
	 {'Gender': 'Female', 'Language': 'ro-RO', 'Name': 'Carmen'},
	 {'Gender': 'Female', 'Language': 'ru-RU', 'Name': 'Tatyana'},
	 {'Gender': 'Female', 'Language': 'sv-SE', 'Name': 'Astrid'},
	 {'Gender': 'Female', 'Language': 'tr-TR', 'Name': 'Filiz'}
	]}

###Language dict

	languages = {
	"sv-SE": "Swedish",
	"is-IS": "Icelandic",
	"tr-TR": "Turkish",
	"ro-RO": "Romanian",
	"nl-NL": "Dutch",
	"nb-NO": "Norwegian",
	"da-DK": "Danish",
	"pt-PT": "European Portuguese",
	"cy-GB": "Welsh",
	"fr-FR": "French",
	"pt-BR": "Brazilian Portuguese",
	"ru-RU": "Russian",
	"es-US": "American Spanish",
	"en-GB": "British English",
	"fr-CA": "Canadian French",
	"en-GB-WLS": "Welsh English",
	"en-US": "American English",
	"it-IT": "Italian",
	"de-DE": "German",
	"en-IN": "Indian English",
	"en-AU": "Australian English",
	"pl-PL": "Polish",
	"es-ES": "Castilian Spanish"
	}

###adding a voice
The voice key is in the settings. You can have a different voice for both the front and the back.
Just type:

	def add_card(self, front_text=None, back_text=None, front_media=None, back_media=None, front_options=None, back_answers=None, front_settings={"voice": {'language': {'Language': 'en-GB', 'Name': 'Emma'}})

*Note* you can leave out some of the fields if you wish, but then there is a chance you will get a different voice if another voice matches the specifications before it reaches the voice you want.

