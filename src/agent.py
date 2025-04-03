import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

from classes.populate_table import PopulateTable


class AgentWindow(QMainWindow):

    def __init__(self, agent="agent1"): #REMOVE BEFORE FINAL VERSION
        super().__init__()

        loadUi('ui//agent.ui', self)

    #add style to ui
        self.uiStyle()
        
    #connect db
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

    #initialize classes
        self.populate_table = PopulateTable()

    #Connect Buttons
        #Navigation Buttons
        self.homeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.reservationsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.staffBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.vehiclesBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.statsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

    #Populate Tables/Lists
        self.populate_tour_table()
        self.populate_travelagent_table()
        self.populate_teamleader_table()
        self.populate_driver_table()
        self.populate_buses_table()



    #--Style----------   
    def uiStyle(self):
        pixmap = QPixmap("data//images//logo_image.png")
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.setStyleSheet("padding-top: 20px; padding-bottom: 20px;")

#--Update Tables After An Action----------
    def update_table(self, table_name):
        if table_name == 'Agents':
            self.populate_travelagent_table()
        elif table_name == 'Drivers':
            self.populate_driver_table()
        elif table_name == 'Buses':
            self.populate_buses_table()           
        elif table_name == 'TeamLeaders':
            self.populate_teamleader_table()    
        elif table_name == "Tours":
            self.populate_tour_table()


#--Populate Tables----------  
    def populate_tour_table(self):
        self.populate_table.populate_table(self.tourTableWidget, "SELECT * FROM Tours", 9)
        
    def populate_travelagent_table(self):
        self.populate_table.populate_table(self.travelagentTableWidget, "SELECT * FROM Staff WHERE role='Travel_Agent'", 8)
    
    def populate_teamleader_table(self):
        self.populate_table.populate_table(self.teamleaderTableWidget, "SELECT * FROM TeamLeaders", 5)  
    
    def populate_driver_table(self):
        self.populate_table.populate_table(self.driverTableWidget, "SELECT * FROM Drivers", 6)    
    
    def populate_buses_table(self):
        self.populate_table.populate_table(self.busesTableWidget, "SELECT * FROM Buses", 10)






#!REMOVE BEFORE FINAL VERSION---------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgentWindow()
    window.show()
    sys.exit(app.exec_())