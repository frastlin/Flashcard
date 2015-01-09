# coding: latin-1
"""
add these to the idiams:
http://matadornetwork.com/abroad/10-idioms-italians-understand/

words I don't know:
PIROFILA
terrine
look at chapter 4 in buona patito

sbucciare to peal
unire  to combine
cuoceteli cook them
"""
#Cards for italian
import decks
from voice import Voice
deck = decks.Deck

utensili = deck('utensili')
utensili.default_front['voice'] = Voice(current_voice={'Language': 'en-US', 'Name': 'Salli'})

c = utensili.add_card
c('pan', 'padella', back_media='sounds/pan.ogg')
c('lid', 'coperchio', back_media='sounds/lid.ogg')
c('ladle', 'mestolo', back_media='sounds/ladle.ogg')
c('bowl', 'ciotola', back_media='sounds/bowl.ogg')
c('strainer', 'scola pasta', back_media='sounds/strainer.ogg')
c('blender', 'frullatore', back_media='sounds/blender.ogg')
c('spoon', 'cucchiaio', back_media='sounds/spoon.ogg')
c('knife', 'coltello', back_media='sounds/knife.ogg')
c('baking tin', 'teglia', back_media='sounds/tin.ogg')
c('salad bowl', 'terrina', back_media='sounds/salid_bowl.ogg')
c('caserole dish', 'casseruola', back_media='sounds/casorole_dish.ogg')
c('cutting board', 'tagliere', back_media='sounds/cutting_board.ogg')
c('fork', 'forchetta', back_media='sounds/fork.ogg')
c('coffeepot', 'caffettiera', back_media='sounds/coffee_pot.ogg')
c('teapot', 'Teiera', back_media='sounds/tea_pot.ogg')
c('espresso cup', 'Tazzina', back_media='sounds/expresso_cup.ogg')
c('saucer', 'Piattino', back_media='sounds/saucer.ogg')
c('teaspoon', 'Cucchiaino', back_media='sounds/tea_spoon.ogg')
c('sugar bowl', 'Zuccheriera', back_media='sounds/sugar_bowl.ogg')
c('tea cup', 'tazza', back_media='sounds/tea_cup.ogg')
c('pitcher', 'brocca', back_media='sounds/pitcher.ogg')
c('table cloth', 'tovaglia', back_media='sounds/tablecloth.ogg')
c('grill', 'Bistecchiera', back_media='sounds/grill.ogg')
c('pressure cooker', 'pentola a pressione', back_media='sounds/pressure_cooker.ogg')
c('skillet', 'tegame', back_media='sounds/skillet.ogg')
c('rolling pin', 'matterello', back_media='sounds/rolling_pin.ogg')
c('basting brush', 'pennello', back_media='sounds/basting_brush.ogg')
c('chopping knife whith the crescent blade', 'mezzaluna', back_media='sounds/moon.ogg')

verbi = deck('verbi')
c = verbi.add_card
c('to flavor', 'condire')
c('to walk', 'caminare')
c('to continue', 'continuare')
c('to cover', 'coprire')
c('to cook', 'cuocere')
c('distribute', 'distribuire')
c('to let', 'lasciare')
c('to stur', 'mescolare')
c('to put', 'mettere')
c('to brown', 'rosolare')
c('to pour', 'versare')
c('to fry', 'soffriggere')
c('to mince', 'tagliare')
c('to flatten out, as in doe', 'stendere')
c('to oil', 'ungere')
c('to serve', 'servire')
c('to shell', 'sbucciare')
c('to melt', 'sciogliere')


espressioni_idiomatiche = deck("Espressioni Idiomatiche")
c = espressioni_idiomatiche.add_card
c("bad weather", "c'è un tempo da lupi")
c('love at first sight', 'È stato un colpo di fulmine')
c('head is in the clouds', 'Ha sempre la testa fra le nuvole')
c("it's raining buckets", "Sta piovendo a catinelle")
c("lightning fast", "L'ho fatto in un lampo")
c("I'm speaking to the wind", "Mi sembra di parlare al vento")
c("Someone decides for everyone", "Fa il bello e il cattivo tempo")
c("His heart is as cold as ice", "Ha un cuore di ghiaccio")
c("Powerful people don't harm each other", "Lupo non mangia lupo")
c("Old habbets die hard", "Il lupo perde il pelo ma non il vizio")
c('to cry wolf', 'Gridare "al lupo"')
c("I am starvin marvin", "Avere una fame da lupo")
#c("an apple a day keeps the doctor away", "una mela al giorno, toglie il medico di torno")

tempo = deck('tempo')
"""
il sole
sunny

 È nuvoloso 
cloudy

 C'è nebbia 
fog

 Fa caldo 
hot

 Nevica 
snow

È sereno
clear sky

 C'è un temporale 
storming

 Fa freddo 
cold

 C'è vento 
windy

 Piove
raining
"""

eateries = deck('eateries')
cpres = eateries.add_card
"""
I negozi
IL BAR
LA FRUTTERIA
L'ENOTECA
LA MACELLERIA
LA PANETTERIA
LA PASTICCERIA
LA PESCHERIA
LA PIZZERIA - pizza place
IL RISTORANTE -restaurant
LA ROSTICCERIA
LA TRATTORIA
"""

deck_list = [utensili, verbi, espressioni_idiomatiche]
