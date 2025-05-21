import sqlite3
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi



class HotelRegisterWindow(QMainWindow):
    finished = pyqtSignal()


    def __init__(self,):
            super().__init__()
            
            loadUi('ui/hotelRegister.ui', self)
            
            self.connection = sqlite3.connect("data//database.db")
            self.cursor = self.connection.cursor()

            self.add_Hotel_button.clicked.connect(self.addHotel)    

            #keep list of created ids
            self.generateId = set()


    def input_clear(self):
            self.hotelNameInput.setText("")
            self.hotelCityInput.setText("")
            self.hotelAddressInput.setText("")
            self.hotelPriceInput.setText("") 

    
    def createItemID(self):
        min_id = 10**5  
        max_id = (10**6) - 1 
        
        while True:
            new_id = f"HTL{random.randint(min_id, max_id)}"
            if new_id not in self.generateId:
                self.generateId.add(new_id)
                return new_id


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