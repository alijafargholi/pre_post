# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectedInfo.ui'
#
# Created: Mon Mar 24 00:08:42 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_currentInfo(object):
    def setupUi(self, currentInfo):
        currentInfo.setObjectName(_fromUtf8("currentInfo"))
        currentInfo.resize(389, 286)
        self.gridLayout = QtGui.QGridLayout(currentInfo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(currentInfo)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(currentInfo)
        QtCore.QMetaObject.connectSlotsByName(currentInfo)

    def retranslateUi(self, currentInfo):
        currentInfo.setWindowTitle(_translate("currentInfo", "Form", None))

