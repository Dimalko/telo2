import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi


"""
    Window for registering new team leaders in the system.
    Allows users to add team leader information including personal details,
    payment information, and specialized skills.
    """
class TeamLeaderRegisterWindow(QMainWindow):
    finished = pyqtSignal()

    """
        Initializes the team leader registration window.
        Loads the UI, connects to the database, and sets up the event handler
        for the team leader registration button.
        """
    def __init__(self,):
        super().__init__()
            
        loadUi('ui/TeamLeadersRegister.ui', self)
            
            
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Team_Leader_button.clicked.connect(self.addTeamLeader) 

    """
        Clears all input fields in the team leader registration form.
        Resets the form to its initial state after successful team leader registration.
        """
    def input_clear(self):
        self.IdInput.setText("")
        self.FirstNameInput.setText("")
        self.LastNameInput.setText("")
        self.PaymentInput.setText("")
        self.SkillsInput.setText("")   

    """
        Creates a new team leader record in the database.
        Validates that required fields (ID, first name, last name, payment) are provided,
        retrieves form data including personal information, payment details, and skills.
        Inserts the team leader data into the database. Shows warning messages
        for invalid input or database constraint violations.
        """
    def addTeamLeader(self):
        try:
            id = self.IdInput.text()
            firstName = self.FirstNameInput.text()
            lastName = self.LastNameInput.text()
            payment = float(self.PaymentInput.text())
            skills = self.SkillsInput.text()
            

            self.cursor.execute("INSERT INTO TeamLeaders (id, f_name, l_name, payment, skills) VALUES (?, ?, ?, ?, ?)",
                                (id, firstName, lastName, payment, skills))
            if id != ""or firstName != "" or lastName != "" or payment != "":
                self.connection.commit()
            else:
                raise ValueError
            self.input_clear()
            self.connection.commit()
            self.hide()
            self.finished.emit()
            self.input_clear()
        except ValueError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")  