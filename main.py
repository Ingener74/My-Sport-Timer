#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
try:
	from PySide.QtGui import *
	from PySide.QtCore import *
	from ui_mainwindow import *
	from ui_settings import *
except Exception as e:
	print e

class SettingsWindow(QWidget, Ui_SettingsWindow):
	def __init__(self, parent=None):
		super(SettingsWindow, self).__init__(parent)
		self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		
		self.SettingsAction.triggered.connect(self.settings)
		
		self.set = SettingsWindow()
		
	def settings(self):
		self.set.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()
