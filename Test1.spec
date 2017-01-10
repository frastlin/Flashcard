# -*- mode: python -*-
a = Analysis(['engine.py'],
             pathex=['C:\\Users\\brandon\\programming\\PythonFiles\\applications\\flashcard'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
#a.datas += [("freesansbold.ttf", "freesansbold.ttf", "DATA")]


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Test1.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
