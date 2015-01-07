from distutils.core import setup
import py2exe

data_files = [("Italian_stuff", ["italian_cards.py"]),]

setup(data_files=data_files, console=['helloworld.py'])
