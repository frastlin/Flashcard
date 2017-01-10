from distutils.core import setup
import py2exe
import accessible_output

data_files = accessible_output.py2exe_datafiles()

setup(console=['helloworld.py'], data_files=data_files, zipfile="zipped_stuff.zip",
options={'py2exe': {
#These must be modules, 'packages': can also be used.
'includes': ['jojo'],
#1 is all compressed, 2 is almost all compressed and 3 is not much compressed
'bundle_files': 1,
#Instead of making a "dist" dir when done, it will create this dir.
'dist_dir': 'helloworld_dir'
}})
