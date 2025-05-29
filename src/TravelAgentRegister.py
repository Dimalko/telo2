import sqlite3
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi

"""
    Window for registering new travel agents in the system.
    Allows administrators to create new travel agent accounts with personal details,
    work hours, and salary information.
    """
class TravelAgentRegisterWindow(QMainWindow):
    finished = pyqtSignal()
    
    """
        Initializes the travel agent registration window.
        Loads the UI, connects to the database, and sets up event handlers for the registration form.
        """
    def __init__(self,):
        super().__init__()
        
        loadUi('ui/TravelAgentRegister.ui', self)
        
        
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Travel_Agent_button.clicked.connect(self.addTravelAgent)
        
        #keep list of created ids
        self.generateId = set()


    """
        Clears all input fields in the registration form.
        Resets the form to its initial state after successful agent registration.
        """
    def input_clear(self):
        self.usernameInput.setText("")
        self.passwordInput.setText("")
        self.FirstNameInput.setText("")
        self.LastNameInput.setText("")
        self.Work_HoursInput.setText("")
        self.SalaryInput.setText("")

    """
        Generates a unique travel agent ID.
        Creates a random 6-digit ID prefixed with 'AG' and ensures uniqueness
        by checking against previously generated IDs.
        :return: Unique agent ID string in format 'AG######'
        """
    def createItemID(self):
        min_id = 10**5  
        max_id = (10**6) - 1 
        
        while True:
            new_id = f"AG{random.randint(min_id, max_id)}"
            if new_id not in self.generateId:
                self.generateId.add(new_id)
                return new_id


    """
        Creates a new travel agent record in the database.
        Validates input fields, generates a unique ID, and inserts the agent data
        into the Staff table with role 'Travel_Agent'. Shows warning messages
        for invalid input or database constraint violations.
        """
    def addTravelAgent(self):
        try:
            id=self.createItemID()
            username = self.usernameInput.text()
            password = self.passwordInput.text()
            firstname = self.FirstNameInput.text()
            lastName = self.LastNameInput.text()
            hours = float(self.Work_HoursInput.text())
            salary = float(self.SalaryInput.text())
            role="Travel_Agent"
            

            self.cursor.execute("INSERT INTO Staff (id, username, password, f_name, l_name, role, work_hours, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (id,username, password, firstname, lastName, role, hours, salary))
            if username == "" or password == "" or firstname == "" or lastName == "" or hours == "" or salary == "":
                raise ValueError("Empty fields")
            self.connection.commit()
            
            self.hide()
            self.finished.emit()
            
            self.input_clear()
        except ValueError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")    