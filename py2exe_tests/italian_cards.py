# coding: latin-1
"""
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
deck = decks.Deck

utensili = deck('utensili')
c = utensili.add_card
c('pan', 'padella')
c('lid', 'coperchio')
c('ladle', 'mestolo')
c('bowl', 'ciotola')
c('strainer', 'scola pasta')
c('blender', 'frullatore')
c('spoon', 'cucchiaio')
c('knife', 'coltello')
c('baking tin', 'teglia')
c('salad bowl', 'terrina')
c('caserole dish', 'casseruola')
c('cutting board', 'tagliere')
c('fork', 'forchetta')
c('coffeepot', 'caffettiera')
c('teapot', 'Teiera')
c('espresso cup', 'Tazzina')
c('saucer', 'Piattino')
c('teaspoon', 'Cucchiaino')
c('sugar bowl', 'Zuccheriera')
c('tea cup', 'tazza')
c('pitcher', 'brocca')
c('table cloth', 'tovaglia')
c('grill', 'Bistecchiera')
c('pressure cooker', 'pentola a pressione')
c('skillet', 'tegame')
c('rolling pin', 'matterello')
c('basting brush', 'pennello')
c('chopping knife whith the crescent blade', 'mezzaluna')

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
