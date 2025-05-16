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
            payment = self.PaymentInput.text()
            skills = self.SkillsInput.text()
            

            self.cursor.execute("INSERT INTO TeamLeaders (id, f_name, l_name, payment, skills) VALUES (?, ?, ?, ?, ?)",
                                (id, firstName, lastName, payment, skills))
            self.connection.commit()
            self.finished.emit()
            self.input_clear()
            QMessageBox.information(self, "Success", "Team Leader added successfully")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Could not add Team Leader")
            self.input_clear()
            self.connection.rollback()
        finally:
            self.connection.close()
            self.finished.emit()
            self.close()