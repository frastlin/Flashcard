# The script from:
#http://www.pygame.org/wiki/Pygame2exe?parent=CookBook
#that changes a pygame game to an exe file.

#this will create a dist directary containing the executable and all the data  dirs.
#all libraries will be bundled in executable file.

try:
	from distutils.core import setup
	import py2exe, pygame
	from modulefinder import Module
	import glob, fnmatch
	import os, sys, shutil
	import operator
except ImportError, message:
	raise SystemExit, "Unable to load module: %s" % message

#hack that fixes the pygame mixer and pygame font:

#save the orriginal before we edit it
originalIsSystemDLL = py2exe.build_exe.isSystemDLL

def isSystemDLL(pathname):
	"""replaces the py2exe build_exe function."""
	#checks if the freetype and ogg dlls are being included:
	if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
		return 0
	#if not one of the above dlls, return the orriginal function we saved above:
	return originalIsSystemDLL(pathname)

#Now we override the py2exe orriginal function with the one we created above:
py2exe.build_exe.isSystemDLL = isSystemDLL

class pygame2exe(py2exe.build_exe.py2exe):
	"""not sure when we call this, but it has the including of the dlls for the music and font modules."""

#Here is a hack to make sure pygame's default font is included:
	def copy_extensions(self, extensions):
		#get pygame default font
		pygameDir = os.path.split(pygame.base.__file__)[0]
		pygame_default_font = os.path.join(pygameDir, pygame.font.get_default_font())

		#add font to the list of extensions to be coppied:
		extensions.append(Module("pygame.font", pygame_default_font))
		py2exe.build_exe.py2exe.copy_extensions(self, extensions)

class BuildExe(object):
	"""Now we create the class that handles all the data we will need for our dist folder"""

	def __init__(self):
		#the name of our starting module.py:
		self.script = "engine.py"
		
		#name of program
		self.project_name = "Flashcard"

		#Project URL:
		self.project_url = "about_none"

		#version of program:
		self.project_version = "1.0"

		#License of the program:
		self.license = "my app's license"

		#Author of program:
		self.author_name = "Brandon Keith Biggs"
		self.author_email = "brandonkeithbiggs@gmail.com"
		self.copyright = "Copyright (c) 2015 Brandon Keith Biggs"

		#description:
		self.project_description = "An interactive flashcard engine"

		#Icon file, will use pygame default:
		self.icon_file = None

		#extra files or dirs copied to game
		self.extra_datas = []

		#extra or excluded python modules:
		self.extra_modules = []
		self.exclude_modules = []

		#dll excludes
		self.exclude_dll = []

		#python packages to be included (in string form)
		self.extra_scripts = []

		#zip file name, None will bundle files in the exe rather than the zip file
		self.zipfile_name = None

		#dist directory:
		self.dist_dir = 'dir'

	def opj(self, *args):

		path = os.path.join(*args)
		return os.path.normpath(path)

	def find_data_files(self, srcDir, *wildcards, **kw):

		#get a list of files under the srcDir matching the wildcards that is returned in a format to be used for install_data
		def walk_helper(arg, dirname, files):
			if '.svn' in dirname:
				return
			names = []
			lst, wildcards = arg
			for wc in wildcards:
				wc_name = self.opj(dirname, wc)
				for f in files:
					filename = self.opj(dirname, f)

					if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
						names.append(filename)

			if names:
				lst.append((dirname, names,))

		file_list = []
		recursive = kw.get('recursive', True)
		if recursive:
			os.path.walk(srcDir, walk_helper, (file_list, wildcards))
		else:
			walk_helper((file_list, wildcards), srcDir, [os.path.basename(f) for f in glob.glob(self.opj(srcdir, '*'))])

		return file_list

	def run(self):

		if os.path.isdir(self.dist_dir):
			shutil.rmtree(self.dist_dir)

		#Use the default pygame icon if none given:
		if not self.icon_file:
			path = os.path.split(pygame.__file__)[0]
			self.icon_file = os.path.join(path, 'pygame.ico')

		#list all datafiles to add
#		extra_datas = []
#		for data in self.extra_datas:
#			if os.path.isdir(data):
#				extra_datas.extend(self.find_data_files(data, '*'))
#			else:
#				extra_datas.append(('.', [data]))
		extra_datas = self.extra_datas


		setup(
			cmdclass = {'py2exe': pygame2exe},
			version=self.project_version,
			description=self.project_description,
			name=self.project_name,
			url=self.project_url,
			author=self.author_name,
			author_email=self.author_email,
			license=self.license,
			zipfile=self.zipfile_name,
			data_files=extra_datas,
			dist_dir=self.dist_dir,


			#targets to build:
			windows=[{
				'script': self.script,
				'icon_resources': [(0, self.icon_file)],
				'copyright': self.copyright,
			}],

			options={'py2exe': {
				'optimize': 2,
				'bundle_files': 1,
				'compressed': True,
				'excludes': self.exclude_modules,
				'packages': self.extra_modules,
				'dll_excludes': self.exclude_dll,
				'includes': self.extra_scripts
				}
			})

		#Remove the build folder
		if os.path.isdir('build'):
			shutil.rmtree('build')

if __name__ == '__main__':
	if operator.lt(len(sys.argv), 2):
		sys.argv.append('py2exe')

	#Run our script:
	build_1 = BuildExe()

	import accessible_output
	datas = accessible_output.py2exe_datafiles()
	datas.append(('sounds', ['sounds/bone.ogg']))
	datas.append('freesansbold.ttf')
	datas.append('cacert.pem')
	build_1.extra_datas = datas
	build_1.dist_dir = 'Flashcard/'
	build_1.run()

	raw_input("Press any key to continue > ")
