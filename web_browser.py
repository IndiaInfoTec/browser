# importing modules
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# main window
class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen,self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.Browser)
        self.showMaximized()
        NavBar=QToolBar()
        self.addToolBar(NavBar)

        # creating various buttons
        BackButton=QAction('←',self)
        BackButton.triggered.connect(self.Browser.back)
        NavBar.addAction(BackButton)

        ForwardButton = QAction('→',self)
        ForwardButton.triggered.connect(self.Browser.forward)
        NavBar.addAction(ForwardButton)

        ReloadButton = QAction('↻',self)
        ReloadButton.triggered.connect(self.Browser.reload)

        NavBar.addAction(ReloadButton)
        HomeButton = QAction('Home',self)
        HomeButton.triggered.connect(self.NavigateHome)

        self.UrlBar=QLineEdit()
        self.UrlBar.returnPressed.connect(self.NavigateToUrl)

        NavBar.addWidget(self.UrlBar)
        self.Browser.urlChanged.connect(self.UpdateUrl)

    def NavigateHome(self):
        self.Browser.setUrl("http://google.com")

    def NavigateToUrl(self):
        Url = self.UrlBar.text()
        self.Browser.setUrl(QUrl('https://google.com'))
        
    def UpdateUrl(self,p):
        self.UrlBar.setText(str(p))

Application = QApplication(sys.argv)
QApplication.setApplicationName('RP Browser')
Window = MainScreen()
Application.exec()
