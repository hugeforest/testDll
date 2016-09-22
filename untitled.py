# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(215, 207)
        self.button_hook = QtWidgets.QPushButton(Form)
        self.button_hook.setGeometry(QtCore.QRect(9, 29, 75, 23))
        self.button_hook.setObjectName("button_hook")
        self.button_stop = QtWidgets.QPushButton(Form)
        self.button_stop.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.button_stop.setObjectName("button_stop")
        self.button_start = QtWidgets.QPushButton(Form)
        self.button_start.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.button_start.setObjectName("button_start")
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(120, 160, 75, 23))
        self.quit.setObjectName("quit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.button_hook.raise_()
        self.button_start.raise_()
        self.quit.raise_()
        self.button_stop.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(Form)
        self.quit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MyWindow"))
        self.button_hook.setText(_translate("Form", "Hook"))
        self.button_stop.setText(_translate("Form", "Stop"))
        self.button_start.setText(_translate("Form", "Start"))
        self.quit.setText(_translate("Form", "Quit"))

