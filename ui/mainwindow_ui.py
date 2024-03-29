# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/barankrky/dts-yt-downloader/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 220)
        font = QtGui.QFont()
        font.setFamily("Sans")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appLabel = QtWidgets.QLabel(self.centralwidget)
        self.appLabel.setGeometry(QtCore.QRect(0, 10, 701, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.appLabel.setFont(font)
        self.appLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appLabel.setObjectName("appLabel")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(590, 60, 89, 25))
        self.downloadButton.setObjectName("downloadButton")
        self.urlBox = QtWidgets.QLineEdit(self.centralwidget)
        self.urlBox.setGeometry(QtCore.QRect(170, 60, 411, 25))
        self.urlBox.setObjectName("urlBox")
        self.urlText = QtWidgets.QLabel(self.centralwidget)
        self.urlText.setGeometry(QtCore.QRect(20, 60, 141, 21))
        self.urlText.setToolTipDuration(-1)
        self.urlText.setObjectName("urlText")
        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(600, 160, 89, 25))
        self.about.setObjectName("about")
        self.reportButton = QtWidgets.QPushButton(self.centralwidget)
        self.reportButton.setGeometry(QtCore.QRect(10, 160, 89, 25))
        self.reportButton.setObjectName("reportButton")
        self.infoText = QtWidgets.QLabel(self.centralwidget)
        self.infoText.setGeometry(QtCore.QRect(20, 100, 661, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.infoText.setFont(font)
        self.infoText.setStyleSheet("color: rgb(85, 87, 83)")
        self.infoText.setWordWrap(True)
        self.infoText.setObjectName("infoText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appLabel.setText(_translate("MainWindow", "DTS Youtube Downloader"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.urlText.setText(_translate("MainWindow", "Youtube Video URL"))
        self.about.setText(_translate("MainWindow", "About..."))
        self.reportButton.setText(_translate("MainWindow", "Report..."))
        self.infoText.setText(_translate("MainWindow", "<html><head/><body><p>When you copy the URL of the video you want to download from YouTube, paste it into the box above, and then press the \'Download\' button, your downloading process will begin. You can check the status above.</p></body></html>"))
