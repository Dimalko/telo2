import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

class AdminWindow(QMainWindow):
    switch_login = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
    # Load the UI file
        loadUi('ui//admin.ui', self)

    #add style to ui
        self.uiStyle()
        
    #connect db
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

    #connect buttons
        self.homeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.requestBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.ongoingBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.staffBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.vehiclesBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.statsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

    #populate tables/lists
        # self.populate_stock_table()
        # self.populate_sellers_table()
        # self.populate_order_list()
        # self.populate_order_table()
        # self.populate_finished_order_list()
        # self.populate_finished_order_table()
        # self.populate_notification_list()

    
    def uiStyle(self):
        pixmap = QPixmap("data//images//logo_image.png")
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.setStyleSheet("padding-top: 20px; padding-bottom: 20px;")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())