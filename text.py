#This is a module for rendering text and backgrounds
import pygame, colors, display

default_font = {'ypos': 100, 'xpos': 350, 'font': 'freesansbold.ttf', 'font_color': 'white', 'size': 42, 'font_background': 'black', 'spacing': 0}

def display_text(text, settings=default_font):
	"""Call this function with a dict of settings and your string to render text."""
	if settings.keys() != default_font.keys():
		[settings.update({i: default_font[i]}) for i in default_font if i not in settings]
	font_color = check_color(settings['font_color'])
	font_background = check_color(settings['text_background'])
	fontObj = pygame.font.Font(settings['font'], settings['size'])
	textSurfaceObject = fontObj.render(text, True, font_color, font_background)
	textRectangleObject = textSurfaceObject.get_rect()
	textRectangleObject.center = (settings['xpos'], settings['ypos'])
	display.add(textSurfaceObject, textRectangleObject)

def complex_multilign(text_settings, extra_spacing=0, xpos=350, ypos=100, center=True, persistent=False, clear=True):
	"""Pass a seperate set of settings for each font"""
	pf = pygame.font.Font
	rect_list = []
	if clear:
		display.persistent_list = []
	for l in text_settings:
		if len(l) == 2:
			#[l[1].update({i: default_font[i]}) for i in default_font if i not in l[1]]
			l = [l[0], settings_check(l[1])]
		else:
			l = [l[0], default_font]
		#I am bringing this here so I can have more controll over the process
		#The 'spacing' in the dict is the extra space between that single lign and the other ligns
		if l[1]['spacing']:
			ypos += l[1]['spacing']
		font_color = l[1]['font_color']
		font_background = l[1]['font_background']
		fontObj = pf(l[1]['font'], l[1]['size'])
		textSurfaceObject = fontObj.render(l[0], True, font_color, font_background)
		textRectangleObject = textSurfaceObject.get_rect()
		if center:
			textRectangleObject.center = (xpos, ypos)
		else:
			textRectangleObject.topleft = (xpos, ypos)
		display.add(source=textSurfaceObject, dest=textRectangleObject, persistent=persistent)
		ypos += fontObj.get_linesize() + extra_spacing + l[1]['spacing']
		rect_list.append(textRectangleObject)
	return rect_list

def simple_multilign(text, settings=default_font):
	"""Call this function to show wrapping text"""
	if settings.keys() != default_font.keys():
		[settings.update({i: default_font[i]}) for i in default_font if i not in settings]
	for l in text:
		display_text(l, settings)
		settings['ypos'] += int((settings['size'] * 1.10))

def text_wrap(text, settings=default_font, extra_spacing=0, xpos=350, ypos=100, center=True):
	"""A function to wrap and display font that could be quite long"""
	settings = settings_check(settings)
	fontObj = pygame.font.Font(settings['font'], settings['size'])
	sizer = fontObj.size
	if sizer(text) > 600 or "\n" in text:
		line_list = text.split('\n')
		current_text = ""
		for line in line_list:
			if sizer(line)[0] > 600:
				current_text += "%s\n" % splitter(line, sizer)
			else:
				current_text += "%s\n" % line
	final_list = [[l, settings] for l in current_text.split('\n')]
	return complex_multilign(text_settings=final_list, extra_spacing=extra_spacing, xpos=xpos, ypos=ypos, center=center)

#	[displayer(final_string=s, fontObj=fontObj, settings=settings, center=center, xpos=xpos, ypos=ypos) for s in final_text]

def splitter(line, sizer, max_size=600):
	"""Will take a line and split it into max_size chuncks"""
	final_string = ""
	temp_string = ""
	word_list = line.split(' ')
	for w in word_list:
		if sizer(temp_string)[0] <= max_size - sizer(w)[0]:
			temp_string += "%s " % w
		else:
			final_string += "%s\n" % temp_string
			temp_string = "%s " % w
	final_string += "%s\n" % temp_string
	return final_string

def displayer(final_string, fontObj, settings, center, xpos, ypos):
	"""Use this to create the rectangle object for a line of text and send it to the display queue"""
	textSurfaceObject = fontObj.render(final_string, True, settings['font_color'], settings['font_background'])
	textRectangleObject = textSurfaceObject.get_rect()
	if center:
		textRectangleObject.center = (xpos, ypos)
	else:
		textRectangleObject = (xpos, ypos)
	display.add(textSurfaceObject, textRectangleObject)

def settings_check(current_settings=None):
	"""Will check if there are settings and if so, will return the updated settings, if not, will return default_font. current_settings needs to be a dict."""
	if current_settings and current_settings != default_font:
		[current_settings.update({i: default_font[i]}) for i in default_font if i not in current_settings]
	else:
		current_settings = default_font
	#color checks for all items that have colors
	current_settings['font_color'] = check_color(current_settings['font_color'])
	current_settings['font_background'] = check_color(current_settings['font_background'])

	return current_settings

def check_color(color=None):
	if isinstance(color, (tuple, list, set)):
		return color
	else:
			c = colors.colors_list1.get(color)
			if c:
				return c
			else:
				return (100, 50, 80)

#print(sorted(pygame.font.get_fonts()))
