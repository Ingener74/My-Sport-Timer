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

class SportTimer:
	def __init__(self, minutes, seconds, onCountdown):
		if minutes > 59 or minutes < 0:
			raise RuntimeError("minutes must be less than 59 and more than 0")
		self.min           = minutes
		if seconds > 59 or seconds < 0:
			raise RuntimeError("secons must be less than 59 and more than 0")
		self.sec           = seconds
		self._onCountdown  = onCountdown

	def dec(self):
		if self.sec == 0 and self.min == 0:
			self._onCountdown()
		elif self.sec == 0 and self.min != 0:
			self.min -= 1
			self.sec = 59
		else:
			self.sec -= 1
	
	def __str__(self):
		outstr = ''
		if self.min < 10:
			outstr += '0'
		outstr += str(self.min) + ':'
		if self.sec < 10:
			outstr += '0'
		outstr += str(self.sec)
		return outstr

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
		
		self.newSportTimer()
		self.lcdNumberTime.display(str(self._sportTimer))
		
		self.pushButtonStart.connect(SIGNAL('clicked()'), self.start_button)
		
	def OnCountdown(self):
		self.newSportTimer()
		QSound('data/bell.wav').play()
#		self.TrayIcon.showMessage(u'Спортивный таймер...', u'Пора позаниматься!!!', qg.QSystemTrayIcon.Information, 2000)
		
	def newSportTimer(self):
		self._sportTimer = SportTimer(self.set.spinBoxSessionMinutes.value() - 1, 59, self.OnCountdown)
		
	def start_button(self):
		self.Timer1 = self.startTimer(1000)
# 		if(self.Timer1.is_active()):
# 			self.Timer1.stop()
# 		else:
# 			self.Timer1.start()
		
	def timerEvent(self, *args, **kwargs):
		self._sportTimer.dec()
		self.lcdNumberTime.display(str(self._sportTimer))
		return QMainWindow.timerEvent(self, *args, **kwargs)
		
	def settings(self):
		self.set.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()
