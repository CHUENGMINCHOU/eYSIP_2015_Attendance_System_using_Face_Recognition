# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created: Thu Jul  2 01:20:20 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from recognizer import *
from final6 import *
import sys
import threading
import datetime
import myResources_rc
from excel import *
from mySerial import *

entryDetections = []
exitDetections = []

entryN = 0
exitN = 0

threshold = 4

entryDetection = "Name: ----"
exitDetection = ""
entryLastDetection = ""
exitLastDetection = ""
entryTime = ""
exitTime = ""
entryImage = "./pics/unknown.jpg"
exitImage = "./pics/unknown.jpg"
entryFailure = 0
exitFailure = 0
time = ""
entryLastDetected = 0
exitLastDetected = 0


for i in range(12):
    entryDetections.append(0)

for i in range(12):
    exitDetections.append(0)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    
    camera1 = cv2.VideoCapture(0)
    camera2 = cv2.VideoCapture(1)
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        init_recognizer()
        
        QtCore.QTimer.singleShot(10, self.timer_func)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Downloads/index.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(37.0)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(./pics/bg10.jpg);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ExitStream = QtGui.QLabel(self.centralwidget)
        self.ExitStream.setGeometry(QtCore.QRect(440, 70, 320, 240))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ExitStream.setFont(font)
        self.ExitStream.setFrameShape(QtGui.QFrame.Box)
        self.ExitStream.setFrameShadow(QtGui.QFrame.Plain)
        self.ExitStream.setLineWidth(10)
        self.ExitStream.setText(_fromUtf8(""))
        self.ExitStream.setPixmap(QtGui.QPixmap(_fromUtf8("./pics/c1.jpg")))
        self.ExitStream.setScaledContents(True)
        self.ExitStream.setObjectName(_fromUtf8("ExitStream"))
        self.EntryImage = QtGui.QLabel(self.centralwidget)
        self.EntryImage.setGeometry(QtCore.QRect(25, 330, 150, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.EntryImage.setFont(font)
        self.EntryImage.setStyleSheet(_fromUtf8(""))
        self.EntryImage.setText(_fromUtf8(""))
        self.EntryImage.setPixmap(QtGui.QPixmap(_fromUtf8("./pics/unknown.jpg")))
        self.EntryImage.setScaledContents(True)
        self.EntryImage.setObjectName(_fromUtf8("EntryImage"))
        self.ExitImage = QtGui.QLabel(self.centralwidget)
        self.ExitImage.setGeometry(QtCore.QRect(420, 330, 150, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ExitImage.setFont(font)
        self.ExitImage.setStyleSheet(_fromUtf8("image: url(:/pics/none.png);"))
        self.ExitImage.setText(_fromUtf8(""))
        self.ExitImage.setPixmap(QtGui.QPixmap(_fromUtf8("./pics/unknown.jpg")))
        self.ExitImage.setScaledContents(True)
        self.ExitImage.setObjectName(_fromUtf8("ExitImage"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 500, 121, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 500, 111, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.LastEntry = QtGui.QLabel(self.centralwidget)
        self.LastEntry.setGeometry(QtCore.QRect(161, 500, 240, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LastEntry.setFont(font)
        self.LastEntry.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.LastEntry.setObjectName(_fromUtf8("LastEntry"))
        self.LastExit = QtGui.QLabel(self.centralwidget)
        self.LastExit.setGeometry(QtCore.QRect(551, 500, 240, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LastExit.setFont(font)
        self.LastExit.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.LastExit.setObjectName(_fromUtf8("LastExit"))
        self.EntryID = QtGui.QLabel(self.centralwidget)
        self.EntryID.setGeometry(QtCore.QRect(180, 380, 200, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.EntryID.setFont(font)
        self.EntryID.setFocusPolicy(QtCore.Qt.NoFocus)
        self.EntryID.setAutoFillBackground(False)
        self.EntryID.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.EntryID.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.EntryID.setObjectName(_fromUtf8("EntryID"))
        self.EntryTime = QtGui.QLabel(self.centralwidget)
        self.EntryTime.setGeometry(QtCore.QRect(180, 420, 200, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.EntryTime.setFont(font)
        self.EntryTime.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.EntryTime.setObjectName(_fromUtf8("EntryTime"))
        self.ExitName = QtGui.QLabel(self.centralwidget)
        self.ExitName.setGeometry(QtCore.QRect(585, 340, 200, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ExitName.setFont(font)
        self.ExitName.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.ExitName.setObjectName(_fromUtf8("ExitName"))
        self.ExitID = QtGui.QLabel(self.centralwidget)
        self.ExitID.setGeometry(QtCore.QRect(585, 380, 200, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ExitID.setFont(font)
        self.ExitID.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.ExitID.setObjectName(_fromUtf8("ExitID"))
        self.ExitTime = QtGui.QLabel(self.centralwidget)
        self.ExitTime.setGeometry(QtCore.QRect(585, 420, 200, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ExitTime.setFont(font)
        self.ExitTime.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.ExitTime.setObjectName(_fromUtf8("ExitTime"))
        self.EntryStream = QtGui.QLabel(self.centralwidget)
        self.EntryStream.setGeometry(QtCore.QRect(30, 70, 320, 240))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.EntryStream.setFont(font)
        self.EntryStream.setStyleSheet(_fromUtf8("background-image: url(./pics/bg1.jpeg);"))
        self.EntryStream.setFrameShape(QtGui.QFrame.Box)
        self.EntryStream.setFrameShadow(QtGui.QFrame.Plain)
        self.EntryStream.setLineWidth(10)
        self.EntryStream.setMidLineWidth(7)
        self.EntryStream.setText(_fromUtf8(""))
        self.EntryStream.setPixmap(QtGui.QPixmap(_fromUtf8("./pics/c1.jpg")))
        self.EntryStream.setScaledContents(True)
        self.EntryStream.setObjectName(_fromUtf8("EntryStream"))
        self.Time = QtGui.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(530, 20, 230, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.Time.setObjectName(_fromUtf8("Time"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setMargin(3)
        self.label.setIndent(2)
        self.label.setObjectName(_fromUtf8("label"))
        self.EntryName = QtGui.QLabel(self.centralwidget)
        self.EntryName.setGeometry(QtCore.QRect(180, 340, 200, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.EntryName.setFont(font)
        self.EntryName.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border-image: url(./pics/fg1.jpg);"))
        self.EntryName.setObjectName(_fromUtf8("EntryName"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuEnable_Worksheet_Editing = QtGui.QMenu(self.menuEdit)
        self.menuEnable_Worksheet_Editing.setObjectName(_fromUtf8("menuEnable_Worksheet_Editing"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet(_fromUtf8("font: 75 bold 12pt \"Purisa\";\n"
"color: rgb(255, 255, 255);"))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Worksheet = QtGui.QAction(MainWindow)
        self.actionOpen_Worksheet.setObjectName(_fromUtf8("actionOpen_Worksheet"))
        self.actionMinimize_Maximize = QtGui.QAction(MainWindow)
        self.actionMinimize_Maximize.setObjectName(_fromUtf8("actionMinimize_Maximize"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionEnable_Entry_Live_Stream = QtGui.QAction(MainWindow)
        self.actionEnable_Entry_Live_Stream.setObjectName(_fromUtf8("actionEnable_Entry_Live_Stream"))
        self.actionEnable_Exit_Livestream = QtGui.QAction(MainWindow)
        self.actionEnable_Exit_Livestream.setObjectName(_fromUtf8("actionEnable_Exit_Livestream"))
        self.actionAdd_Create_Database = QtGui.QAction(MainWindow)
        self.actionAdd_Create_Database.setObjectName(_fromUtf8("actionAdd_Create_Database"))
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionEntry_Live_Stream = QtGui.QAction(MainWindow)
        self.actionEntry_Live_Stream.setObjectName(_fromUtf8("actionEntry_Live_Stream"))
        self.actionExit_Live_Stream = QtGui.QAction(MainWindow)
        self.actionExit_Live_Stream.setObjectName(_fromUtf8("actionExit_Live_Stream"))
        self.actionEntry_data = QtGui.QAction(MainWindow)
        self.actionEntry_data.setObjectName(_fromUtf8("actionEntry_data"))
        self.actionExit_Data = QtGui.QAction(MainWindow)
        self.actionExit_Data.setObjectName(_fromUtf8("actionExit_Data"))
        self.actionAppearance = QtGui.QAction(MainWindow)
        self.actionAppearance.setObjectName(_fromUtf8("actionAppearance"))
        self.actionAdditional_Fonts = QtGui.QAction(MainWindow)
        self.actionAdditional_Fonts.setObjectName(_fromUtf8("actionAdditional_Fonts"))
        self.actionAbout_Eyantra = QtGui.QAction(MainWindow)
        self.actionAbout_Eyantra.setObjectName(_fromUtf8("actionAbout_Eyantra"))
        self.actionAbout_Attendance_System = QtGui.QAction(MainWindow)
        self.actionAbout_Attendance_System.setObjectName(_fromUtf8("actionAbout_Attendance_System"))
        self.actionCopyright = QtGui.QAction(MainWindow)
        self.actionCopyright.setObjectName(_fromUtf8("actionCopyright"))
        self.actionLogout = QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.menuFile.addAction(self.actionOpen_Worksheet)
        self.menuFile.addAction(self.actionMinimize_Maximize)
        self.menuFile.addAction(self.actionClose)
        self.menuEnable_Worksheet_Editing.addAction(self.actionLogin)
        self.menuEnable_Worksheet_Editing.addAction(self.actionLogout)
        self.menuEdit.addAction(self.actionAdd_Create_Database)
        self.menuEdit.addAction(self.menuEnable_Worksheet_Editing.menuAction())
        self.menuView.addAction(self.actionEntry_Live_Stream)
        self.menuView.addAction(self.actionExit_Live_Stream)
        self.menuView.addAction(self.actionEntry_data)
        self.menuView.addAction(self.actionExit_Data)
        self.menuSettings.addAction(self.actionAppearance)
        self.menuSettings.addAction(self.actionAdditional_Fonts)
        self.menuHelp.addAction(self.actionAbout_Eyantra)
        self.menuHelp.addAction(self.actionAbout_Attendance_System)
        self.menuHelp.addAction(self.actionCopyright)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Autologging Attendance System", None))
        self.ExitStream.setStatusTip(_translate("MainWindow", "Live Stream Exit Video", None))
        self.EntryImage.setStatusTip(_translate("MainWindow", "Detection at the Entrance", None))
        self.ExitImage.setStatusTip(_translate("MainWindow", "Detection at the Exit", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">LAST ENTRY:</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">LAST EXIT:</span></p></body></html>", None))
        self.LastEntry.setStatusTip(_translate("MainWindow", "Last entry", None))
        self.LastEntry.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.LastExit.setStatusTip(_translate("MainWindow", "Last exit", None))
        self.LastExit.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.EntryID.setStatusTip(_translate("MainWindow", "Entry ID", None))
        self.EntryID.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.EntryTime.setStatusTip(_translate("MainWindow", "Entry Time", None))
        self.EntryTime.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.ExitName.setStatusTip(_translate("MainWindow", "Exit Name", None))
        self.ExitName.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.ExitID.setStatusTip(_translate("MainWindow", "Exit ID", None))
        self.ExitID.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.ExitTime.setStatusTip(_translate("MainWindow", "Exit Time", None))
        self.ExitTime.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.EntryStream.setStatusTip(_translate("MainWindow", "Live Stream Entry Video", None))
        self.Time.setStatusTip(_translate("MainWindow", "Current Time", None))
        self.Time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">HH:MM:SS</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Live Stream", None))
        self.EntryName.setStatusTip(_translate("MainWindow", "Entry Name", None))
        self.EntryName.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.menubar.setStatusTip(_translate("MainWindow", "Menubar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuEnable_Worksheet_Editing.setTitle(_translate("MainWindow", "Enable Worksheet Editing", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.statusbar.setStatusTip(_translate("MainWindow", "Status Bar", None))
        self.actionOpen_Worksheet.setText(_translate("MainWindow", "Open Worksheet", None))
        self.actionMinimize_Maximize.setText(_translate("MainWindow", "Minimize/Maximize", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionEnable_Entry_Live_Stream.setText(_translate("MainWindow", "Enable Entry Live Stream", None))
        self.actionEnable_Exit_Livestream.setText(_translate("MainWindow", "Enable Exit Livestream", None))
        self.actionAdd_Create_Database.setText(_translate("MainWindow", "Add/Create Database", None))
        self.actionLogin.setText(_translate("MainWindow", "Login", None))
        self.actionEntry_Live_Stream.setText(_translate("MainWindow", "Entry Live Stream", None))
        self.actionExit_Live_Stream.setText(_translate("MainWindow", "Exit Live Stream", None))
        self.actionEntry_data.setText(_translate("MainWindow", "Entry data", None))
        self.actionExit_Data.setText(_translate("MainWindow", "Exit Data", None))
        self.actionAppearance.setText(_translate("MainWindow", "Appearance", None))
        self.actionAdditional_Fonts.setText(_translate("MainWindow", "Additional Fonts", None))
        self.actionAbout_Eyantra.setText(_translate("MainWindow", "About Eyantra", None))
        self.actionAbout_Attendance_System.setText(_translate("MainWindow", "About Attendance System", None))
        self.actionCopyright.setText(_translate("MainWindow", "Copyright", None))
        self.actionLogout.setText(_translate("MainWindow", "Logout", None))

    def timer_func(self):
        ret, frame1 = self.camera1.read(0)
        cv2.imwrite("image1.jpg", frame1)
        
        ret, frame2 = self.camera2.read(0)
        cv2.imwrite("image2.jpg", frame2)
        
        self.EntryStream.setPixmap(QtGui.QPixmap(_fromUtf8("./image1.jpg")))
        self.ExitStream.setPixmap(QtGui.QPixmap(_fromUtf8("./image2.jpg")))
        
        #If only main thread is running
        if threading.active_count() == 1 :
            #threadEntry = RecognizerClass1(frame1)
            threadExit = RecognizerClass2(frame2)
            #threadEntry.start()
            threadExit.start()
        
        '''
        else:
            threadList = threading.enumerate()
            
            #If threadEntry is running, start threadExit
            if "threadEntry" in threadList:
                threadExit = RecognizerClass2(frame2)
                threadExit.start()
                
            #If threadExit is running, start threadEntry
            elif "threadExit" in threadList:
                threadEntry = RecognizerClass1(frame1)
                threadEntry.start()
                
        '''
        
        time = datetime.datetime.now().strftime("%d %b, %Y : %H:%M:%S")
        self.Time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\"> " + time + "</span></p></body></html>", None))
        
        self.EntryName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">" + entryDetection +"</span></p></body></html>", None))
        self.EntryImage.setPixmap(QtGui.QPixmap(_fromUtf8(entryImage)))
        self.EntryTime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">" + entryTime +"</span></p></body></html>", None))
        self.LastEntry.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">" + entryLastDetection +"</span></p></body></html>", None))
        
        self.ExitName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">" + exitDetection +"</span></p></body></html>", None))
        self.ExitImage.setPixmap(QtGui.QPixmap(_fromUtf8(exitImage)))
        self.ExitTime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">" + exitTime +"</span></p></body></html>", None))
        self.LastExit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">" + exitLastDetection + "</span></p></body></html>", None))
            
        QtCore.QTimer.singleShot(0, self.timer_func)
            
    if __name__ == '__main__':    	
    	app = QtGui.QApplication(sys.argv)
    	ex = Ui_MainWindow()
    	ex.show()
    	out = app.exec_()  
    	camera1.release()
        camera2.release()        
        close_excel()
        closeSerial()
        sys.exit(out)
        
class RecognizerClass1(threading.Thread):
        
    def __init__(self, input_frame):
        threading.Thread.__init__(self)
        self.__frame = input_frame
        
        
    def run(self):
        global entryN
        global entryDetection, entryTime, entryImage
        global entryFailure
        global entryLastDetected, entryLastDetection
        
        label = get_label_2(self.__frame)
        print "1 : {}".format(label_to_name(label))
        print "1 : {}".format(entryN)
            
            
        entryDetections[label] = entryDetections[label] + 1
        entryN = entryN + 1        
        if entryN > 10:
            entryN = 0
            entryDetectedLabel = findMax(entryDetections)
            
            if entryDetectedLabel == 0 :
                if entryDetections[entryDetectedLabel] > 5:
                    entryDetection = "Name : ------"
                    entryImage = "./pics/unknown.jpg"
                    entryTime = "Entry: ------"
                    
                    redOn()
                    greenOff()
                
                else : 
                    entryDetectedLabel = findMax2(entryDetections)
                    
            if entryDetectedLabel != entryLastDetected and entryDetectedLabel != 0 and entryDetected != 11:

                redOff()
                greenOn()
                
                print label_to_name(entryDetectedLabel), " is detected"
                entryDetection = "Name: " + label_to_name (entryDetectedLabel)
                entryTime = "Entry: " + datetime.datetime.now().strftime("%I:%M %p")
                if entryDetectedLabel < 10:
                    entryImage = "./displayImages/subject0" + str(entryDetectedLabel) + "_smile.jpg"
                else:
                    entryImage = "./displayImages/subject" + str(entryDetectedLabel) + "_smile.jpg"
                
                if entryLastDetected != 0:
                    entryLastDetection = label_to_name (entryLastDetected)
                
                #new_entry(label_to_name (entryDetectedLabel), 10, datetime.datetime.now().strftime("%I:%M %p"))
                
                save_excel()
                
            for i in range(12):
                entryDetections[i] = 0
                    
            entryLastDetected = entryDetectedLabel
            
            
class RecognizerClass2(threading.Thread):
        
    def __init__(self, input_frame):
        threading.Thread.__init__(self)
        self.__frame = input_frame
        
        
    def run(self):
        global exitN
        global exitDetection, exitTime, exitImage
        global exitFailure
        global exitLastDetected, exitLastDetection
        
        label = get_label_2(self.__frame)
        print "2 : {}".format(label_to_name(label))
        print "2 : {}".format(exitN)
        
        exitDetections[label] = exitDetections[label] + 1
        exitN = exitN + 1        
        if exitN > 10:
            exitN = 0
            exitDetectedLabel = findMax(exitDetections)
            
            if exitDetectedLabel == 11:
                cv2.imwrite("./UnknownFaces/" + datetime.datetime.now().strftime("%I:%M") + ".jpg", self.__frame)
            elif exitDetectedLabel == 0:
                if exitDetections[exitDetectedLabel] > 5:
                    exitDetection = "Name : ------"
                    exitImage = "./pics/unknown.jpg"
                    exitTime = "Exit: ------"
                
                    redOn()
                    greenOff()
                
                else:
                    exitDetectedLabel = findMax2(exitDetections)
            
            if exitDetectedLabel != exitLastDetected and exitDetectedLabel != 0:
                print label_to_name(exitDetectedLabel), " is detected"
                exitDetection = "Name: " + label_to_name (exitDetectedLabel)
                exitTime = "Exit: " + datetime.datetime.now().strftime("%I:%M %p")
                if exitDetectedLabel < 10:
                    exitImage = "./displayImages/subject0" + str(exitDetectedLabel) + "_smile.jpg"
                else:
                    exitImage = "./displayImages/subject" + str(exitDetectedLabel) + "_smile.jpg"
                
                new_entry(label_to_name (exitDetectedLabel), 10, datetime.datetime.now().strftime("%I:%M %p"))
                
                if exitLastDetected != 0:
                    exitLastDetection = label_to_name (exitLastDetected)
                
                redOff()
                greenOn()
                
            for i in range(12):
                exitDetections[i] = 0
                    
            exitLastDetected = exitDetectedLabel
          
                
                
def findMax(array):
    maxIndex = 0
    i = 1
    while i < 12:
        if array[i] > array[maxIndex]:
            maxIndex = i
        i = i + 1
    return maxIndex

def findMax2(array):
    maxIndex = 1
    i = 2
    while i < 12:
        if array[i] > array[maxIndex]:
            maxIndex = i
        i = i + 1
    return maxIndex
