#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from untitled import Ui_Form
from my_an import *
import threading

global hwnd
hwnd=0

class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.button_hook.clicked.connect(button_hook_clicked)
        self.button_stop.clicked.connect(button_stop_clicked)
        self.button_start.clicked.connect(button_start_clicked)
        self.quit.clicked.connect(self.quit_clicked)

    def mybutton_clicked(self):
        x=self.lineEdit.text()
        self.lineEdit.setText("ok")
        print(x)

    def quit_clicked(self):
        print("hooked quit")


def button_hook_clicked():
    x=myshow.lineEdit.text()
    if x == "":
        return
    if isinstance(x,str):
        print("str")
        return
    x=int(x)
    if not isinstance(x,int):
        pass
        return
    fake_window(x)
    print("Hooked")


def button_stop_clicked():
    x=myshow.lineEdit.text()
    print(x)
    if x == "":
        print("x")
        return
    x=int(x)
    print("s")
    if not isinstance(x,int):
        print("not int")
        return
    global hwnd
    hwnd=x
    restore_window(x)
    print("stopped!")


def thread_run():
    pass


def button_start_clicked():
    global hwnd
    print(hwnd)



if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())

