#These are contents of readme and other stuff

# *~*
readme_python = """
<p><title>Read Me</title></p>

<p><a href="#script">script example</a>
<a href="#index">code index</a></p>

<p>Welcome to the deck scripts of the application.</p>

<h1>***WARNING!!!!!***</h1>

<p>DO NOT DO ANYTHING WITH THE FILES HERE UNLESS YOU KNOW PYTHON!!!</p>

<h1>Instructions for use:</h1>

<p>first, you can put any files here, but a large number of .py files may slow down the program a little at startup as it searches through all the .py files for the line: <br />
deck_list = [] <br />
Every file should have the above line with your decks inbetween the brackets [deck1, deck2, deck3, deck4]. You can have as many decks as you wish in a file. You can also create another folder inside this folder and store all your unfinished decks in it. The program will not see them.</p>

<h1>What scripting options are there</h1>

<p>You can create decks with:
all kinds of background colors (using rgb values), color of text, color of the background of the text...
you can add pictures to the background, you can add your own font files, you can add sounds and mp3, ogg or wav files to your programs, you can add options, key short-cuts, text to speech voices and all kinds of things to each side of the card.</p>

<h2>The deck structure</h2>

<p>There are global settings for each deck and then there are spacific settings for each card and then settings for each side of the card. The order of prefference is:
side,
card,
deck.
so if you set in the deck for all cards to have an orange background and you wanted card number 3 to have a green front and yellow background, you can do that.</p>

<h1>code</h1>

<p>Yeah yeah lets get to the good stuff!</p>

<h3><a name="script">Scripts</a></h3>

<pre><code>import decks
deck = decks.Deck

deck1 = deck("Deck 1")
c = deck1.add_card
c(front_text="What is 1 + 1?", back_text="It is 2!")
c("What is the meaning of life?", "I think you know")
c("When is your birthday?", "It is sometime after the last one")

deck_list = [deck1]
</code></pre>

<h3>What's going on?</h3>

<pre><code>import decks
deck = decks.Deck
</code></pre>

<p>The above two lines are importing the module decks into our script. The line below it is aliasing or assigning the name "deck" to the class inside the module decks that we imported.  </p>

<pre><code>deck1 = deck("Deck 1")
c = deck1.add_card
</code></pre>

<p>Here we are making a deck named "deck1". <br />
In the second line we are making an alias "c" to be the deck1.add_card function.  </p>

<pre><code>c(front_text="What is 1 + 1?", back_text="It is 2!")
c("What is the meaning of life?", "I think you know")
c("When is your birthday?", "It is sometime after the last one")
</code></pre>

<p>Here we just added 3 cards.  </p>

<pre><code>deck_list = [deck1]
</code></pre>

<p>This final line tells the script all the decks we have in this module. Without the above line, you will have no decks imported.</p>

<h1><a name="index">Scripting Index</a></h1>

<p>There are 3 ways of adding settings to decks: <br />
1. add the settings when you name your deck.
2. add them in an extra line
3. make different settings for each card.</p>

<h2>adding settings when you call the creation of the deck</h2>

<pre><code>def __init__(self, title="Default title"):
    \"\"\"The default options for a deck:
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
    \"\"\"
    #Here are our default sides
    self.title = title
    self.default_front = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': 'black'}
    self.default_back = {'voice': None, 'font': {'size': 40, 'font_color': 'white', 'font': 'freesansbold.ttf', 'font_background': 'black'}, 'font_location': {'xpos': 350, 'ypos': 100, 'center': True}, 'background': (0, 0, 0), 'cards_repeat': True, 'repeating': 1, 'random': True}
    #*note*, here is what the scripting deck_settings is, it is really a refference to the default_back.
    #'cards_repeat': True, 'repeating': 1, 'random': True
</code></pre>

<h3>default back settings</h3>

<p>The default back settings are really the back settings and global settings in one. if you use the scripting language, you are used to using a shortcut to accessing the default back. The global options are</p>

<pre><code>#'cards_repeat': True, 'repeating': 1, 'random': True
</code></pre>

<p><code>cards_repeat</code> is just saying if you would like the cards to come back after being played. You can change this on each card.  </p>

<p>repeating is saying how many cards till that card shows up in the deck again. This is because a random card is chosen when you have random selected and you don't really want to get the same card 3 times in a row.  </p>

<p>random is just what it sounds like, it calls a random.choice on the deck.  </p>

<h2>adding settings on a different line</h2>

<p>if we wished to not have our deck be random we would have this line under the c = <code>deck1.add_card</code>  </p>

<pre><code>deck1.default_back['random'] = False
</code></pre>

<p>or we could also do:  </p>

<pre><code>deck1.update({'random': False})
</code></pre>

<p>Both are perfectly fine!</p>

<h2>adding settings to each card</h2>

<p>in the <code>add_card</code> function there is a <code>back_settings</code> and <code>front_settings</code> argument. <br />
to change the size of the font on the back of the card you would type:</p>

<pre><code>c("What is the meaning of life?", "I think you know", back_settings={"font": {"size": 42}})
</code></pre>

<h2><code>add_card</code> function</h2>

<pre><code>def add_card(self, front_text=None, back_text=None, front_media=None, back_media=None, front_options=None, back_answers=None, front_settings={}, back_settings={}):
</code></pre>

<p>You can add text, media, settings and the other stuff has not been added yet. You don't need to fill out everything on settings, it will be put into the settings by an update when the card is called.</p>

<h2>Adding voices:</h2>

<h3>dict of voices</h3>

<pre><code>voice_dict = {'Voices': [
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
</code></pre>

<h3>Language dict</h3>

<pre><code>languages = {
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
</code></pre>

<h3>adding a voice</h3>

<p>The voice key is in the settings. You can have a different voice for both the front and the back.
Just type:</p>

<pre><code>def add_card(self, front_text=None, back_text=None, front_media=None, back_media=None, front_options=None, back_answers=None, front_settings={"voice": {'language': {'Language': 'en-GB', 'Name': 'Emma'}})
</code></pre>

<p><em>Note</em> you can leave out some of the fields if you wish, but then there is a chance you will get a different voice if another voice matches the specifications before it reaches the voice you want.</p>

"""

