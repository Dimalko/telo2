import sqlite3
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


    def input_clear(self):
            self.hotelIdInput.setText("")
            self.hotelNameInput.setText("")
            self.hotelAddressInput.setText("")
            self.hotelPriceInput.setText("") 



    def addHotel(self):
            try:
                id = self.hotelIdInput.text()
                name = self.hotelNameInput.text()
                address = self.hotelAddressInput.text()
                price = self.hotelPriceInput.text()
                

                self.cursor.execute("INSERT INTO Hotels (id, name, address, price_pp) VALUES (?, ?, ?, ?)",
                                    (id, name, address, price))
                self.connection.commit()
                
                self.hide()
                self.finished.emit()
                self.input_clear()
                
            except ValueError:
                QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")    