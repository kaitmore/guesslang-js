# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['guess.py'],
             pathex=['/usr/local/bin/miniconda3/lib/python3.7/site-packages', '/Users/kaitmore/Projects/guesslang-js'],
             binaries=[],
             datas=[('/usr/local/bin/miniconda3/lib/python3.7/site-packages/guesslang/data/', './guesslang/data/')],
             hiddenimports=[],
             hookspath=['./hooks/'],
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
          name='guess',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='guess')