
import sys
from PySide.QtGui import QMainWindow, QPushButton, QApplication, QDialog, QWidget
from PySide.QtCore import QObject

from ui_mainwindow import Ui_MainWindow
from ui_settings import Ui_SettingsWindow

class SettingsWindow(QWidget, Ui_SettingsWindow):
	def __init__(self, parent=None):
		super(SettingsWindow, self).__init__(parent)
		self.ui = Ui_SettingsWindow()
		self.setupUi(self)
		
		print "settings window ctor"

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.setupUi(self)
		
		self.SettingsAction.triggered.connect(self.settings)
		
		self.set = SettingsWindow()
		
	def settings(self):
		print "settings"
		self.set.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()