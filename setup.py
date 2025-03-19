from setuptools import setup

APP = ['find_camera.py']
DATA_FILES = ['Info.plist']
OPTIONS = {
    'argv_emulation': True,
    'plist': 'Info.plist',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
