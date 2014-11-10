#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

subprocess.Popen(['pyside-rcc', 'data/resouces.qrc',  '-o', 'resouces_rc.py'])

subprocess.Popen(['pyside-uic', 'data/mainwindow.ui', '-o', 'ui_mainwindow.py'])
subprocess.Popen(['pyside-uic', 'data/settings.ui'  , '-o', 'ui_settings.py'])
