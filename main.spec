# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.win32 import versioninfo as vi

block_cipher = None

# Caminho absoluto para o ícone
icon_path = os.path.abspath('assets/report.ico')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/*', 'assets')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ImportPO',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=icon_path,  # Opcional: especifique o caminho para o ícone do seu aplicativo
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ImportPO',
)
