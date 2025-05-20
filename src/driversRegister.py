import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi


class DriverRegisterWindow(QMainWindow):
    finished = pyqtSignal()

    def __init__(self,):
        super().__init__()

        loadUi('ui/DriversRegister.ui', self)

        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Driver_button.clicked.connect(self.addDriver)



    def input_clear(self):
        self.IdInput.setText("")
        self.FirstNameInput.setText("")
        self.LastNameInput.setText("")
        self.PaymentInput.setText("")


    def addDriver(self):
        try:
            id = self.IdInput.text()
            firstName = self.FirstNameInput.text()
            lastName = self.LastNameInput.text()
            payment = float(self.PaymentInput.text())
            type = self.TypeComboBox.currentText()
            status = "Available"

            self.cursor.execute("INSERT INTO Drivers (tax_code, f_name, l_name,type,salary,status) VALUES (?, ?, ?, ?, ?,?)",
                                (id, firstName, lastName,type, payment, status))
            if id != "":
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