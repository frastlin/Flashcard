# -*- mode: python -*-
a = Analysis(['engine.py'],
             pathex=['C:\\Users\\brandon\\programming\\PythonFiles\\applications\\flashcard'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

def Datafiles(*filenames, **kw):
    import os

    def datafile(path, strip_path=True):
        parts = path.split('/')
        path = name = os.path.join(*parts)
        if strip_path:
            name = os.path.basename(path)
        return name, path, 'DATA'

    strip_path = kw.get('strip_path', True)
    return TOC(
        datafile(filename, strip_path=strip_path)
        for filename in filenames
        if os.path.isfile(filename))

docfiles = Datafiles("freesansbold.ttf")

"""
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          docfiles,
          name='Test1.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               docfiles,
               name=os.path.join('dist', 'pdfposter'))
"""