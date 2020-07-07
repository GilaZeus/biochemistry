# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\git\biochemistry\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PIL import Image
import importlib
import shutil
import chain_to_import


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        importlib.reload(chain_to_import)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 776, 516))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.labels = []
        self.hbox = QtWidgets.QHBoxLayout()
        self.create_labels(chain_to_import.chain)
        for label in self.labels:
            self.hbox.addWidget(label[0])
        self.scrollAreaWidgetContents_2.setLayout(self.hbox)

        '''self.molecule = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.molecule.setGeometry(QtCore.QRect(10, 40, 311, 401))
        self.molecule.setObjectName("molecule")
        
        self.plus = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.plus.setGeometry(QtCore.QRect(290, 180, 31, 61))
        self.plus.setObjectName("plus")
        
        self.enzyme = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.enzyme.setGeometry(QtCore.QRect(340, 90, 261, 181))
        self.enzyme.setObjectName("enzyme")'''
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def create_labels(self, chain):
        x = 10
        for reaction in chain:
            for educt in reaction.educts:
                label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
                img = Image.open(educt.image)
                width, height = img.size
                if 64 * len(educt.name) > width:
                    width = 64 * len(educt.name)
                label.setGeometry(QtCore.QRect(x, 40, width, height + 50))
                label.setObjectName(educt.name)
                text = "<html><head/><body><p align=\"center\"><img src=\"" + \
                       educt.image + "\"/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">" + \
                       educt.name + "</span></p></body></html>"
                self.labels.append([label, text])
                x += width + 10
                if reaction.educts.index(educt) != len(reaction.educts) - 1:
                    label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
                    label.setGeometry(QtCore.QRect(x, 40, 50, 50))
                    label.setObjectName('plus')
                    text = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">+</span></p></body></html>"
                    self.labels.append([label, text])
                    x += 300
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            width = 48 * len(reaction.name) + 50
            label.setGeometry(QtCore.QRect(x, 40, width, 401))
            label.setObjectName(reaction.name)
            text = "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">" + \
                   reaction.name + "</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">————————&gt;</span></p></body></html>"
            self.labels.append([label, text])
            x += width
        
        for product in chain.chain[-1].products:
            img = Image.open(product.image)
            width, height = img.size
            if 64 * len(product.name) > width:
                width = 64 * len(product.name)    
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            label.setGeometry(QtCore.QRect(x, 40, width, height + 50))
            label.setObjectName(product.name)
            text = "<html><head/><body><p align=\"center\"><img src=\"" + \
                   product.image + "\"/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">" + \
                   product.name + "</span></p></body></html>"
            self.labels.append([label, text])
            x += width + 10
            if reaction.products.index(product) != len(reaction.products) - 1:
                label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
                label.setGeometry(QtCore.QRect(x, 40, 50, 50))
                label.setObjectName('plus')
                text = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">+</span></p></body></html>"
                self.labels.append([label, text])
                x += 300


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        for label in self.labels:
            label[0].setText(_translate("MainWindow", label[1]))