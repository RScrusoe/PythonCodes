# -*- mode: python -*-

block_cipher = None


a = Analysis(['test2.py'],
             pathex=['C:\\Users\\RS Rahul\\OneDrive\\Documents\\My Python codes'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='test2',
          debug=False,
          strip=False,
          upx=True,
          console=True )
