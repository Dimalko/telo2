import sqlite3
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi


class ToursRegisterWindow(QMainWindow):
    finished = pyqtSignal()


    def __init__(self,):
        super().__init__()

        loadUi('ui/ToursRegister.ui', self)

        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Tour_button.clicked.connect(self.addTour)
    


    def input_clear(self):
        self.idInput.setText("")
        self.destinationInput.setText("")
        self.descriptionInput.setText("")
        self.kmInput.setText("")
        self.transportationInput.setText("")


    def addTour(self):
        try:
            id = self.idInput.text()
            destination = self.destinationInput.text()
            start_date = self.start_dateEdit.date().toString("yyyy-MM-dd")  
            end_date = self.end_dateEdit.date().toString("yyyy-MM-dd")
            description = self.descriptionInput.text()
            km = self.kmInput.text()
            transportation = self.transportationInput.text()
            status = "Free"    


            self.cursor.execute("INSERT INTO Tours (id, destination, start_date, end_date, description, km, transportation, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (id, destination, start_date, end_date, description, km, transportation, status))
            self.connection.commit()
            self.finished.emit()
            self.input_clear()
            QMessageBox.information(self, "Success", "Tour added successfully")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Could not add Tour")
            self.input_clear()
            self.connection.rollback()
        finally:
            self.connection.close()
            self.finished.emit()
            self.close()




#start_date = self.start_dateEdit.date().toString("yyyy-MM-dd")  
       # end_date = self.end_dateEdit.date().toString("yyyy-MM-dd")