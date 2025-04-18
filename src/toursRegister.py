import sqlite3
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QCheckBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi


class ToursRegisterWindow(QMainWindow):
    finished = pyqtSignal()


    def __init__(self,):
        super().__init__()

        loadUi('ui/ToursRegister.ui', self)

        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.checkboxes = []

        self.destinationInput.textChanged.connect(self.addHotels)
        self.add_Tour_button.clicked.connect(self.addTour)
    


    def input_clear(self):
        self.idInput.setText("")
        self.destinationInput.setText("")
        self.descriptionInput.setText("")
        self.kmInput.setText("")
        for cb in self.checkboxes:
            cb.setParent(None)
        self.checkboxes.clear()

    
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


    def addTour(self):
        try:
            id = self.idInput.text()
            destination = self.destinationInput.text()
            start_date = self.start_dateEdit.date().toString("yyyy-MM-dd")  
            end_date = self.end_dateEdit.date().toString("yyyy-MM-dd")
            description = self.descriptionInput.text()
            km = self.kmInput.text()
            transportation = self.transportationInput.currentText()
            status = "Free"    


            self.cursor.execute("INSERT INTO Tours (id, destination, start_date, end_date, description, km, transportation, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (id, destination, start_date, end_date, description, km, transportation, status))
            
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




#start_date = self.start_dateEdit.date().toString("yyyy-MM-dd")  
       # end_date = self.end_dateEdit.date().toString("yyyy-MM-dd")