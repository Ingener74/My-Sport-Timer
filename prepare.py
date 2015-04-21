#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Установи в PATH пути до pyside-rcc, и pyside-uic, последний раз у меня это были
C:/Python27/Scripts
C:/Python27/Lib/site-packages/PySide
"""


import subprocess

subprocess.Popen(['pyside-rcc', 'data/resouces.qrc',  '-o', 'resouces_rc.py'])

subprocess.Popen(['pyside-uic', 'data/mainwindow.ui', '-o', 'ui_mainwindow.py'])
subprocess.Popen(['pyside-uic', 'data/settings.ui'  , '-o', 'ui_settings.py'])
