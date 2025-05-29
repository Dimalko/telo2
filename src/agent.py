import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QListWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

from classes.populate_table import PopulateTable
from reservation import ReservationWindow
from createDescription import CreateTourDescriptionWindow


"""AgentWindow class for the travel agency application.
This class represents the main window for travel agents, allowing them to manage tours, reservations, and staff.
It includes functionalities to add reservations, view and filter tours, and manage staff information.
"""
class AgentWindow(QMainWindow):
    open_ReservationtReg = pyqtSignal()
    open_createDescription = pyqtSignal()
    

    """Constructor for the AgentWindow class.
    Args:
        agent (str): The name of the agent. Default is "agent1". This parameter is for testing purposes and should be removed in the final version.
    """
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
        #Add Buttons
        self.add_Reservation_Button.clicked.connect(self.addReservation) 
        #LogOut Button
        self.logOutBtn.clicked.connect(self.to_login_window)
        #Create Tour Description Button
        self.createTourDescriptionBtn.clicked.connect(self.createTourDescription)

    #Populate Tables/Lists
        self.populate_tour_table()
        self.populate_travelagent_table()
        self.populate_teamleader_table()
        self.populate_driver_table()
        self.populate_buses_table()
    #Connect Other Windows
        self.ReservationRegister = ReservationWindow()
        self.ReservationRegister.finished.connect(lambda: self)  
        self.createDescriptionShow = CreateTourDescriptionWindow()    



    """Sets the style for the UI elements.
    This method sets the logo image and applies padding to the logo label."""
    #--Style----------   
    def uiStyle(self):
        pixmap = QPixmap("data//images//logo_image.png")
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.setStyleSheet("padding-top: 20px; padding-bottom: 20px;")

    """Updates the table after an action is performed.
    This method checks which table needs to be updated based on the provided table name and calls the appropriate method to repopulate the table.
    Args:
        table_name (str): The name of the table to be updated. Possible values are 'Agents', 'Drivers', 'Buses', 'TeamLeaders', and 'Tours'.
    """
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
    """Populates the tour table with data from the database.
    This method retrieves all tours from the database and displays them in the tour table widget."""
    def populate_tour_table(self):
        self.populate_table.populate_table(self.tourTableWidget, "SELECT * FROM Tours", 9)

    """Populates the travel agent table with data from the database.
    This method retrieves all travel agents from the database and displays them in the travel agent table widget."""    
    def populate_travelagent_table(self):
        self.populate_table.populate_table(self.travelagentTableWidget, "SELECT * FROM Staff WHERE role='Travel_Agent'", 8)

    """Populates the team leader table with data from the database.
    This method retrieves all team leaders from the database and displays them in the team leader table widget."""
    def populate_teamleader_table(self):
        self.populate_table.populate_table(self.teamleaderTableWidget, "SELECT * FROM TeamLeaders", 5)  

    """Populates the driver table with data from the database.
    This method retrieves all drivers from the database and displays them in the driver table widget."""
    def populate_driver_table(self):
        self.populate_table.populate_table(self.driverTableWidget, "SELECT * FROM Drivers", 6)    

    """Populates the buses table with data from the database.
    This method retrieves all buses from the database and displays them in the buses table widget."""
    def populate_buses_table(self):
        self.populate_table.populate_table(self.busesTableWidget, "SELECT * FROM Buses", 10)


    """Adds a new reservation.
    This method emits a signal to open the reservation registration window"""
    def addReservation(self):
        self.open_ReservationtReg.emit()
        self.ReservationRegister.show()


    """Loads free tours from the database.
    This method retrieves all tours with the status 'Free' and displays them in the tour list widget."""
    def loadFreeTours(self):
        self.TourlistWidget.clear()
        self.cursor.execute("SELECT id, destination FROM Tours WHERE status = 'Free'")
        tours = self.cursor.fetchall()

        for tour in tours:
            item = QListWidgetItem(f"{tour[0]} - {tour[1]}")
            item.setData(Qt.UserRole, tour[0])  # Αποθήκευση tour_id
            self.TourlistWidget.addItem(item)

    """Filters free tours based on the search text.
    This method retrieves tours with the status 'Free' that match the search text and updates the tour list widget accordingly.
    If no search text is provided, it loads all free tours."""
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

    """Loads reservations for a specific tour.
    This method retrieves all active reservations for the specified tour and displays them in the reservation table widget."""    
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
            AND Reservations.status = 'Active'
        """, (tour_id,))
        
        results = self.cursor.fetchall()

        for row_idx, row_data in enumerate(results):
            self.ReservationtableWidget.insertRow(row_idx)
            for col_idx, value in enumerate(row_data):
                self.ReservationtableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    """Handles the selection of a tour from the tour list widget.
    This method retrieves the tour ID from the selected item, loads the reservations for that tour,
    and updates the total cost label.
    """
    def handleTourSelection(self, item):
        tour_id = item.data(Qt.UserRole)
        self.loadTourReservations(tour_id)
        self.updateTotalCostLabel(tour_id)
    """Updates the total cost label for a specific tour.
    This method retrieves the total cost of all active reservations for the specified tour and updates the label accordingly.
    Args:
        tour_id (int): The ID of the tour for which to calculate the total cost.
    """
    def updateTotalCostLabel(self, tour_id):
        self.cursor.execute("""
            SELECT SUM(cost) FROM Reservations 
            WHERE tour_id = ? AND status = 'Active'
        """, (tour_id,))
        result = self.cursor.fetchone()
        total = result[0] if result[0] is not None else 0.0
        self.TotalCostlabel.setText(f"€ {total:.2f}")

    """Creates a tour description.
    This method emits a signal to open the create tour description window and shows the window."""
    #Create Tour Description Window
    def createTourDescription(self):
        self.open_createDescription.emit()
        self.createDescriptionShow.show()



#--LogOut----------
    """Navigates to the login window.
    This method imports the LoginWindow class, creates an instance of it, shows the login window, and hides the current agent window."""
    def to_login_window(self):
        from login import LoginWindow
        login_window_instance = LoginWindow()
        login_window_instance.show()
        self.hide()
        self.login_window_instance = login_window_instance



#!REMOVE BEFORE FINAL VERSION---------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgentWindow()
    window.show()
    sys.exit(app.exec_())