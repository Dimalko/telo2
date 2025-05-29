import sqlite3
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QCheckBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi

"""
    Window for registering new tours in the system.
    Allows users to create tours with destination, dates, description, transportation details,
    and associate hotels with the tour.
    """
class ToursRegisterWindow(QMainWindow):
    finished = pyqtSignal()

    """
        Initializes the tours registration window.
        Loads the UI, connects to the database, and sets up event handlers.
        """
    def __init__(self,):
        super().__init__()

        loadUi('ui/ToursRegister.ui', self)

        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.checkboxes = []

        self.destinationInput.textChanged.connect(self.addHotels)
        self.add_Tour_button.clicked.connect(self.addTour)

        #keep list of created ids
        self.generateId = set()
    

        """
        Clears all input fields and removes hotel checkboxes.
        Resets the form to its initial state after successful tour creation.
        """
    def input_clear(self):
        self.destinationInput.setText("")
        self.descriptionInput.setText("")
        self.kmInput.setText("")
        for cb in self.checkboxes:
            cb.setParent(None)
        self.checkboxes.clear()

    """
        Generates a unique tour ID.
        Creates a random 6-digit ID prefixed with 'TO' and ensures uniqueness
        by checking against previously generated IDs.
        :return: Unique tour ID string in format 'TO######'
        """
    def createItemID(self):
        min_id = 10**5  
        max_id = (10**6) - 1 
        
        while True:
            new_id = f"TO{random.randint(min_id, max_id)}"
            if new_id not in self.generateId:
                self.generateId.add(new_id)
                return new_id

    """
        Dynamically loads and displays hotels based on the entered destination.
        Creates checkboxes for each hotel in the specified city, allowing users
        to select which hotels to associate with the tour.
        """
    def addHotels(self):
        hotelCity = self.destinationInput.text()
        self.cursor.execute("SELECT id, name FROM Hotels WHERE city = ?",
                            (hotelCity,))
        hotels = self.cursor.fetchall()

        for hotel in hotels:
            checkbox = QCheckBox(hotel[1])
            checkbox.hotel_id = hotel[0]
            self.hotelContainer.addWidget(checkbox)
            self.checkboxes.append(checkbox)

    """
        Creates a new tour record in the database.
        Validates input fields, generates a unique ID, inserts tour data,
        and associates selected hotels with the tour. Shows warning messages
        for invalid input or database errors.
        """
    def addTour(self):
        try:
            id = self.createItemID()
            destination = self.destinationInput.text()
            start_date = self.start_dateEdit.date().toString("yyyy-MM-dd")  
            end_date = self.end_dateEdit.date().toString("yyyy-MM-dd")
            description = self.descriptionInput.text()
            km = float(self.kmInput.text())
            transportation = self.transportationInput.currentText()
            status = "Free"    
            activities = self.activitiesInput.text()


            self.cursor.execute("INSERT INTO Tours (id, destination, start_date, end_date, description, km, transportation, status, activities) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (id, destination, start_date, end_date, description, km, transportation, status, activities))
            if destination == "" or start_date == "" or end_date == "" or description == "" or km == "" or transportation == "" or status == "" or activities == "":
                raise ValueError("Empty fields")
            for cb in self.checkboxes:
                if cb.isChecked():
                    self.cursor.execute("INSERT INTO ToursHotels (tour_id, hotel_id) VALUES (?, ?)",
                                        (id, cb.hotel_id,))      
            self.connection.commit()
            
            self.hide()
            self.finished.emit()
            self.input_clear()
            
        except ValueError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")    