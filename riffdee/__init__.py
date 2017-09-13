#!/usr/bin/python
#coding:utf-8
# Author:  Dan-Erik Lindberg -- <riffdee@dan-erik.com>
# Created: 2012-07-12
# License: GPL-3

import sys
from PyQt4 import QtCore, QtGui

from riffdeewindow import Ui_RiffDee
from RiffDeeMega import *
from RiffDeeSingle import *
from RiffDeeTag import *

#
#   Main window class is where it all begins
#
class MainDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_RiffDee()
        self.ui.setupUi(self)

        #
        #   Connect buttons to windows
        #
        QtCore.QObject.connect(self.ui.btnTag, QtCore.SIGNAL('clicked()'), self.showtag)
        QtCore.QObject.connect(self.ui.btnSingle, QtCore.SIGNAL('clicked()'), self.showsingle)
        QtCore.QObject.connect(self.ui.btnMega, QtCore.SIGNAL('clicked()'), self.showmega)

        #
        #   Automatic startup of certain applications
        #
        if "Tag" in sys.argv or "tag" in sys.argv:
            self.showtag()
        if "Single" in sys.argv or "single" in sys.argv:
            self.showsingle()
        if "Mega" in sys.argv or "mega" in sys.argv:
            self.showmega()

        def showtag(self):
            t_win = TagWindow(self)
            t_win.show()

        def showsingle(self):
            s_win = SingleWindow(self)
            s_win.show()

        def showmega(self):
            m_win = MegaWindow(self)
            m_win.show()


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainDialog()
    form.show()
    sys.exit(app.exec_())
