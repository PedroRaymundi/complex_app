# -*- mode: python ; coding: utf-8 -*-

import pkgutil

import rasterio
import pandas
import osgeo
import numba

# list all rasterio and fiona submodules, to include them in the package
additional_packages = list()
for package in pkgutil.iter_modules(rasterio.__path__, prefix="rasterio."):
    additional_packages.append(package.name)

for package in pkgutil.iter_modules(pandas.__path__, prefix="pandas."):
    additional_packages.append(package.name)

for package in pkgutil.iter_modules(osgeo.__path__, prefix="osgeo."):
    additional_packages.append(package.name)

for package in pkgutil.iter_modules(numba.__path__, prefix="numba."):
    additional_packages.append(package.name)

block_cipher = None

a = Analysis(
    ['complex_app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=additional_packages,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='complex_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
