import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):							#example class derived from the base class QWidge, so 2 construtors
	def __init__(self):							#constructor method for the example class
		super(Example,self).__init__()					#super method provides parental control to  Example class
		self.initUI()							#object to the function

	def initUI(self):							#function
		'''btn = QtGui.QPushButton('Quit',self)		
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(btn.sizeHint())
		btn.move(50,50)'''				
		self.setGeometry(300,300,500,700)				#combines move nad resize 
		self.setWindowTitle('Attendance Auto-logging System')		#name
		self.setWindowIcon(QtGui.QIcon('index.jpeg'))			#add image as an icon
		self.show()							#display

def main():									#main function	
	app = QtGui.QApplication(sys.argv)					#creating application object
	ex = Example()								#call to the class example
	sys.exit(app.exec_())							#clean exit

if __name__ == '__main__':
	main()	
