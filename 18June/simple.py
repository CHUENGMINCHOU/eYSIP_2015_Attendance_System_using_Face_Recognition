import sys
from PyQt4 import QtGui

def main():

	app = QtGui.QApplication(sys.argv)	#creating an application object, sys.arg = list of parameters from command line
	w = QtGui.QWidget()			#base class for all user interface object, creates constructor, it is a default constructor and 						 has no parent, hence called window
	w.resize(2500,1500)			#resizes the window (width,height) in px.
	w.move(0,0)				#moves screen to the (x,y) co-ordinates of the screen
	w.setWindowTitle('Attendance Auto-Logging System')		#name to the window
	w.show()				#display the window
	
	sys.exit(app.exec_())			#clean exit from the main

if __name__ == '__main__':
	main()
	