# *~*
readme_script = """
<!DOCTYPE html>
<html>
<head>
<title>How to Make Decks</title>
</head>
<body>
<p><a href="#easy">Easy deck creation</a>
<a href="#cool">Adding Cool Stuff</a>
<a href="#tags">Tags</a>
<a href="#help">Help Me</a></p>

<h1>discription</h1>

<p>Flashcard is meant to be the most simple way to make and use flash cards. <br />
To get going, all you need to do is make a file with a <em>text file (.txt extension)</em> in this folder and for the first line, make a title. for all the other lines, write the front and on the next line write the back. For example:  </p>

<h2><a name="easy">easy flash card creation</a></h2>

<pre><code>My First Deck

Why did the chicken cross the road?
Cause it wanted to get to the other side!
What did the big bucket say to the little bucket?
You look a little pail!
Why did the poney sound strange?
Because it was a little horse!
</code></pre>

<h1><a name="cool">Adding Cool Stuff</a></h1>

<p>Flashcard has the ability to add media like sound files. In order to do this you need to insert something called <em>tags</em>. Tags are in the format: <br />
tag:command <br />
<em>Warning</em> You must put the colen (<em>:</em>) after the tag and then put the command after it. Another tag is the voice tag. You can make a voice by adding a command to the command like: <br />
voice:language=French, gender=female  </p>

<h2>Tagged Deck</h2>

<pre><code>title:My second deck  

What did the skeleton say when he got on the motorcycle?
I was bone to be wild!
media:sounds/bone.ogg
What's your name?
Mine's Sally!
voice:name=sally
</code></pre>

<h2><a name="tags">Tags</a></h2>

<ul>
<li>media, add media</li>
<li>voice add a voice from IVONA  Text to Speach</li>
<li>title used to start a new deck, used if you wish to add more than one deck in a document</li>
<li>text Not needed, but makes the decks a little more clear, it will just say that you are making text for the  cards</li>
<li>deck settings has reverse, random, <code>cards_repeat</code> and repeating and is used for the global settings. More later</li>
</ul>

<h2>voice</h2>

<p>To add voices you need to choose at leaste one item from the following: <br />
name, gender, language  </p>

<h3>name</h3>

<p>The name argument is very spacific and will make sure you get the correct name. But sometimes there are two voices with the same name. Here is the list of names: <br />
Salli Joey Naja Mads Marlene Hans Nicole Russell Amy Brian Emma Gwyneth Geraint Gwyneth Geraint Raveena Chipmunk Eric Ivy Jennifer Justin Kendra Kimberly Conchita Enrique Penelope Miguel Chantal Celine Mathieu Dora Karl Carla Giorgio Liv Lotte Ruben Agnieszka Jacek Ewa Jan Maja Vitoria Ricardo Cristiano Carmen Tatyana Astrid Filiz <br />
There are 49 names and Gwyneth is the only one where it is in both Welsh English and Welsh.</p>

<h3>gender</h3>

<p>This is simple, but often helps you narrow down a voice. You have <br />
male <br />
female <br />
and if you know what language, but not what the name is, you can just do something like: <br />
language=Italian, gender=female  </p>

<h3>language</h3>

<p>Here is a list of languages. If you just would like American English, you only need to write english and it will default to english:  </p>

<ul>
<li>Swedish</li>
<li>Icelandic</li>
<li>Turkish</li>
<li>Romanian</li>
<li>Dutch</li>
<li>Norwegian</li>
<li>Danish</li>
<li>European Portuguese</li>
<li>Welsh</li>
<li>French</li>
<li>Brazilian Portuguese</li>
<li>Russian</li>
<li>American Spanish</li>
<li>British English</li>
<li>Canadian French</li>
<li>Welsh English</li>
<li>American English</li>
<li>Italian</li>
<li>German</li>
<li>Indian English</li>
<li>Australian English</li>
<li>Polish</li>
<li>Castilian Spanish</li>
</ul>

<h2>deck settings</h2>

<p>If you would like some controll over what your deck does when it runs, you can place the line <br />
<code>deck_settings:</code> <br />
right after the title. You then put the commands after it like: <br />
<code>deck_settings:random=no</code> <br />
will turn off random. <br />
Here are the commands:  </p>

<h3>reverse</h3>

<p>will make it so that the back of the card will be first and then it will flip to the front. <br />
Type yes or no</p>

<h3>random</h3>

<p>By default this is yes, but you can make it no so that your cards will show up in the order you made them. <br />
Type yes or no</p>

<h3><code>cards_repeat</code></h3>

<p>If you only wish for a card to show up once, make this no. <br />
Type yes or no</p>

<h3>repeating</h3>

<p>This makes it so that a card will not show up twice in a row. It makes a holding area for the size you specify here. By default it is 1. <br />
Type a number that is smaller than the number of cards you have.  </p>

<h1><a name="help">Help Me!</a></h1>

<p>Here are some common problems  </p>

<h2>My voice is freazing or not playing</h2>

<p>This means that your internet connection is slow or not there. When you run a deck the voice files will be stored on your computer for off-line playing, so run your deck first online, then you can run it offline.</p>

<h2>After I made my deck, the program crashed!</h2>

<p>Make sure you don't have any special characters like &ldquo; &rdquo; make them " or '. If you still can't get it to work, try to write your decks in notepad.</p>

<h2>I don't see my problem here!</h2>

<p>If you don't see your problem here,
<a href="mailto:brandonkeithbiggs@gmail.com?subject=Help me with Flashcard PLEAAAAAAAAAAAASE!!!">Send me an email</a></p>
</body>
</html>
"""

