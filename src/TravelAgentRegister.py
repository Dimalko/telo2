import sqlite3
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi

class TravelAgentRegisterWindow(QMainWindow):
    finished = pyqtSignal()

    def __init__(self,):
        super().__init__()
        
        loadUi('ui/TravelAgentRegister.ui', self)
        
        
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Travel_Agent_button.clicked.connect(self.addTravelAgent)
        
        #keep list of created ids
        self.generateId = set()



    def input_clear(self):
        self.usernameInput.setText("")
        self.passwordInput.setText("")
        self.FirstNameInput.setText("")
        self.LastNameInput.setText("")
        self.Work_HoursInput.setText("")
        self.SalaryInput.setText("")


    def createItemID(self):
        min_id = 10**5  
        max_id = (10**6) - 1 
        
        while True:
            new_id = f"AG{random.randint(min_id, max_id)}"
            if new_id not in self.generateId:
                self.generateId.add(new_id)
                return new_id



    def addTravelAgent(self):
        try:
            id=self.createItemID()
            username = self.usernameInput.text()
            password = self.passwordInput.text()
            firstname = self.FirstNameInput.text()
            lastName = self.LastNameInput.text()
            hours = self.Work_HoursInput.text()
            salary = self.SalaryInput.text()
            role="Travel_Agent"
            

            self.cursor.execute("INSERT INTO Staff (id, username, password, f_name, l_name, role, work_hours, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (id,username, password, firstname, lastName, role, hours, salary))
            self.connection.commit()
            
            self.hide()
            self.finished.emit()
            
            self.input_clear()
        except ValueError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")    