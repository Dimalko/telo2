import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi



class BusesRegisterWindow(QMainWindow):
    finished = pyqtSignal()
    
    
    
    def __init__(self,):
        super().__init__()

        loadUi('ui/BusesRegister.ui', self)

        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Buses_button.clicked.connect(self.addBus)


    def input_clear(self):
        self.PlateNumberInput.setText("")
        self.ModelInput.setText("")
        self.YearInput.setText("")
        self.MileageInput.setText("")
        self.Rental_CostInput.setText("")
        self.ConsumptionInput.setText("")
        self.SeatsInput.setText("")


    def addBus(self):
        try:
            plateNumber = self.PlateNumberInput.text()
            model = self.ModelInput.text()
            year = self.YearInput.text()
            mileage = float(self.MileageInput.text())
            company = self.CompanyComboBox.currentText()
            rental_cost = float(self.Rental_CostInput.text())
            consumption = float(self.ConsumptionInput.text())
            seats = float(self.SeatsInput.text())
            date = self.Contract_Date_dateEdit.date().toString("yyyy-MM-dd")  # Assuming your QDateEdit is named DateEdit
            status = "Available"

            self.cursor.execute("INSERT INTO Buses (plate_number, model, year, mileage,company, rental_cost, consumption, seats, status,contract_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?)",
                                (plateNumber, model, year, mileage,company, rental_cost, consumption, seats, status,date))
            self.connection.commit()
            self.hide()
            self.finished.emit()
            self.input_clear()
        except ValueError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")   