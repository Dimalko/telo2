import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal

class AdminWindow(QMainWindow):
    switch_login = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
    # Load the UI file
        loadUi('ui//admin.ui', self)
        
    #connect db
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()
        
    #populate tables/lists
        # self.populate_stock_table()
        # self.populate_sellers_table()
        # self.populate_order_list()
        # self.populate_order_table()
        # self.populate_finished_order_list()
        # self.populate_finished_order_table()
        # self.populate_notification_list()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.ui.show()
    sys.exit(app.exec_())