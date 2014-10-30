#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json
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
	def __init__(self, mainWindow, parent=None):
		super(SettingsWindow, self).__init__(parent)
		self.setupUi(self)
		
		self._json_data = json.load(open("config.json"))
		
		self.spinBoxSessionMinutes.setValue(int(self._json_data["session_minutes"]))
		self.spinBoxTouchMinutes.setValue(int(self._json_data["touch_minutes"]))
		self.spinBoxTouchSeconds.setValue(int(self._json_data["touch_seconds"]))
		
		self.spinBoxSessionMinutes.connect(SIGNAL('valueChanged(int)'), self.sessionMinutesValueChanged)
		self.spinBoxSessionMinutes.connect(SIGNAL('valueChanged(int)'), mainWindow.changeLCD)
		
		self.spinBoxTouchMinutes.connect(SIGNAL('valueChanged(int)'), self.touchMinutesValueChanged)
		
		self.spinBoxTouchSeconds.connect(SIGNAL('valueChanged(int)'), self.touchSecondsValueChanged)
		
	def saveToJson(self, key, val):
		self._json_data[key] = val
		with open("config.json", "w") as json_file:
			json.dump(self._json_data, json_file, sort_keys=True, indent=4, separators=(',', ':'))
		
	def sessionMinutesValueChanged(self, val):
		self.saveToJson("session_minutes", val)
			
	def touchMinutesValueChanged(self, val):
		self.saveToJson("touch_minutes", val)
		
	def touchSecondsValueChanged(self, val):
		self.saveToJson("touch_seconds", val)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		
		self.SettingsAction.triggered.connect(self.settings)
# 		self.ExitAction.triggered.connect(self.quit_)
		
		self._settingsWindow = SettingsWindow(self)
		
		self.changeLCD()
		
		self.pushButtonStart.connect(SIGNAL('clicked()'), self.start_button)
		
	def changeLCD(self):
		self.newSportTimer()
		self.lcdNumberTime.display(str(self._sportTimer))
		
	def OnCountdown(self):
		self.newSportTimer()
		QSound('data/bell.wav').play()
#		self.TrayIcon.showMessage(u'Спортивный таймер...', u'Пора позаниматься!!!', qg.QSystemTrayIcon.Information, 2000)
		
	def newSportTimer(self):
		self._sportTimer = SportTimer(self._settingsWindow.spinBoxSessionMinutes.value() - 1, 59, self.OnCountdown)
		
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
		self._settingsWindow.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()
