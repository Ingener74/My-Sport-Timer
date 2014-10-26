
import sys
from PySide.QtGui import QMainWindow, QPushButton, QApplication

from ui_mainwindow import Ui_MainWindow
from ui_settings import Ui_SettingsWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		
		#self.SettingsAction.triggered.connect()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	frame = MainWindow()
	frame.show()
	app.exec_()