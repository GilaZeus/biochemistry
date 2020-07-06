# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\git\biochemistry\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 776, 516))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.molecule = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.molecule.setGeometry(QtCore.QRect(10, 40, 311, 401))
        self.molecule.setObjectName("molecule")
        self.plus = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.plus.setGeometry(QtCore.QRect(290, 180, 31, 61))
        self.plus.setObjectName("plus")
        self.enzyme = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.enzyme.setGeometry(QtCore.QRect(340, 90, 261, 181))
        self.enzyme.setObjectName("enzyme")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.open_chain)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "open"))
        self.molecule.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/pictures/Glucose.png\"/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Glucose</span></p></body></html>"))
        self.plus.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">+</span></p></body></html>"))
        self.enzyme.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">Enzyme_name</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">————————&gt;</span></p></body></html>"))
