import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QListWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

from classes.populate_table import PopulateTable
from reservation import ReservationWindow

class AgentWindow(QMainWindow):
    open_ReservationtReg = pyqtSignal()
    def __init__(self, agent="agent1"): #REMOVE BEFORE FINAL VERSION
        super().__init__()

        loadUi('ui//agent.ui', self)

    #add style to ui
        self.uiStyle()
        
    #connect db
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()
        self.loadFreeTours()

    #initialize classes
        self.populate_table = PopulateTable()

    #Connect Buttons
        #Navigation Buttons
        self.homeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.reservationsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.staffBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.vehiclesBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.statsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.TourslineEdit.textChanged.connect(self.filterFreeTours)
        self.TourlistWidget.itemClicked.connect(self.handleTourSelection)

    #Populate Tables/Lists
        self.populate_tour_table()
        self.populate_travelagent_table()
        self.populate_teamleader_table()
        self.populate_driver_table()
        self.populate_buses_table()
    #Connect Other Windows
        self.ReservationRegister = ReservationWindow()
        self.ReservationRegister.finished.connect(lambda: self)
    #Add Buttons
        self.add_Reservation_Button.clicked.connect(self.addReservation)        




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



    def addReservation(self):
        self.open_ReservationtReg.emit()
        self.ReservationRegister.show()



    def loadFreeTours(self):
        self.TourlistWidget.clear()
        self.cursor.execute("SELECT id, destination FROM Tours WHERE status = 'Free'")
        tours = self.cursor.fetchall()

        for tour in tours:
            item = QListWidgetItem(f"{tour[0]} - {tour[1]}")
            item.setData(Qt.UserRole, tour[0])  # Αποθήκευση tour_id
            self.TourlistWidget.addItem(item)
    
    def filterFreeTours(self):
            search_text = self.TourslineEdit.text().strip().lower()
            self.TourlistWidget.clear()

            if not search_text:
                self.loadFreeTours()
                return

            self.cursor.execute("""
                SELECT id, destination FROM Tours
                WHERE status = 'Free' AND LOWER(id) LIKE ?
            """, (f"{search_text}%",))
            tours = self.cursor.fetchall()

            if not tours:
                self.TourlistWidget.addItem("No results for this value")
                return

            for tour in tours:
                item = QListWidgetItem(f"{tour[0]} - {tour[1]}")
                item.setData(Qt.UserRole, tour[0])
                self.TourlistWidget.addItem(item)

        
    def loadTourReservations(self, tour_id):
        self.ReservationtableWidget.setRowCount(0)
        self.cursor.execute("""
            SELECT
                Reservations.id,
                Client.f_name,
                Reservations.people_numb,
                Hotels.name,
                Reservations.cost,
                Reservations.payment_type
            FROM Reservations
            JOIN Client ON Reservations.client_n = Client.phone_number
            JOIN Hotels ON Reservations.hotel_id = Hotels.id
            WHERE Reservations.tour_id = ?
        """, (tour_id,))
        
        results = self.cursor.fetchall()

        for row_idx, row_data in enumerate(results):
            self.ReservationtableWidget.insertRow(row_idx)
            for col_idx, value in enumerate(row_data):
                self.ReservationtableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def handleTourSelection(self, item):
        tour_id = item.data(Qt.UserRole)
        self.loadTourReservations(tour_id)
        self.updateTotalCostLabel(tour_id)

    def updateTotalCostLabel(self, tour_id):
        self.cursor.execute("""
            SELECT SUM(cost) FROM Reservations WHERE tour_id = ?
        """, (tour_id,))
        result = self.cursor.fetchone()
        total = result[0] if result[0] is not None else 0.0
        self.TotalCostlabel.setText(f"€ {total:.2f}")


#!REMOVE BEFORE FINAL VERSION---------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgentWindow()
    window.show()
    sys.exit(app.exec_())