# *~*
my_cards = """\"\"\"
*WARNING!*
Before this runs, you need to change its extension from .txt to .py

Welcome to your very own flashcard maker!
Here you can create your own decks of flash cards very easily, but there are some things you should be aware of before typing anything:

1. Right below this text there are some lines of text. Do NOT delete this, it is very important all files of decks have it! Also, there are 3 quotes before and after this text, those are to tell the computer that this is text and not cards!
2. to create your own deck, go to the lign that says: "#create decks here" and below that you can begin with deck creation.
3. If you see a hash sign like #, it is a comment and that means you can type anything after it and it will not give an error.

If you wish to quickly get started, go to the heading that says: "#sample decks", otherwise, keep reading.

Creating decks and cards:
What the final deck text will look like:
deck1 = deck("Deck 1")
c = deck1.add_card
c(front_text="What is 1 + 1?", back_text="It is 2!")
c("What is the meaning of life?", "I think you know")

If that looks dificult, lets break it down:
first, type what you would like to call your deck only in this file. don't put any spaces in the name. I'll call my deck:
deck1
Next, we need to say to the computer that this is a deck and then what we would like the deck to display as in the program itself. for example, I wish to call my deck in the decks list in the program: "deck 1" so I type:
deck1 = deck("deck 1")
That "= deck(name)" is what specifies to the computer that deck1 really is a deck and not something else.

Next, we add cards:
This is very easy, but kind of a lot of typing. You first type the deck name "deck1" and then follow it with a "." and then "add_card" like:
deck1.add_card
Then we need to add what our card is going to say. We do this by putting our text in (). To tell what side of the card the text is on, you type: front_text or back_text like:
deck1.add_card(front_text="What is 1 + 1?", back_text="1 + 1 = 4!")
*Note* you need to make sure you have both sets of (). Also, the "" two quotes before and after what you wish your card to say or the computer will think you are trying to tell it something. There is also a "," after the final quote of the first side's text. This is to tell the computer to look for the next side's text.

Making life easier:
Now, I don't like typing a lot, so I am going to make a short-cut for adding my cards to deck1. I am going to tell the computer that "c" is to add a card. So I need to type:
c = deck1.add_card
Now I only need to type "c" followed by my (statements) to add a card!
Another cool thing is that I don't need to type front_text and back_text all the time. I can just put my quotes of text in seperated by the comma "," like:
c("Why is the sky blue?", "Good question")
This will make adding cards much faster.
When you wish to add another deck, you just repeat these above steps, but with different names:
deck2 = deck("Deck 2")
c = deck2.add_card
c("What is the meaning of life?", "I think you know...")

When we are finished, there is a little line at the bottom of the file that says:
deck_list = []
when we are done creating a deck, we add the deck's name inbetween those brackets [] like:
deck_list = [deck1, deck2]

in conclusion:
It is very easy to add a deck, you just type the name of your deck, a short cut to tell the computer to add a card to the deck, then type the front side of the card's text, then the back side of the card's text, then add it to the deck_list. That is all!

#sample decks
#You can copy and paste this into the body of the document and see what turns out.
deck1 = deck("Deck 1")
c = deck1.add_card
c("What is 1 + 1?", "It is 2!")
c("What is the meaning of life?", "I think you know")
c("When is your birthday?", "It is sometime after the last one")

deck2 = deck("Deck 2")
c = deck2.add_card
c("What color is the blue sky on a sunny day?", "Orange!")
c("Why did the chicken cross the road?", "uh... good question! I guess I'll never know.")
c("When do you wake up in the morning?", "Too early")

deck_list = [deck1, deck2]
\"\"\"
#** Do not remove this text **
import decks
deck = decks.Deck
# ** end of important text **

#sample decks
#You can copy and paste this into the body of the document and see what turns out.
deck1 = deck("Deck 1")
c = deck1.add_card
c("What is 1 + 1?", "It is 2!")
c("What is the meaning of life?", "I think you know")
c("When is your birthday?", "It is sometime after the last one")

deck2 = deck("Deck 2")
c = deck2.add_card
c("What color is the blue sky on a sunny day?", "Orange!")
c("Why did the chicken cross the road?", "uh... good question! I guess I'll never know.")
c("When do you wake up in the morning?", "Too early")

deck_list = [deck1, deck2]
"""

# *~*
example_deck = """Attension! Click me!
deck settings:random=no

Hit enter
To change sides and cards!

What did the skeleton say when he got on the motorcycle?
I was bone to be wild!
media:sounds/bone.ogg

Make a text (.txt file) in the My Decks folder
to make your own decks!

What did the big bucket say to the little bucket?
You look a tad bit pail!
voice:name=emma

Press escape
To get out of the deck and program!

"""
