#This is our basic setup for cards
from voice import Voice

class Side(object):
	def __init__(self, text="hello world", media=None, settings={}, options=None):
		"""Settings for each card
			text: text that is the actual meet of the thing. It can be None if only media plays.
			media: sound or video object for pygame
			options: when on the front card are text that shows as options. when on the back card are the correct options.
		"""
		self.text = text
		self.media = media
		self.options = options
		self.settings = settings

		if settings.get('voice'):
			self.settings['voice'] = Voice(self.settings['voice'])


		#Operation variables
