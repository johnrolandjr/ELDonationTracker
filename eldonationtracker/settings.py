# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTdesignerfiles/settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(697, 356)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 681, 355))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.pushButtonSelectFolder = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSelectFolder.setObjectName("pushButtonSelectFolder")
        self.gridLayout.addWidget(self.pushButtonSelectFolder, 1, 3, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButtonRevert = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonRevert.setObjectName("pushButtonRevert")
        self.gridLayout.addWidget(self.pushButtonRevert, 9, 2, 1, 2)
        self.pushButton_sound = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sound.setObjectName("pushButton_sound")
        self.gridLayout.addWidget(self.pushButton_sound, 5, 3, 1, 2)
        self.label_donors_to_display = QtWidgets.QLabel(self.layoutWidget)
        self.label_donors_to_display.setObjectName("label_donors_to_display")
        self.gridLayout.addWidget(self.label_donors_to_display, 6, 0, 1, 1)
        self.lineEditTeamID = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditTeamID.setObjectName("lineEditTeamID")
        self.gridLayout.addWidget(self.lineEditTeamID, 3, 1, 1, 1)
        self.label_tracker_image = QtWidgets.QLabel(self.layoutWidget)
        self.label_tracker_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tracker_image.setObjectName("label_tracker_image")
        self.gridLayout.addWidget(self.label_tracker_image, 4, 1, 1, 1)
        self.lineEditParticipantID = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditParticipantID.setObjectName("lineEditParticipantID")
        self.gridLayout.addWidget(self.lineEditParticipantID, 0, 1, 1, 1)
        self.pushButton_persistentsave = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_persistentsave.setObjectName("pushButton_persistentsave")
        self.gridLayout.addWidget(self.pushButton_persistentsave, 10, 2, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEditCurrencySymbol = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditCurrencySymbol.setObjectName("lineEditCurrencySymbol")
        self.gridLayout.addWidget(self.lineEditCurrencySymbol, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_tracker_image = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_tracker_image.setObjectName("pushButton_tracker_image")
        self.gridLayout.addWidget(self.pushButton_tracker_image, 4, 3, 1, 2)
        self.spinBox_DonorsToDisplay = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_DonorsToDisplay.setObjectName("spinBox_DonorsToDisplay")
        self.gridLayout.addWidget(self.spinBox_DonorsToDisplay, 6, 1, 1, 1)
        self.labelTextFolder = QtWidgets.QLabel(self.layoutWidget)
        self.labelTextFolder.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTextFolder.setObjectName("labelTextFolder")
        self.gridLayout.addWidget(self.labelTextFolder, 1, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.label_sound = QtWidgets.QLabel(self.layoutWidget)
        self.label_sound.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sound.setObjectName("label_sound")
        self.gridLayout.addWidget(self.label_sound, 5, 1, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 9, 4, 1, 1)
        self.pushButton_font = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_font.setObjectName("pushButton_font")
        self.gridLayout.addWidget(self.pushButton_font, 7, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label_6.setText(_translate("Dialog", "Donation Sound"))
        self.pushButtonSelectFolder.setText(_translate("Dialog", "select Folder"))
        self.label_4.setText(_translate("Dialog", "Team ID"))
        self.label_2.setText(_translate("Dialog", "Text Folder"))
        self.pushButtonRevert.setText(_translate("Dialog", "Revert"))
        self.pushButton_sound.setText(_translate("Dialog", "select Sound"))
        self.label_donors_to_display.setText(_translate("Dialog", "Donors to Display"))
        self.label_tracker_image.setText(_translate("Dialog", "No Image Selected"))
        self.pushButton_persistentsave.setStatusTip(_translate("Dialog", "To have the settings persist across upgrades"))
        self.pushButton_persistentsave.setText(_translate("Dialog", "Persist Settings"))
        self.label_3.setText(_translate("Dialog", "Currency Symbol"))
        self.label_5.setText(_translate("Dialog", "Tracker Image"))
        self.label.setText(_translate("Dialog", "Participant ID"))
        self.pushButton_tracker_image.setText(_translate("Dialog", "select Image"))
        self.labelTextFolder.setText(_translate("Dialog", "No Folder Selected"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label_sound.setText(_translate("Dialog", "No Sound Selected"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButton_font.setText(_translate("Dialog", "Tracker Font"))
