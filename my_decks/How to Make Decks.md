<title>How to Make Decks</title>

[Easy deck creation](#easy)
[Adding Cool Stuff](#cool)
[Tags](#tags)
[Help Me](#help)

#discription
Flashcard is meant to be the most simple way to make and use flash cards.  
To get going, all you need to do is make a file with a *text file (.txt extension)* in this folder and for the first line, make a title. for all the other lines, write the front and on the next line write the back. For example:  

##<a name="easy">easy flash card creation</a>
	My First Deck
	
	Why did the chicken cross the road?
	Cause it wanted to get to the other side!
	What did the big bucket say to the little bucket?
	You look a little pail!
	Why did the poney sound strange?
	Because it was a little horse!

# <a name="cool">Adding Cool Stuff</a>
Flashcard has the ability to add media like sound files. In order to do this you need to insert something called *tags*. Tags are in the format:  
tag:command  
*Warning* You must put the colen (*:*) after the tag and then put the command after it. Another tag is the voice tag. You can make a voice by adding a command to the command like:  
voice:language=French, gender=female  
##Tagged Deck

	title:My second deck  
	
	What did the skeleton say when he got on the motorcycle?
	I was bone to be wild!
	media:sounds/bone.ogg
	What's your name?
	Mine's Sally!
	voice:name=sally

##<a name="tags">Tags</a>
- media, add media
- voice add a voice from IVONA  Text to Speach
- title used to start a new deck, used if you wish to add more than one deck in a document
- text Not needed, but makes the decks a little more clear, it will just say that you are making text for the  cards
- deck settings has reverse, random, `cards_repeat` and repeating and is used for the global settings. More later

##voice
To add voices you need to choose at leaste one item from the following:  
name, gender, language  
###name
The name argument is very spacific and will make sure you get the correct name. But sometimes there are two voices with the same name. Here is the list of names:  
Salli Joey Naja Mads Marlene Hans Nicole Russell Amy Brian Emma Gwyneth Geraint Gwyneth Geraint Raveena Chipmunk Eric Ivy Jennifer Justin Kendra Kimberly Conchita Enrique Penelope Miguel Chantal Celine Mathieu Dora Karl Carla Giorgio Liv Lotte Ruben Agnieszka Jacek Ewa Jan Maja Vitoria Ricardo Cristiano Carmen Tatyana Astrid Filiz  
There are 49 names and Gwyneth is the only one where it is in both Welsh English and Welsh.
###gender
This is simple, but often helps you narrow down a voice. You have  
male  
female  
and if you know what language, but not what the name is, you can just do something like:  
language=Italian, gender=female  
###language
Here is a list of languages. If you just would like American English, you only need to write english and it will default to english:  

- Swedish
- Icelandic
- Turkish
- Romanian
- Dutch
- Norwegian
- Danish
- European Portuguese
- Welsh
- French
- Brazilian Portuguese
- Russian
- American Spanish
- British English
- Canadian French
- Welsh English
- American English
- Italian
- German
- Indian English
- Australian English
- Polish
- Castilian Spanish

##deck settings
If you would like some controll over what your deck does when it runs, you can place the line  
`deck_settings:`  
right after the title. You then put the commands after it like:  
`deck_settings:random=no`  
will turn off random.  
Here are the commands:  
###reverse
will make it so that the back of the card will be first and then it will flip to the front.  
Type yes or no

###random
By default this is yes, but you can make it no so that your cards will show up in the order you made them.  
Type yes or no

###`cards_repeat`
If you only wish for a card to show up once, make this no.  
Type yes or no

###repeating
This makes it so that a card will not show up twice in a row. It makes a holding area for the size you specify here. By default it is 1.  
Type a number that is smaller than the number of cards you have.  

#<a name="help">Help Me!</a>
Here are some common problems  
##My voice is freazing or not playing
This means that your internet connection is slow or not there. When you run a deck the voice files will be stored on your computer for off-line playing, so run your deck first online, then you can run it offline.
##After I made my deck, the program crashed!
Make sure you don't have any special characters like &ldquo; &rdquo; make them " or '. If you still can't get it to work, try to write your decks in notepad.

##I don't see my problem here!
If you don't see your problem here,
<a href="mailto:brandonkeithbiggs@gmail.com?subject=Help me with Flashcard PLEAAAAAAAAAAAASE!!!">Send me an email</a>
