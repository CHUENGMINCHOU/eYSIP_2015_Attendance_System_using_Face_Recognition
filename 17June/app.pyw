import os
import platform
import sys				#for sys.argv[]
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import helpform
import newimagedlg
import qrc_resources

__version__ = "1.0.0"

class MainWindow(QMainWindow):
	def __int__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.image = QImage()
		self.dirty = False
		self.filename = None
		self.mirroredvertically = None
		self.mirroredhorizontally None

		
