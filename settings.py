# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(612, 279)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 0, 591, 271))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditCurrencySymbol = QtWidgets.QLineEdit(self.widget)
        self.lineEditCurrencySymbol.setObjectName("lineEditCurrencySymbol")
        self.gridLayout.addWidget(self.lineEditCurrencySymbol, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditParticipantID = QtWidgets.QLineEdit(self.widget)
        self.lineEditParticipantID.setObjectName("lineEditParticipantID")
        self.gridLayout.addWidget(self.lineEditParticipantID, 0, 1, 1, 1)
        self.labelTextFolder = QtWidgets.QLabel(self.widget)
        self.labelTextFolder.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTextFolder.setObjectName("labelTextFolder")
        self.gridLayout.addWidget(self.labelTextFolder, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButtonSelectFolder = QtWidgets.QPushButton(self.widget)
        self.pushButtonSelectFolder.setObjectName("pushButtonSelectFolder")
        self.gridLayout.addWidget(self.pushButtonSelectFolder, 1, 3, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditTeamID = QtWidgets.QLineEdit(self.widget)
        self.lineEditTeamID.setObjectName("lineEditTeamID")
        self.gridLayout.addWidget(self.lineEditTeamID, 3, 1, 1, 1)
        self.pushButtonRevert = QtWidgets.QPushButton(self.widget)
        self.pushButtonRevert.setObjectName("pushButtonRevert")
        self.gridLayout.addWidget(self.pushButtonRevert, 5, 2, 1, 2)
        self.pushButtonSave = QtWidgets.QPushButton(self.widget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 5, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_tracker_image = QtWidgets.QLabel(self.widget)
        self.label_tracker_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tracker_image.setObjectName("label_tracker_image")
        self.gridLayout.addWidget(self.label_tracker_image, 4, 1, 1, 1)
        self.pushButton_tracker_image = QtWidgets.QPushButton(self.widget)
        self.pushButton_tracker_image.setObjectName("pushButton_tracker_image")
        self.gridLayout.addWidget(self.pushButton_tracker_image, 4, 3, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label_2.setText(_translate("Dialog", "Text Folder"))
        self.labelTextFolder.setText(_translate("Dialog", "No Folder Selected"))
        self.label_3.setText(_translate("Dialog", "Currency Symbol"))
        self.pushButtonSelectFolder.setText(_translate("Dialog", "select Folder"))
        self.label.setText(_translate("Dialog", "Participant ID"))
        self.label_4.setText(_translate("Dialog", "Team ID"))
        self.pushButtonRevert.setText(_translate("Dialog", "Revert"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.label_5.setText(_translate("Dialog", "Tracker Image"))
        self.label_tracker_image.setText(_translate("Dialog", "No Image Selected"))
        self.pushButton_tracker_image.setText(_translate("Dialog", "select Image"))

