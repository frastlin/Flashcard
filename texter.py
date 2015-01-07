#Pass text of either a dict or a string when calling the class, then you can shift the displayed text, scroll it, and change it's settings.

class Text:
	"""Class for creating text objects that will display to the screen"""

	def __init__(self, text="Hello world", settings={}, surface=None, xpos=350, ypos=100, center=True):
		extra_spacing=0
		self.default_settings = {"current_font": {'size': 46, 'spacing': 0, 'font_color': 'white', 'font_background': 'black', 'font': 'freesansbold.ttf'},
			"default_font": {'size': 46, 'font_color': 'white', 'spacing': 0, 'font_background': 'black', 'font': 'freesansbold.ttf'},
			"highlighted_font": {'size': 46, 'font_color': 'black', 'spacing': 0, 'font_background': 'white', 'font': 'freesansbold.ttf'}
			}
		self.settings = self.setter(settings, self.default_settings)


class Fonter:
	"""Placing the font settings in a class(and putting each setting to be assigned in a function) removes the need for copy. It is 45 seconds with deep copy on 1000000 and 2.5 seconds for assigning a class to 1000000. having a built-in function rather than doing refresh or select is 0.1 seconds slower for 1m."""
	def __init__(self, settings={}):
		self.current_font = {'size': 46, 'spacing': 0, 'font_color': 'white', 'font_background': 'black', 'font': 'freesansbold.ttf'} # 'ypos': 50, 'xpos': 350}
		self.default_font = {'size': 46, 'font_color': 'white', 'spacing': 0, 'font_background': 'black', 'font': 'freesansbold.ttf'}
		self.highlighted_font = {'size': 46, 'font_color': 'black', 'spacing': 0, 'font_background': 'white', 'font': 'freesansbold.ttf'}
		self.update_font(settings)

	def update_font(self, settings):
		"""Will go through the settings and update the classes fonts if needed"""
		if not settings:
			return 0
		elif settings.get('default_font'):
			self.default_font.update(settings['default_font'])
		elif settings.get('highlighted_font'):
			self.highlighted_font.update(settings['highlighted_font'])
		self.current_font.update(self.default_font)

	def refresh(self):
		"""Will switch current_font back to default_font"""
		self.current_font.update(self.default_font)

	def select(self):
		"""Will switch current_font to highlighted_font"""
		self.current_font.update(self.highlighted_font)


#