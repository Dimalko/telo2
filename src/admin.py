import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

from travelAgentRegister import TravelAgentRegisterWindow
from delete import DeleteWindow
from teamleaderRegister import TeamLeaderRegisterWindow
from driversRegister import DriverRegisterWindow
from busesRegister import BusesRegisterWindow
from toursRegister import ToursRegisterWindow


from classes.populate_table import PopulateTable

class AdminWindow(QMainWindow):
    open_TravelAgentReg = pyqtSignal()
    open_TeamLeaderReg = pyqtSignal()
    open_DriverReg = pyqtSignal()
    open_BusReg = pyqtSignal()
    open_TourReg = pyqtSignal()
    open_delete = pyqtSignal()
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

    #Connect Buttons
        #Navigation Buttons
        self.homeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.requestBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.ongoingBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.staffBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.vehiclesBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.statsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        #Add Buttons
        self.add_Travel_Agent_button.clicked.connect(self.addTravelAgent)
        self.add_Team_Leader_button.clicked.connect(self.addTeamLeader)
        self.add_Driver_Button.clicked.connect(self.addDriver)
        self.Add_Buses_Button.clicked.connect(self.addBus)
        self.add_Tour_button.clicked.connect(self.addTour)
        #Remove Buttons
        self.removeAgentBtn.clicked.connect(self.removeAgent)
        self.removeTourBtn.clicked.connect(self.removeTour)
        self.removeTeamLeaderBtn.clicked.connect(self.removeTeamLeader)

    #Populate Tables/Lists
        self.populate_tour_table()
        self.populate_travelagent_table()
        self.populate_teamleader_table()
        self.populate_driver_table()
        self.populate_buses_table()

    #Connect Other Windows
        self.TravelAgentRegister = TravelAgentRegisterWindow()
        self.TravelAgentRegister.finished.connect(lambda: self.update_table("Agents"))  

        self.TeamLeaderRegister = TeamLeaderRegisterWindow()
        self.TeamLeaderRegister.finished.connect(lambda: self.update_table("TeamLeaders")) 

        self.DriverRegister = DriverRegisterWindow()
        self.DriverRegister.finished.connect(lambda: self.update_table("Drivers"))

        self.BusRegister = BusesRegisterWindow()
        self.BusRegister.finished.connect(lambda: self.update_table("Buses"))

        self.ToursRegister = ToursRegisterWindow()
        self.ToursRegister.finished.connect(lambda: self.update_table("Tours"))
        
        seller_query = "DELETE FROM Staff WHERE id = ?"
        seller_labelText = "Travel Agent id:"
        self.removeAgentShow = DeleteWindow(seller_query, seller_labelText, True)
        self.removeAgentShow.finished.connect(lambda: self.update_table("Agents"))
        
        tour_query = "DELETE FROM Tours WHERE id = ?"
        tour_labelText = "Tour id:"
        self.removeTourShow = DeleteWindow(tour_query, tour_labelText, True)
        self.removeTourShow.finished.connect(lambda: self.update_table("Tours"))

        tLeader_query = "DELETE FROM TeamLeaders WHERE id = ?"
        tLeader_labelText = "Team Leader id:"
        self.removeTeamLeaderShow = DeleteWindow(tLeader_query, tLeader_labelText, True)
        self.removeTeamLeaderShow.finished.connect(lambda: self.update_table("TeamLeaders"))


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


#--Display Windows----------
    #Add Windows
    def addTravelAgent(self):
        self.open_TravelAgentReg.emit()
        self.TravelAgentRegister.show()
        self.populate_travelagent_table()
    
    def addTeamLeader(self):
        self.open_TeamLeaderReg.emit()
        self.TeamLeaderRegister.show()    
        self.populate_teamleader_table()  
    def addDriver(self):
        self.open_DriverReg.emit()
        self.DriverRegister.show()    
    def addBus(self):
        self.open_BusReg.emit()
        self.BusRegister.show()
    def addTour(self):
        self.open_TourReg.emit()
        self.ToursRegister.show()    
    #Remove/Delete Windows
    def removeAgent(self):
        self.open_delete.emit()
        self.removeAgentShow.show()

    def removeTour(self):
        self.open_delete.emit()
        self.removeTourShow.show()
    
    def removeTeamLeader(self):
        self.open_delete.emit()
        self.removeTeamLeaderShow.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())