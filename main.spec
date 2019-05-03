# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
<<<<<<< HEAD
             pathex=['/Users/angelflores/Github/Tutor_Time'],
=======
             pathex=['C:\\Users\\Henry\\Documents\\GitHub\\Tutor_Time'],
>>>>>>> 570e0bbcb5c32d03229a0c27839d62befc3fd00e
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
app = BUNDLE(coll,
             name='main.app',
             icon=None,
             bundle_identifier=None)
