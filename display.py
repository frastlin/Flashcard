#This is the module for displaying stuff
import pygame, colors, ticker

#Don't append to this list unless you know what you are doing with the format. Call add to add stuff to this list.
blit_list = []
rect_list = []
old_rect_list = []
flags = {"fill": True}
background = (0, 0, 0)
surfaces = {}

#Here is an event queue, add files with event_queue.schedule
event_queue = ticker.Scheduler(0.001)

def renderer(displaySurface):
	"""is called every iteration of the loop and displays everything in the display_list"""
	global rect_list, old_rect_list, blit_list
	if rect_list:
		if flags["fill"]:
			displaySurface.fill(background)
		[displaySurface.blit(source=i[0], dest=i[1], area=i[2], special_flags=i[3]) for i in blit_list]
		rects = [i for i in rect_list]
		rects += old_rect_list
		old_rect_list = [i for i in rect_list]
		rect_list = []
		blit_list = []
		if not surfaces.get("main"):
			surfaces["main"] = displaySurface
		flags["fill"] = True
		return rects

def draw(shape, fill=False):
	"""Will add the shape to the display_list"""
	rect_list.append(shape)
	if not fill:
		flags["fill"] = False

def add(source, dest, area=None, special_flags=0, persistent=False, fill=True):
	"""Use this to add objects, it will make sure you are adding them in the right format"""
	blit_list.append((source, dest, area, special_flags, persistent))
	rect_list.append(dest)
	if not fill:
		flags["fill"] = False

def change_background(color=(0, 0, 0)):
	"""Call this to change the color of the background. either an string or a rgb tuple"""
	global background
	background = check_color(color)

def check_color(color=None):
	if isinstance(color, (tuple, list, set)):
		return color
	else:
			c = colors.colors_list1.get(color)
			if c:
				return c
			else:
				return (100, 50, 80)
