# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'submit_note_v01.ui'
#
# Created: Tue Mar 18 21:06:06 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(773, 430)
        Form.setMinimumSize(QtCore.QSize(600, 430))
        Form.setMaximumSize(QtCore.QSize(800, 423))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.userLabel = QtGui.QLabel(Form)
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.verticalLayout_3.addWidget(self.userLabel)
        self.dateLabel = QtGui.QLabel(Form)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.verticalLayout_3.addWidget(self.dateLabel)
        self.timeLabel = QtGui.QLabel(Form)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.verticalLayout_3.addWidget(self.timeLabel)
        self.projectLabel = QtGui.QLabel(Form)
        self.projectLabel.setObjectName(_fromUtf8("projectLabel"))
        self.verticalLayout_3.addWidget(self.projectLabel)
        self.programLabel = QtGui.QLabel(Form)
        self.programLabel.setObjectName(_fromUtf8("programLabel"))
        self.verticalLayout_3.addWidget(self.programLabel)
        self.scenNameLabel = QtGui.QLabel(Form)
        self.scenNameLabel.setObjectName(_fromUtf8("scenNameLabel"))
        self.verticalLayout_3.addWidget(self.scenNameLabel)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.userSpace = QtGui.QLineEdit(Form)
        self.userSpace.setReadOnly(True)
        self.userSpace.setObjectName(_fromUtf8("userSpace"))
        self.verticalLayout.addWidget(self.userSpace)
        self.dateSpace = QtGui.QLineEdit(Form)
        self.dateSpace.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dateSpace.setObjectName(_fromUtf8("dateSpace"))
        self.verticalLayout.addWidget(self.dateSpace)
        self.timeSpace = QtGui.QLineEdit(Form)
        self.timeSpace.setObjectName(_fromUtf8("timeSpace"))
        self.verticalLayout.addWidget(self.timeSpace)
        self.projectSpace = QtGui.QLineEdit(Form)
        self.projectSpace.setObjectName(_fromUtf8("projectSpace"))
        self.verticalLayout.addWidget(self.projectSpace)
        self.projectWidget = QtGui.QListWidget(Form)
        self.projectWidget.setObjectName(_fromUtf8("projectWidget"))
        item = QtGui.QListWidgetItem()
        self.projectWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.projectWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.projectWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.projectWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.projectWidget.addItem(item)
        self.verticalLayout.addWidget(self.projectWidget)
        self.sceneNameSpace = QtGui.QLineEdit(Form)
        self.sceneNameSpace.setObjectName(_fromUtf8("sceneNameSpace"))
        self.verticalLayout.addWidget(self.sceneNameSpace)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.snapShotPushButton = QtGui.QPushButton(Form)
        self.snapShotPushButton.setMinimumSize(QtCore.QSize(0, 180))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/snapshot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snapShotPushButton.setIcon(icon)
        self.snapShotPushButton.setIconSize(QtCore.QSize(64, 64))
        self.snapShotPushButton.setObjectName(_fromUtf8("snapShotPushButton"))
        self.verticalLayout_4.addWidget(self.snapShotPushButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.submitNoteButton = QtGui.QPushButton(Form)
        self.submitNoteButton.setMinimumSize(QtCore.QSize(0, 40))
        self.submitNoteButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 166, 0)\n"
""))
        self.submitNoteButton.setObjectName(_fromUtf8("submitNoteButton"))
        self.horizontalLayout.addWidget(self.submitNoteButton)
        self.cancelButton = QtGui.QPushButton(Form)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 40))
        self.cancelButton.setStyleSheet(_fromUtf8("background-color:rgb(166, 0, 0)"))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.subjectLabel = QtGui.QLabel(Form)
        self.subjectLabel.setObjectName(_fromUtf8("subjectLabel"))
        self.verticalLayout_2.addWidget(self.subjectLabel)
        self.subjectSpace = QtGui.QLineEdit(Form)
        self.subjectSpace.setObjectName(_fromUtf8("subjectSpace"))
        self.verticalLayout_2.addWidget(self.subjectSpace)
        self.tagLabel_3 = QtGui.QLabel(Form)
        self.tagLabel_3.setObjectName(_fromUtf8("tagLabel_3"))
        self.verticalLayout_2.addWidget(self.tagLabel_3)
        self.descriptionSpace = QtGui.QPlainTextEdit(Form)
        self.descriptionSpace.setPlainText(_fromUtf8(""))
        self.descriptionSpace.setObjectName(_fromUtf8("descriptionSpace"))
        self.verticalLayout_2.addWidget(self.descriptionSpace)
        self.tagLabel_2 = QtGui.QLabel(Form)
        self.tagLabel_2.setObjectName(_fromUtf8("tagLabel_2"))
        self.verticalLayout_2.addWidget(self.tagLabel_2)
        self.warningSpace = QtGui.QPlainTextEdit(Form)
        self.warningSpace.setObjectName(_fromUtf8("warningSpace"))
        self.verticalLayout_2.addWidget(self.warningSpace)
        self.tagLabel = QtGui.QLabel(Form)
        self.tagLabel.setObjectName(_fromUtf8("tagLabel"))
        self.verticalLayout_2.addWidget(self.tagLabel)
        self.tagSpace = QtGui.QLineEdit(Form)
        self.tagSpace.setObjectName(_fromUtf8("tagSpace"))
        self.verticalLayout_2.addWidget(self.tagSpace)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.subjectSpace, self.descriptionSpace)
        Form.setTabOrder(self.descriptionSpace, self.warningSpace)
        Form.setTabOrder(self.warningSpace, self.tagSpace)
        Form.setTabOrder(self.tagSpace, self.submitNoteButton)
        Form.setTabOrder(self.submitNoteButton, self.cancelButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Submit Note", None))
        self.userLabel.setText(_translate("Form", "User", None))
        self.dateLabel.setText(_translate("Form", "Date", None))
        self.timeLabel.setText(_translate("Form", "Time", None))
        self.projectLabel.setText(_translate("Form", "Project", None))
        self.programLabel.setText(_translate("Form", "Program", None))
        self.scenNameLabel.setText(_translate("Form", "Scene Name", None))
        __sortingEnabled = self.projectWidget.isSortingEnabled()
        self.projectWidget.setSortingEnabled(False)
        item = self.projectWidget.item(0)
        item.setText(_translate("Form", "Maya", None))
        item = self.projectWidget.item(1)
        item.setText(_translate("Form", "Nuke", None))
        item = self.projectWidget.item(2)
        item.setText(_translate("Form", "Photoshop", None))
        item = self.projectWidget.item(3)
        item.setText(_translate("Form", "Deltagen", None))
        item = self.projectWidget.item(4)
        item.setText(_translate("Form", "Other", None))
        self.projectWidget.setSortingEnabled(__sortingEnabled)
        self.snapShotPushButton.setText(_translate("Form", "Snap Shot", None))
        self.submitNoteButton.setText(_translate("Form", "Submit", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))
        self.subjectLabel.setText(_translate("Form", "Note Title:", None))
        self.tagLabel_3.setText(_translate("Form", "Description:", None))
        self.tagLabel_2.setText(_translate("Form", "Warnings: (optional)", None))
        self.tagLabel.setText(_translate("Form", "Tags (optional):", None))
        self.tagSpace.setPlaceholderText(_translate("Form", "example:  #materialChange#newACC", None))

from media import resource_rc