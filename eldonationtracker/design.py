# -*- coding: utf-8 -*-
# type: ignore
# Form implementation generated from reading ui file '../QTdesignerfiles/design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 749)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../QTdesignerfiles/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.ParticipantInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.ParticipantInfo.setGeometry(QtCore.QRect(10, 60, 301, 301))
        self.ParticipantInfo.setObjectName("ParticipantInfo")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.ParticipantInfo)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 281, 295))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_avg_donations = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_avg_donations.setAlignment(QtCore.Qt.AlignCenter)
        self.label_avg_donations.setObjectName("label_avg_donations")
        self.gridLayout.addWidget(self.label_avg_donations, 3, 1, 1, 1)
        self.TotalRaised = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TotalRaised.sizePolicy().hasHeightForWidth())
        self.TotalRaised.setSizePolicy(sizePolicy)
        self.TotalRaised.setMaximumSize(QtCore.QSize(100, 50))
        self.TotalRaised.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TotalRaised.setObjectName("TotalRaised")
        self.gridLayout.addWidget(self.TotalRaised, 4, 0, 1, 1)
        self.label_totalraised = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_totalraised.setAlignment(QtCore.Qt.AlignCenter)
        self.label_totalraised.setObjectName("label_totalraised")
        self.gridLayout.addWidget(self.label_totalraised, 3, 0, 1, 1)
        self.participant_avatar = QtWebEngineWidgets.QWebEngineView(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.participant_avatar.sizePolicy().hasHeightForWidth())
        self.participant_avatar.setSizePolicy(sizePolicy)
        self.participant_avatar.setAutoFillBackground(False)
        self.participant_avatar.setUrl(QtCore.QUrl("about:blank"))
        self.participant_avatar.setZoomFactor(0.63)
        self.participant_avatar.setObjectName("participant_avatar")
        self.gridLayout.addWidget(self.participant_avatar, 0, 0, 1, 1)
        self.AvgDonation = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AvgDonation.sizePolicy().hasHeightForWidth())
        self.AvgDonation.setSizePolicy(sizePolicy)
        self.AvgDonation.setMaximumSize(QtCore.QSize(100, 50))
        self.AvgDonation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AvgDonation.setObjectName("AvgDonation")
        self.gridLayout.addWidget(self.AvgDonation, 4, 1, 1, 1)
        self.label_total_num_donations = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_total_num_donations.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_num_donations.setObjectName("label_total_num_donations")
        self.gridLayout.addWidget(self.label_total_num_donations, 1, 1, 1, 1)
        self.label_goal = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_goal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_goal.setObjectName("label_goal")
        self.gridLayout.addWidget(self.label_goal, 1, 0, 1, 1)
        self.TotalNumDonations = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TotalNumDonations.sizePolicy().hasHeightForWidth())
        self.TotalNumDonations.setSizePolicy(sizePolicy)
        self.TotalNumDonations.setMaximumSize(QtCore.QSize(100, 50))
        self.TotalNumDonations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TotalNumDonations.setObjectName("TotalNumDonations")
        self.gridLayout.addWidget(self.TotalNumDonations, 2, 1, 1, 1)
        self.Goal = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Goal.sizePolicy().hasHeightForWidth())
        self.Goal.setSizePolicy(sizePolicy)
        self.Goal.setMaximumSize(QtCore.QSize(100, 50))
        self.Goal.setBaseSize(QtCore.QSize(0, 0))
        self.Goal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Goal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Goal.setObjectName("Goal")
        self.gridLayout.addWidget(self.Goal, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 115, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.DonationInfo = QtWidgets.QGroupBox(self.centralwidget)
        self.DonationInfo.setGeometry(QtCore.QRect(330, 60, 451, 301))
        self.DonationInfo.setObjectName("DonationInfo")
        self.label = QtWidgets.QLabel(self.DonationInfo)
        self.label.setGeometry(QtCore.QRect(30, 140, 121, 16))
        self.label.setObjectName("label")
        self.RecentDonations = QtWidgets.QTextBrowser(self.DonationInfo)
        self.RecentDonations.setGeometry(QtCore.QRect(10, 160, 431, 101))
        self.RecentDonations.setAutoFillBackground(False)
        self.RecentDonations.setDocumentTitle("")
        self.RecentDonations.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.RecentDonations.setObjectName("RecentDonations")
        self.LastDonation = QtWidgets.QTextBrowser(self.DonationInfo)
        self.LastDonation.setGeometry(QtCore.QRect(10, 40, 431, 31))
        self.LastDonation.setAutoFillBackground(False)
        self.LastDonation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LastDonation.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LastDonation.setObjectName("LastDonation")
        self.label_2 = QtWidgets.QLabel(self.DonationInfo)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.DonationInfo)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_3.setObjectName("label_3")
        self.TopDonation = QtWidgets.QTextBrowser(self.DonationInfo)
        self.TopDonation.setGeometry(QtCore.QRect(10, 100, 431, 31))
        self.TopDonation.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TopDonation.setObjectName("TopDonation")
        self.TeamGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TeamGroupBox.setGeometry(QtCore.QRect(10, 370, 771, 291))
        self.TeamGroupBox.setObjectName("TeamGroupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.TeamGroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 751, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.label_TeamTotalRaised = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_TeamTotalRaised.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_TeamTotalRaised.setObjectName("label_TeamTotalRaised")
        self.gridLayout_2.addWidget(self.label_TeamTotalRaised, 1, 4, 1, 1)
        self.textBrowser_TeamTop5 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_TeamTop5.setObjectName("textBrowser_TeamTop5")
        self.gridLayout_2.addWidget(self.textBrowser_TeamTop5, 3, 2, 1, 4)
        self.label_TeamGoal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_TeamGoal.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_TeamGoal.setObjectName("label_TeamGoal")
        self.gridLayout_2.addWidget(self.label_TeamGoal, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_TeamNumDonations = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_TeamNumDonations.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_TeamNumDonations.setObjectName("label_TeamNumDonations")
        self.gridLayout_2.addWidget(self.label_TeamNumDonations, 1, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(254, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 6, 1, 1)
        self.label_TeamCaptain = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_TeamCaptain.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_TeamCaptain.setObjectName("label_TeamCaptain")
        self.gridLayout_2.addWidget(self.label_TeamCaptain, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.label_TopTeamParticipant = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_TopTeamParticipant.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_TopTeamParticipant.setObjectName("label_TopTeamParticipant")
        self.gridLayout_2.addWidget(self.label_TopTeamParticipant, 3, 6, 1, 1)
        self.pushButtonRun = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRun.setGeometry(QtCore.QRect(570, 670, 84, 31))
        self.pushButtonRun.setObjectName("pushButtonRun")
        self.pushButtonStop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStop.setGeometry(QtCore.QRect(670, 670, 84, 31))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.CopyrightLabel = QtWidgets.QLabel(self.centralwidget)
        self.CopyrightLabel.setGeometry(QtCore.QRect(30, 680, 481, 31))
        self.CopyrightLabel.setObjectName("CopyrightLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SettingsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SettingsButton.setAutoDefault(False)
        self.SettingsButton.setDefault(False)
        self.SettingsButton.setFlat(False)
        self.SettingsButton.setObjectName("SettingsButton")
        self.horizontalLayout.addWidget(self.SettingsButton)
        self.TrackerButton = QtWidgets.QPushButton(self.layoutWidget)
        self.TrackerButton.setObjectName("TrackerButton")
        self.horizontalLayout.addWidget(self.TrackerButton)
        self.ProgressBarButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ProgressBarButton.setObjectName("ProgressBarButton")
        self.horizontalLayout.addWidget(self.ProgressBarButton)
        self.RefreshButton = QtWidgets.QPushButton(self.layoutWidget)
        self.RefreshButton.setObjectName("RefreshButton")
        self.horizontalLayout.addWidget(self.RefreshButton)
        self.TestAlertButton = QtWidgets.QPushButton(self.layoutWidget)
        self.TestAlertButton.setObjectName("TestAlertButton")
        self.horizontalLayout.addWidget(self.TestAlertButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 788, 29))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionCheck_for_Update = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Update.setObjectName("actionCheck_for_Update")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionCheck_for_Update)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EL Donation Tracker"))
        self.ParticipantInfo.setTitle(_translate("MainWindow", "Participant Info"))
        self.label_avg_donations.setText(_translate("MainWindow", "Average Donation"))
        self.label_totalraised.setText(_translate("MainWindow", "Total Raised"))
        self.label_total_num_donations.setText(_translate("MainWindow", "Total # of Donations"))
        self.label_goal.setText(_translate("MainWindow", "Goal"))
        self.DonationInfo.setTitle(_translate("MainWindow", "Participant Donation Info"))
        self.label.setText(_translate("MainWindow", "Recent Donations"))
        self.RecentDonations.setPlaceholderText(_translate("MainWindow", "Recent Donations"))
        self.LastDonation.setPlaceholderText(_translate("MainWindow", "Last Donation"))
        self.label_2.setText(_translate("MainWindow", "Last Donation"))
        self.label_3.setText(_translate("MainWindow", "Top Donor"))
        self.TopDonation.setPlaceholderText(_translate("MainWindow", "Top Donor"))
        self.TeamGroupBox.setTitle(_translate("MainWindow", "Team Info"))
        self.label_TeamTotalRaised.setText(_translate("MainWindow", "Raised"))
        self.label_TeamGoal.setText(_translate("MainWindow", "Team Goal"))
        self.label_11.setText(_translate("MainWindow", "# of Donations"))
        self.label_10.setText(_translate("MainWindow", "Goal"))
        self.label_TeamNumDonations.setText(_translate("MainWindow", "# Donations"))
        self.label_12.setText(_translate("MainWindow", "Total Raised"))
        self.label_13.setText(_translate("MainWindow", "Top Team Participant"))
        self.label_TeamCaptain.setText(_translate("MainWindow", "Team Captain"))
        self.label_14.setText(_translate("MainWindow", "Top 5 Team Participants"))
        self.label_9.setText(_translate("MainWindow", "Team Captain"))
        self.label_TopTeamParticipant.setText(_translate("MainWindow", "Top Team Participant"))
        self.pushButtonRun.setText(_translate("MainWindow", "Run"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop"))
        self.CopyrightLabel.setText(_translate("MainWindow", "© 2015-2021 Eric Mesa; Licensed GPLv3; http://extralife.ericmesa.com"))
        self.SettingsButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Change folders, Extra Life ID, etc</p></body></html>"))
        self.SettingsButton.setText(_translate("MainWindow", "Settings"))
        self.TrackerButton.setText(_translate("MainWindow", "Tracker"))
        self.ProgressBarButton.setText(_translate("MainWindow", "Progress Bar"))
        self.RefreshButton.setText(_translate("MainWindow", "Force Refresh"))
        self.TestAlertButton.setText(_translate("MainWindow", "Test Alert"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionDocumentation.setToolTip(_translate("MainWindow", "Open Documentation in your default browser"))
        self.actionCheck_for_Update.setText(_translate("MainWindow", "Check for Update"))
        self.actionCheck_for_Update.setToolTip(_translate("MainWindow", "Checks for Updates"))
        self.actionAbout.setText(_translate("MainWindow", "About ELDonationTracker"))
from PyQt5 import QtWebEngineWidgets
