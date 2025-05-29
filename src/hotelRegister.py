import sqlite3
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi


"""
    Window for registering new hotels in the system.
    Allows users to add hotel information including name, location details,
    and pricing to the hotel management system.
    """
class HotelRegisterWindow(QMainWindow):
    finished = pyqtSignal()

    """
        Initializes the hotel registration window.
        Loads the UI, connects to the database, sets up event handlers,
        and initializes the ID generation tracking set.
        """
    def __init__(self,):
            super().__init__()
            
            loadUi('ui/hotelRegister.ui', self)
            
            self.connection = sqlite3.connect("data//database.db")
            self.cursor = self.connection.cursor()

            self.add_Hotel_button.clicked.connect(self.addHotel)    

            #keep list of created ids
            self.generateId = set()

    """
        Clears all input fields in the hotel registration form.
        Resets the form to its initial state after successful hotel registration.
        """
    def input_clear(self):
            self.hotelNameInput.setText("")
            self.hotelCityInput.setText("")
            self.hotelAddressInput.setText("")
            self.hotelPriceInput.setText("") 

    """
        Generates a unique hotel ID.
        Creates a random 6-digit ID prefixed with 'HTL' and ensures uniqueness
        by checking against previously generated IDs.
        :return: Unique hotel ID string in format 'HTL######'
        """
    def createItemID(self):
        min_id = 10**5  
        max_id = (10**6) - 1 
        
        while True:
            new_id = f"HTL{random.randint(min_id, max_id)}"
            if new_id not in self.generateId:
                self.generateId.add(new_id)
                return new_id

    """
        Creates a new hotel record in the database.
        Validates input fields, generates a unique ID, and inserts hotel data
        including name, city, address, and price per person. Validates that
        name and address fields are not empty. Shows warning messages
        for invalid input or database constraint violations.
        """
    def addHotel(self):
            try:
                id = self.createItemID()
                name = self.hotelNameInput.text()
                city = self.hotelCityInput.text()
                address = self.hotelAddressInput.text()
                price = float(self.hotelPriceInput.text())
                

                self.cursor.execute("INSERT INTO Hotels (id, name, city, address, price_pp) VALUES (?, ?, ?, ?, ?)",
                                    (id, name, city, address, price))
                if name != "":
                 self.connection.commit()
                else:
                    raise ValueError
                if address != "":
                 self.connection.commit()
                else:
                    raise ValueError
                
                self.hide()
                self.finished.emit()
                self.input_clear()
                
            except ValueError:
                QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")    