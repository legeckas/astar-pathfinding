# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'astar-pathfinding/astar_pathfinding_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 957)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.node_frame = QtWidgets.QFrame(self.centralwidget)
        self.node_frame.setGeometry(QtCore.QRect(0, 0, 760, 760))
        self.node_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.node_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.node_frame.setObjectName("node_frame")
        self.ready_button_frame = QtWidgets.QFrame(self.centralwidget)
        self.ready_button_frame.setGeometry(QtCore.QRect(0, 760, 760, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.ready_button_frame.setFont(font)
        self.ready_button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ready_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ready_button_frame.setLineWidth(0)
        self.ready_button_frame.setObjectName("ready_button_frame")
        self.readyButton = QtWidgets.QPushButton(self.ready_button_frame)
        self.readyButton.setGeometry(QtCore.QRect(340, 0, 80, 23))
        self.readyButton.setObjectName("readyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.readyButton.setText(_translate("MainWindow", "READY!"))
