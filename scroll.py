#A module for scrolling text
import display

scroll_distance = 0


def scroll(od, highlighted, rects, title):
	"""Will scroll and return the list of options that need to be displayed"""
	global scroll_distance
	distance = len(rects) - highlighted

	if rects[highlighted].y > 380 and len(rects) >= highlighted:
		if not scroll_distance:
			scroll_distance = len([i for i in rects if i.y >= 380])
		[od.pop(0) for i in range(scroll_distance - distance)]

	return (od, highlighted)

#I should create a class that will keep od and update od, then have another od it pulls out and modifies. 
