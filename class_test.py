#This is dealing with inharatence
import copy
dict1 = {'fred': {'joe': [{'july': 6, 'june': 5}, 'apples', 'oranges'], 'sammy': 'margaret'}, 'god': 'creats'}


dict1['fred']['joe'][0]['july'] = 9

class Settings(object):
	def __init__(self, color='white', size=20):
		self.color = color
		self.size = size
	def run(self):
		print self.color, self.size

d1 = {'fred': 3, 'joe': 5, 'frank': 1}

l = ['fred', 'joe', 1, 2, 4]

#for k, v in d1.items():
#	v = d1[k]
#	print "this is the key: %s, this is the value: %s." % (k, {'4': 4})

master_dict = {'fred': 5, 'joe': 2, 'sam': 9}

card_dict = copy.deepcopy(master_dict)
card_dict['fred'] = 42
card_dict['crums'] = 43

def change_master_dict(change):
	global master_dict, card_dict
	#check what items are different between the master and the card dict so that we don't change any local settings in the card_dict
	different_items = {}
	for k in card_dict:
		if k not in master_dict or master_dict[k] != card_dict[k]:
			different_items[k] = card_dict[k]
	#make our change and make sure both dicts have the change
	master_dict.update(change)
	card_dict.update(change)
	#Put back in the local settings
	for k in different_items:
		card_dict[k] = different_items[k]

l1 = [(1, 4), (1, 3), (1, 9), (1, 6), (9, 9)]

#for i in card.settings:
#	self.front_default[i] = i

[self.front_default.update{k: card.settings[k]} for k in card.settings]
