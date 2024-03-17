import sys, webbrowser
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from ui.mainwindow_ui import Ui_MainWindow
from ui.aboutForm_ui import Ui_aboutForm
from modules import downloader
from threading import Thread

class DTS_Video_Downloader(QMainWindow):
    def __init__(self):
        super(DTS_Video_Downloader, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.downloader = downloader
        self.setWindowTitle("DTS Video Downloader")
        self.ui.statusBar.showMessage("Ready...")
        self.ui.about.clicked.connect(self.showAbout)
        self.ui.reportButton.clicked.connect(self.reportIssue)
        self.ui.downloadButton.clicked.connect(lambda : self.downloadVideo())


    def downloadThread(self):
        thread = Thread(target=self.downloadVideo)
        thread.start()

    def downloadVideo(self):
        self.ui.statusBar.showMessage("Download starting, please wait amk...")
        user_url = self.ui.urlBox.text()
        self.ui.statusBar.showMessage(self.downloader.DownloadVideo(user_url))
        

    def sleep(self, seconds=3):
        self.timer = QTimer()
        self.timer.timeout.connect(self.sleep)
        self.timer.start(seconds*1000)

    def reportIssue(self):
        issuesUrl = r"https://github.com/barankrky/dts-yt-downloader/issues/new"
        webbrowser.open(issuesUrl)

    def showAbout(self):
        self.aboutWindow = AboutWindow()
        self.aboutWindow.show()
        
        
class AboutWindow(QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_aboutForm()
        self.ui.setupUi(self)
        self.setWindowTitle("About")
        self.ui.okbutton.clicked.connect(self.close)

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DTS_Video_Downloader()
    win.show()
    sys.exit(app.exec_())