#This is the module that deals with error messages and output
log_file = "Flashcard_log.txt"
import sys, traceback

#so the error log doesn't show up with py2exe
sys.stderr = sys.stdout

production = True

def log(message, level=0):
	"""Call this function in order to print to the log"""
	if level == 0 and not production:
		log_write(message)
	elif level == 1 and not production:
		trace(message)

def trace(message):
	log_write("\nMessage:\n%s\nPython error:" % message)
	with open(log_file, "a") as f:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)
		traceback.print_exception(exc_type, exc_value, exc_traceback)

def log_write(message):
	"""Will write to the file and print to the console"""
	print(message)
	with open(log_file, "a") as f:
		f.write(message + "\n")

def start(message=None, clear=False):
	"""Will date and add the message to the logging file"""
	import time
	current_string = "Started at:\n"
	current_string += time.strftime("%A %B %d at %I:%M%p", time.localtime())
	if message:current_string += "\n" + message
	if clear:
		f = open(log_file, "w")
		f.close()
	log(current_string)

