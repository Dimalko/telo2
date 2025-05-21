import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi



class TeamLeaderRegisterWindow(QMainWindow):
    finished = pyqtSignal()


    def __init__(self,):
        super().__init__()
            
        loadUi('ui/TeamLeadersRegister.ui', self)
            
            
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Team_Leader_button.clicked.connect(self.addTeamLeader) 


    def input_clear(self):
        self.IdInput.setText("")
        self.FirstNameInput.setText("")
        self.LastNameInput.setText("")
        self.PaymentInput.setText("")
        self.SkillsInput.setText("")   


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