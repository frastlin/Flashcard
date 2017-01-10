# -*- mode: python -*-
a = Analysis(['engine.py'],
             pathex=['C:\\Users\\brandon\\programming\\PythonFiles\\applications\\flashcard'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
               a.zipfiles,
               a.datas,
          name='engine.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               strip=None,
               upx=True,
               name='engine')
