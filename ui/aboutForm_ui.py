# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/burakdmrbkr/dts-yt-downloader/ui/aboutForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutForm(object):
    def setupUi(self, aboutForm):
        aboutForm.setObjectName("aboutForm")
        aboutForm.resize(618, 382)
        self.okbutton = QtWidgets.QPushButton(aboutForm)
        self.okbutton.setGeometry(QtCore.QRect(510, 350, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.aboutText = QtWidgets.QLabel(aboutForm)
        self.aboutText.setGeometry(QtCore.QRect(30, 160, 551, 101))
        font = QtGui.QFont()
        font.setFamily("Sans")
        self.aboutText.setFont(font)
        self.aboutText.setWordWrap(True)
        self.aboutText.setObjectName("aboutText")
        self.developedLabel = QtWidgets.QLabel(aboutForm)
        self.developedLabel.setGeometry(QtCore.QRect(30, 270, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        self.developedLabel.setFont(font)
        self.developedLabel.setObjectName("developedLabel")
        self.barankrky = QtWidgets.QLabel(aboutForm)
        self.barankrky.setGeometry(QtCore.QRect(50, 290, 131, 20))
        self.barankrky.setObjectName("barankrky")
        self.burakdmrbkr = QtWidgets.QLabel(aboutForm)
        self.burakdmrbkr.setGeometry(QtCore.QRect(40, 310, 101, 20))
        self.burakdmrbkr.setObjectName("burakdmrbkr")
        self.thedarklord = QtWidgets.QLabel(aboutForm)
        self.thedarklord.setGeometry(QtCore.QRect(40, 330, 81, 20))
        self.thedarklord.setObjectName("thedarklord")
        self.appName = QtWidgets.QLabel(aboutForm)
        self.appName.setGeometry(QtCore.QRect(30, 130, 411, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(True)
        font.setWeight(75)
        self.appName.setFont(font)
        self.appName.setObjectName("appName")
        self.appVersion = QtWidgets.QLabel(aboutForm)
        self.appVersion.setGeometry(QtCore.QRect(480, 130, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(False)
        font.setWeight(50)
        self.appVersion.setFont(font)
        self.appVersion.setObjectName("appVersion")

        self.retranslateUi(aboutForm)
        QtCore.QMetaObject.connectSlotsByName(aboutForm)

    def retranslateUi(self, aboutForm):
        _translate = QtCore.QCoreApplication.translate
        aboutForm.setWindowTitle(_translate("aboutForm", "Form"))
        self.okbutton.setText(_translate("aboutForm", "Ok"))
        self.aboutText.setText(_translate("aboutForm", "<html><head/><body><p>DTS is a YouTube video download application that stands out with its simple interface and reliability. It was developed to spite other fake applications on the internet. The application is still under development. If there is an error, you can report it to us from the \'Report\' section in the main menu. Thank you for choosing us."))
        self.developedLabel.setText(_translate("aboutForm", "Developed By"))
        self.barankrky.setText(_translate("aboutForm", "barankrky"))
        self.burakdmrbkr.setText(_translate("aboutForm", "burakdmrbkr"))
        self.thedarklord.setText(_translate("aboutForm", "thedarklord"))
        self.appName.setText(_translate("aboutForm", "Download This Shit Youtube Video Downloader"))
        self.appVersion.setText(_translate("aboutForm", "Version : 1.0"))