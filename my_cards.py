"""
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
"""
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
