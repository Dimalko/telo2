import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

from TravelAgentRegister import TravelAgentRegisterWindow

from classes.populate_table import PopulateTable

class AdminWindow(QMainWindow):
    open_TravelAgentReg = pyqtSignal()
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

    #initialize classes
        self.populate_table = PopulateTable()

    #connect buttons
        self.homeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.requestBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.ongoingBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.staffBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.vehiclesBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.statsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.add_Travel_Agent_button.clicked.connect(self.addTravelAgent)

    #populate tables/lists
        self.populate_tour_table()
        self.populate_travelagent_table()
        # self.populate_sellers_table()
        # self.populate_order_list()
        # self.populate_order_table()
        # self.populate_finished_order_list()
        # self.populate_finished_order_table()
        # self.populate_notification_list()

     # Connect other windows
        self.TravelAgentRegister = TravelAgentRegisterWindow()
        self.TravelAgentRegister.finished.connect(lambda: self.update_table("Agents"))    

    
    def uiStyle(self):
        pixmap = QPixmap("data//images//logo_image.png")
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.setStyleSheet("padding-top: 20px; padding-bottom: 20px;")

    def update_table(self, table_name):
        if table_name == 'Agents':
            self.populate_travelagent_table()
        elif table_name == "tours":
            self.populate_tour_table()

    
    def populate_tour_table(self):
        self.populate_table.populate_table(self.tourTableWidget, "SELECT * FROM Tours", 9)
        
    def populate_travelagent_table(self):
        self.populate_table.populate_table(self.travelagentTableWidget, "SELECT * FROM Staff WHERE role='Travel_Agent'", 8)
#windows dislpay--------
    def addTravelAgent(self):
        self.open_TravelAgentReg.emit()
        self.TravelAgentRegister.show()
        self.populate_travelagent_table()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())