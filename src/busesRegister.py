import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi


"""
    Window for registering new buses in the system.
    Allows users to add bus information including specifications, rental details,
    and contract information to the fleet management system.
    """
class BusesRegisterWindow(QMainWindow):
    finished = pyqtSignal()
    
    
    """
        Initializes the buses registration window.
        Loads the UI, connects to the database, and sets up event handlers for bus registration.
        """
    def __init__(self,):
        super().__init__()

        loadUi('ui/BusesRegister.ui', self)

        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.add_Buses_button.clicked.connect(self.addBus)

    
    """
        Clears all input fields in the bus registration form.
        Resets the form to its initial state after successful bus registration.
        """
    def input_clear(self):
        self.PlateNumberInput.setText("")
        self.ModelInput.setText("")
        self.YearInput.setText("")
        self.MileageInput.setText("")
        self.Rental_CostInput.setText("")
        self.ConsumptionInput.setText("")
        self.SeatsInput.setText("")

    """
        Creates a new bus record in the database.
        Validates input fields, retrieves form data including plate number, model,
        specifications, and rental information. Inserts the bus data with 'Available' status.
        Shows warning messages for invalid input or database constraint violations.
        """
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
            if plateNumber == "":
                raise ValueError("Plate number cannot be empty")
            self.connection.commit()
            self.hide()
            self.finished.emit()
            self.input_clear()
        except ValueError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Warning", "Εσφαλμενα στοιχεια")   