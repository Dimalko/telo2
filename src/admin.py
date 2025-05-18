import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QListWidgetItem,QMessageBox, QDialog, QDialogButtonBox, QFormLayout, QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

from travelAgentRegister import TravelAgentRegisterWindow
from delete import DeleteWindow
from teamleaderRegister import TeamLeaderRegisterWindow
from driversRegister import DriverRegisterWindow
from busesRegister import BusesRegisterWindow
from toursRegister import ToursRegisterWindow
from hotelRegister import HotelRegisterWindow
from createDescription import CreateTourDescriptionWindow

from classes.populate_table import PopulateTable


class AdminWindow(QMainWindow):
    open_TravelAgentReg = pyqtSignal()
    open_TeamLeaderReg = pyqtSignal()
    open_DriverReg = pyqtSignal()
    open_BusReg = pyqtSignal()
    open_TourReg = pyqtSignal()
    open_HotelReg = pyqtSignal()
    open_createDescription = pyqtSignal()
    open_delete = pyqtSignal()
    switch_login = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
    # Load the UI file
        loadUi('ui//admin.ui', self)

    #add style to ui
        self.uiStyle()
        
    #connect db
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

    #initialize classes
        self.populate_table = PopulateTable()

    #Connect Buttons
        #Navigation Buttons
        self.homeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.requestBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.ongoingBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.staffBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.vehiclesBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.hotelsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.statsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        #Add Buttons
        self.add_Travel_Agent_button.clicked.connect(self.addTravelAgent)
        self.add_Team_Leader_button.clicked.connect(self.addTeamLeader)
        self.add_Driver_Button.clicked.connect(self.addDriver)
        self.Add_Buses_Button.clicked.connect(self.addBus)
        self.add_Tour_button.clicked.connect(self.addTour)
        self.addHotelBtn.clicked.connect(self.addHotel)
        #Remove Buttons
        self.removeAgentBtn.clicked.connect(self.removeAgent)
        self.removeTourBtn.clicked.connect(self.removeTour)
        self.removeTeamLeaderBtn.clicked.connect(self.removeTeamLeader)
        self.removeDriverBtn.clicked.connect(self.removeDriver)
        self.removeBusBtn.clicked.connect(self.removeBus)
        self.removeHotelBtn.clicked.connect(self.removeHotel)
        #Edit Buttons
        teq = """
                UPDATE Tours 
                SET destination=?, start_date=?, end_date=?, description=?, km=?, agent=?, transportation=?, status=?, activities=? 
                WHERE id=?
             """
        self.editTourBtn.clicked.connect(lambda: self.editSelectedRow(self.tourTableWidget, teq, 2, readonly_fields=["Id"]))
        aeq = """
                UPDATE Staff 
                SET username=?, password=?, f_name=?, l_name=?, role=?, work_hours=?, salary=?
                WHERE id=?
             """
        self.editAgentBtn.clicked.connect(lambda: self.editSelectedRow(self.travelagentTableWidget, aeq, readonly_fields=["Id"]))
        leq = """
                UPDATE TeamLeaders 
                SET f_name=?, l_name=?, payment=?, skills=?, status=?
                WHERE id=?
             """
        self.editLeaderBtn.clicked.connect(lambda: self.editSelectedRow(self.teamleaderTableWidget, leq, readonly_fields=["Id"]))
        deq = """
                UPDATE Drivers 
                SET f_name=?, l_name=?, type=?, salary=?, status=?
                WHERE tax_code=?
             """
        self.editDriverBtn.clicked.connect(lambda: self.editSelectedRow(self.driverTableWidget, deq, readonly_fields=["Tax Code"]))
        veq = """
                UPDATE Buses 
                SET model=?, year=?, mileage=?, company=?, rental_cost=?, consumption=?, seats=?, status=?, contract_date=?
                WHERE plate_number=?
             """
        self.editVehicleBtn.clicked.connect(lambda: self.editSelectedRow(self.busesTableWidget, veq, readonly_fields=["Plate Number"]))
        heq = """
                UPDATE Hotels 
                SET name=?, city=?, address=?, price_pp=?
                WHERE id=?
             """
        self.editHotelBtn.clicked.connect(lambda: self.editSelectedRow(self.hotelTableWidget, heq, readonly_fields=["Id"]))
        #Create Tour Description Button
        self.createTourDescriptionBtn.clicked.connect(self.createTourDescription)
        #Reservation Buttons
        self.TourlistWidget.itemClicked.connect(self.on_tour_selected)
        self.driverComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        self.vehicleComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        self.guideComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        self.driverComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        self.guideComboBox.currentIndexChanged.connect(self.calculate_all_costs)

        # Τέλος load_comboboxes_for_tour
        self.driverComboBox.setCurrentIndex(0)
        self.vehicleComboBox.setCurrentIndex(0)
        self.guideComboBox.setCurrentIndex(0)
        #Accept/Decline Tour Buttons
        self.acceptTourButton.clicked.connect(self.accept_tour)
        self.declineTourButton.clicked.connect(self.decline_tour)
        #---------------
        #LogOut Button
        self.logOutBtn.clicked.connect(self.to_login_window)
        #---------------
        self.ongoingTourListWidget.itemClicked.connect(self.on_ongoing_tour_selected)
        self.ongoingTourListWidget.itemClicked.connect(self.on_ongoing_tour_selected)
        self.guideComboBox.currentIndexChanged.connect(lambda: self.calculate_all_costs())
        self.driverComboBox.currentIndexChanged.connect(lambda: self.calculate_all_costs())
        self.vehicleComboBox.currentIndexChanged.connect(lambda: self.calculate_all_costs())

        #Complete Tour Button 
        self.completeTourButton.clicked.connect(self.complete_tour)







    #Populate Tables/Lists
        self.populate_tour_table()
        self.populate_travelagent_table()
        self.populate_teamleader_table()
        self.populate_driver_table()
        self.populate_buses_table()
        self.populate_hotels_table()
        self.loadFreeTours()
        self.loadOngoingTours()
        #self.loadOngoingTourDetails()

    #Connect Other Windows
        self.TravelAgentRegister = TravelAgentRegisterWindow()
        self.TravelAgentRegister.finished.connect(lambda: self.update_table("Agents"))  

        self.TeamLeaderRegister = TeamLeaderRegisterWindow()
        self.TeamLeaderRegister.finished.connect(lambda: self.update_table("TeamLeaders")) 

        self.DriverRegister = DriverRegisterWindow()
        self.DriverRegister.finished.connect(lambda: self.update_table("Drivers"))

        self.BusRegister = BusesRegisterWindow()
        self.BusRegister.finished.connect(lambda: self.update_table("Buses"))

        self.ToursRegister = ToursRegisterWindow()
        self.ToursRegister.finished.connect(lambda: self.update_table("Tours"))

        self.HotelRegister = HotelRegisterWindow()
        self.HotelRegister.finished.connect(lambda: self.update_table("Hotels"))
        
        seller_query = "DELETE FROM Staff WHERE id = ?"
        seller_labelText = "Travel Agent id:"
        self.removeAgentShow = DeleteWindow(seller_query, seller_labelText, True)
        self.removeAgentShow.finished.connect(lambda: self.update_table("Agents"))
        
        tour_query = "DELETE FROM Tours WHERE id = ?"
        tour_labelText = "Tour id:"
        self.removeTourShow = DeleteWindow(tour_query, tour_labelText, True)
        self.removeTourShow.finished.connect(lambda: self.update_table("Tours"))

        tLeader_query = "DELETE FROM TeamLeaders WHERE id = ?"
        tLeader_labelText = "Team Leader id:"
        self.removeTeamLeaderShow = DeleteWindow(tLeader_query, tLeader_labelText, True)
        self.removeTeamLeaderShow.finished.connect(lambda: self.update_table("TeamLeaders"))

        driver_query = "DELETE FROM Drivers WHERE tax_code = ?"
        driver_labelText = "Driver id:"
        self.removeDriverShow = DeleteWindow(driver_query, driver_labelText, True)
        self.removeDriverShow.finished.connect(lambda: self.update_table("Drivers"))

        bus_query = "DELETE FROM Buses WHERE plate_number = ?"
        bus_labelText = "Plate Number:"
        self.removeBusShow = DeleteWindow(bus_query, bus_labelText, True)
        self.removeBusShow.finished.connect(lambda: self.update_table("Buses"))

        hotel_query = "DELETE FROM Hotels WHERE id = ?"
        hotel_labelText= "Hotel id:"
        self.removeHotelShow = DeleteWindow(hotel_query, hotel_labelText, True)
        self.removeHotelShow.finished.connect(lambda: self.update_table("Hotels"))

        self.createDescriptionShow = CreateTourDescriptionWindow()


#--Style----------   
    def uiStyle(self):
        pixmap = QPixmap("data//images//logo_image.png")
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.setStyleSheet("padding-top: 20px; padding-bottom: 20px;")


#--Update Tables After An Action----------
    def update_table(self, table_name):
        if table_name == 'Agents':
            self.populate_travelagent_table()
        elif table_name == 'Drivers':
            self.populate_driver_table()
        elif table_name == 'Buses':
            self.populate_buses_table()           
        elif table_name == 'TeamLeaders':
            self.populate_teamleader_table()    
        elif table_name == "Tours":
            self.populate_tour_table()
        elif table_name == "Hotels":
            self.populate_hotels_table()


#--Populate Tables----------  
    def populate_tour_table(self):
        self.populate_table.populate_table(self.tourTableWidget, "SELECT * FROM Tours", 11, 2)
        
    def populate_travelagent_table(self):
        self.populate_table.populate_table(self.travelagentTableWidget, "SELECT * FROM Staff WHERE role='Travel_Agent'", 8)
    
    def populate_teamleader_table(self):
        self.populate_table.populate_table(self.teamleaderTableWidget, "SELECT * FROM TeamLeaders", 6)  
    
    def populate_driver_table(self):
        self.populate_table.populate_table(self.driverTableWidget, "SELECT * FROM Drivers", 6)    
    
    def populate_buses_table(self):
        self.populate_table.populate_table(self.busesTableWidget, "SELECT * FROM Buses", 10)

    def populate_hotels_table(self):
        self.populate_table.populate_table(self.hotelTableWidget, "SELECT * FROM Hotels", 5)

    def loadFreeTours(self):
        self.TourlistWidget.clear()
        self.cursor.execute("SELECT id, destination FROM Tours WHERE status = 'Free'")
        tours = self.cursor.fetchall()

        for tour in tours:
            item = QListWidgetItem(f"{tour[0]} - {tour[1]}")
            item.setData(Qt.UserRole, tour[0])  # Αποθήκευση tour_id
            self.TourlistWidget.addItem(item)
    
#--Display Windows----------
    #Add Windows
    def addTravelAgent(self):
        self.open_TravelAgentReg.emit()
        self.TravelAgentRegister.show()
        self.populate_travelagent_table()
    
    def addTeamLeader(self):
        self.open_TeamLeaderReg.emit()
        self.TeamLeaderRegister.show()    
        self.populate_teamleader_table()  
    
    def addDriver(self):
        self.open_DriverReg.emit()
        self.DriverRegister.show()    
    
    def addBus(self):
        self.open_BusReg.emit()
        self.BusRegister.show()
    
    def addTour(self):
        self.open_TourReg.emit()
        self.ToursRegister.show()   

    def addHotel(self):
        self.open_HotelReg.emit()
        self.HotelRegister.show() 
    
    #Remove/Delete Windows
    def removeAgent(self):
        self.open_delete.emit()
        self.removeAgentShow.show()

    def removeTour(self):
        self.open_delete.emit()
        self.removeTourShow.show()
    
    def removeTeamLeader(self):
        self.open_delete.emit()
        self.removeTeamLeaderShow.show()

    def removeDriver(self):
        self.open_delete.emit()
        self.removeDriverShow.show()

    def removeBus(self):
        self.open_delete.emit()
        self.removeBusShow.show()

    def removeHotel(self):
        self.open_delete.emit()
        self.removeHotelShow.show()

    def load_tour_summary(self, tour_id):
        try:
            self.cursor.execute("""
                SELECT SUM(people_numb), SUM(cost)
                FROM Reservations
                WHERE tour_id = ? AND status = 'Active'
            """, (tour_id,))
            result = self.cursor.fetchone()

            self.tourSummaryTable.setRowCount(1)
            self.tourSummaryTable.setColumnCount(2)

            if not result or result[0] is None:
                self.tourSummaryTable.setItem(0, 0, QTableWidgetItem("No Reservations were made"))
                self.tourSummaryTable.setItem(0, 1, QTableWidgetItem("€0.00"))
                
            else:
                total_people = result[0]
                total_cost = result[1]
                self.tourSummaryTable.setItem(0, 0, QTableWidgetItem(str(total_people)))
                self.tourSummaryTable.setItem(0, 1, QTableWidgetItem(f"€{total_cost:.2f}"))

        except Exception as e:
            print("Error loading tour summary:", e)


    def on_tour_selected(self, item):
        try:
            tour_text = item.text()
            tour_id = tour_text.split(" ")[0].replace("#", "").strip()
            self.selected_tour_id = tour_id

            self.load_tour_summary(tour_id)
            self.load_comboboxes_for_tour(tour_id)
            self.calculate_all_costs()

        except Exception as e:
            print("Error selecting tour:", e)

            

    def calculate_guide_cost(self, monthly_salary, tour_days):
        working_days_month = 22
        return (monthly_salary / working_days_month) * tour_days

       


    def calculate_driver_cost(self, driver_row, tour_days):
        driver_type = driver_row[3]
        salary = driver_row[4]

        if driver_type == 'Freelancer':
            return salary * tour_days
        else:
            working_days_month = 22
            return (salary / working_days_month) * tour_days


    def calculate_bus_cost(self, bus_row, tour_km):
        rental_cost = bus_row[5] or 0
        consumption = bus_row[6]
        fuel_price_per_liter = 1.80

        fuel_cost = (tour_km * consumption / 100) * fuel_price_per_liter
        return rental_cost + fuel_cost
    

    def calculate_driver_cost(self, driver_row, tour_days):

        driver_type = driver_row[3]  # 'Permanent' or 'Freelancer'
        salary = driver_row[4]

        if driver_type == 'Freelancer':
            return salary * tour_days  # salary είναι ημερομίσθιο
        else:
            working_days_month = 22
            return (salary / working_days_month) * tour_days


    def calculate_tour_days(self, start_date, end_date):
        from datetime import datetime
        fmt = "%Y-%m-%d"
        start = datetime.strptime(start_date, fmt)
        end = datetime.strptime(end_date, fmt)
        return (end - start).days + 1


    def load_comboboxes_for_tour(self, tour_id):
        try:
            self.cursor.execute("SELECT transportation FROM Tours WHERE id = ?", (tour_id,))
            result = self.cursor.fetchone()
            if not result:
                return
            transportation = result[0].lower()

            self.driverComboBox.clear()
            self.vehicleComboBox.clear()
            self.guideComboBox.clear()

            if transportation == "bus":
                self.cursor.execute("""
                    SELECT tax_code, f_name, l_name 
                    FROM Drivers 
                    WHERE status = 'Available'
                """)
                for tax_code, f_name, l_name in self.cursor.fetchall():
                    full_name = f"{f_name} {l_name}"
                    self.driverComboBox.addItem(full_name, tax_code)

                self.cursor.execute("""
                    SELECT plate_number, model 
                    FROM Buses 
                    WHERE status = 'Available'
                """)
                for plate, model in self.cursor.fetchall():
                    display = f"{plate} - {model}"
                    self.vehicleComboBox.addItem(display, plate)

            elif transportation == "airplane":
                self.vehicleComboBox.addItem("Airplane", "Airplane")
            elif transportation == "boat":
                self.vehicleComboBox.addItem("Boat", "Boat")

            self.cursor.execute("""
                SELECT id, f_name, l_name 
                FROM TeamLeaders
                WHERE status = 'Available'
            """)
            for tid, f_name, l_name in self.cursor.fetchall():
                full_name = f"{f_name} {l_name}"
                self.guideComboBox.addItem(full_name, tid)

        except Exception as e:
            print("Error loading comboboxes:", e)




    def calculate_all_costs(self, return_values_only=False):
        try:
            tour_id = self.selected_tour_id

            self.cursor.execute("SELECT start_date, end_date, km, transportation FROM Tours WHERE id = ?", (tour_id,))
            result = self.cursor.fetchone()
            if not result:
                return None

            start_date, end_date, tour_km, transportation = result
            tour_days = self.calculate_tour_days(start_date, end_date)

            # Driver
            driver_code = self.driverComboBox.currentData()
            if driver_code:
                self.cursor.execute("SELECT * FROM Drivers WHERE tax_code = ?", (driver_code,))
                driver_row = self.cursor.fetchone()
                driver_cost = self.calculate_driver_cost(driver_row, tour_days)
            else:
                driver_cost = 0.0

            # Guide (διορθωμένο)
            guide_id = self.guideComboBox.currentData()
            if guide_id:
                self.cursor.execute("SELECT * FROM TeamLeaders WHERE id = ?", (guide_id,))
                guide_row = self.cursor.fetchone()
                if guide_row:
                    monthly_salary = guide_row[3]  # π.χ. payment στήλη
                    guide_cost = self.calculate_guide_cost(monthly_salary, tour_days)
                else:
                    guide_cost = 0.0
            else:
                guide_cost = 0.0

            # Vehicle or Transportation cost
            transportation = transportation.strip()
            if transportation == "Bus":
                vehicle_plate = self.vehicleComboBox.currentData()
                if vehicle_plate:
                    self.cursor.execute("SELECT * FROM Buses WHERE plate_number = ?", (vehicle_plate,))
                    bus_row = self.cursor.fetchone()
                    vehicle_cost = self.calculate_bus_cost(bus_row, tour_km)
                else:
                    vehicle_cost = 0.0
                vehicle_label = f"Vehicle Cost: €{vehicle_cost:.2f}"
            else:
                self.cursor.execute("SELECT SUM(people_numb) FROM Reservations WHERE tour_id = ? AND status = 'Active'", (tour_id,))
                total_people = self.cursor.fetchone()[0] or 0
                ticket_price = 120 if transportation == "Airplain" else 60 if transportation == "Boat" else 0
                vehicle_cost = ticket_price * total_people
                vehicle_label = f"Transportation Cost: €{vehicle_cost:.2f}"

            # Total business cost (exclude ticket cost if not Bus)
            if transportation == "Bus":
                total_service_cost = driver_cost + vehicle_cost + guide_cost
            else:
                total_service_cost = driver_cost + guide_cost

            # Total income
            self.cursor.execute("SELECT SUM(cost) FROM Reservations WHERE tour_id = ? AND status = 'Active'", (tour_id,))
            total_income = self.cursor.fetchone()[0] or 0.0

            if total_income > 0:
                profit_amount = total_income - total_service_cost
                profit_percent = (profit_amount / total_income) * 100
            else:
                profit_amount = 0.0
                profit_percent = 0.0

            #Στρογγυλοποίηση κοστων
            round(driver_cost, 2),
            round(guide_cost, 2),
            round(vehicle_cost, 2),
            round(total_service_cost, 2),
            round(total_income, 2),
            round(profit_amount, 2),
            round(profit_percent, 2)
            # Return results if requested
            if return_values_only:
                return {
                    "tour_id": tour_id,
                    "total_income": total_income,
                    "profit_amount": profit_amount,
                    "profit_percent": profit_percent,
                    "driver_cost": driver_cost,
                    "vehicle_cost": vehicle_cost,
                    "guide_cost": guide_cost,
                    "total_cost": total_service_cost
                }

            # Show on UI
            self.driverCostLabel.setText(f"Driver Cost: €{driver_cost:.2f}")
            self.vehicleCostLabel.setText(vehicle_label)
            self.guideCostLabel.setText(f"Guide Cost: €{guide_cost:.2f}")
            self.totalCostLabel.setText(f"Total Cost: €{total_service_cost:.2f}")
            self.profitLabel.setText(f"Profit: €{profit_amount:.2f} ({profit_percent:.1f}%)")

            return True

        except Exception as e:
            print("Error calculating all costs:", e)
            return False

    


    def accept_tour(self):
        try:
            if not hasattr(self, "selected_tour_id"):
                return

            tour_id = self.selected_tour_id

            # Υπολογισμός οικονομικών
            financials = self.calculate_all_costs(return_values_only=True)
            if not financials:
                QMessageBox.warning(self, "Error", "Could not calculate tour financials.")
                return

            # Πληροφορίες Tour
            self.cursor.execute("SELECT start_date, end_date, transportation, destination FROM Tours WHERE id = ?", (tour_id,))
            tour_data = self.cursor.fetchone()
            if not tour_data:
                return
            start_date, end_date, transportation, destination = tour_data

            # Επιλογές χρήστη
            driver_code = self.driverComboBox.currentData()
            vehicle_plate = self.vehicleComboBox.currentData()
            guide_id = self.guideComboBox.currentData()

            # Ενημέρωση προσωπικού
            if transportation == "Bus" and driver_code:
                self.cursor.execute("UPDATE Drivers SET status = 'Busy' WHERE tax_code = ?", (driver_code,))
                self.populate_driver_table()

            if transportation == "Bus" and vehicle_plate:
                self.cursor.execute("UPDATE Buses SET status = 'On Tour' WHERE plate_number = ?", (vehicle_plate,))
                self.cursor.execute("SELECT km FROM Tours WHERE id = ?", (tour_id,))
                result = self.cursor.fetchone()
                if result:
                    tour_km = result[0]
                    self.cursor.execute(
                        "UPDATE Buses SET mileage = mileage + ? WHERE plate_number = ?",
                        (tour_km, vehicle_plate)
                    )
                self.populate_buses_table()

            if guide_id:
                self.cursor.execute("UPDATE TeamLeaders SET status = 'Busy' WHERE id = ?", (guide_id,))
                self.populate_teamleader_table()

            # Update tour status
            self.cursor.execute("UPDATE Tours SET status = 'Accepted' WHERE id = ?", (tour_id,))

            # Transportation field (plate or string)
            transportation_value = vehicle_plate if transportation == "Bus" else transportation

            # Συμμετέχοντες
            self.cursor.execute("SELECT SUM(people_numb) FROM Reservations WHERE tour_id = ? AND status = 'Active'", (tour_id,))
            total_people = self.cursor.fetchone()[0] or 0

            # Εισαγωγή στον πίνακα TourFinancials
            self.cursor.execute("""
                INSERT OR REPLACE INTO TourFinancials (
                    tour_id, destination, start_date, end_date, total_income, participants,
                    transportation, transportation_cost, driver, guide,
                    driver_cost, guide_cost, vehicle_cost, total_cost,
                    profit_amount, profit_percent
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                tour_id,
                destination,
                start_date,
                end_date,
                round(financials["total_income"], 2),
                total_people,
                transportation_value,
                round(financials["vehicle_cost"], 2),
                driver_code if transportation == "Bus" else "",
                guide_id,
                round(financials["driver_cost"], 2),
                round(financials["guide_cost"], 2),
                round(financials["vehicle_cost"], 2),
                round(financials["total_cost"], 2),
                round(financials["profit_amount"], 2),
                round(financials["profit_percent"], 2)
            ))
            
            self.connection.commit()
            QMessageBox.information(self, "Success", f"Tour {tour_id} has been accepted.")

            self.loadFreeTours()
            self.loadOngoingTours()
            self.populate_tour_table()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not accept tour.\n{e}")
            self.connection.rollback()

    def decline_tour(self):
        try:
                if not hasattr(self, "selected_tour_id"):
                    return

                tour_id = self.selected_tour_id

                # Αλλαγή των κρατήσεων σε Cancelled
                self.cursor.execute("UPDATE Reservations SET status = 'Cancelled' WHERE tour_id = ?", (tour_id,))
                self.connection.commit()
                QMessageBox.information(self, "Declined", f"All reservations for tour {tour_id} were cancelled.")
                self.load_tour_summary(tour_id)
                self.calculate_all_costs()

        except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not decline tour.\n{e}")
                self.connection.rollback()



    def editSelectedRow(self, table_widget, query, q_num=1, readonly_fields=None):
        selected_row = table_widget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a row to edit.")
            return

        readonly_fields = readonly_fields or []

        dialog = QDialog(self)
        dialog.setWindowTitle("Edit")
        layout = QFormLayout(dialog)
        inputs = {}

        if q_num == 2:
            for col in range(table_widget.columnCount()-1):
                header = table_widget.horizontalHeaderItem(col).text()
                item = table_widget.item(selected_row, col)
                value = item.text() if item else ""

                field = QLineEdit(value)
                if header in readonly_fields:
                    field.setReadOnly(True)

                layout.addRow(f"{header}:", field)
                inputs[header] = field
        else:
            for col in range(table_widget.columnCount()):
                header = table_widget.horizontalHeaderItem(col).text()
                item = table_widget.item(selected_row, col)
                value = item.text() if item else ""

                field = QLineEdit(value)
                if header in readonly_fields:
                    field.setReadOnly(True)

                layout.addRow(f"{header}:", field)
                inputs[header] = field

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttons)

        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        if dialog.exec_() == QDialog.Accepted:
            updated_values = []
            id_value = None

            if q_num == 2:
                for col in range(table_widget.columnCount()-1):
                    header = table_widget.horizontalHeaderItem(col).text()
                    new_value = inputs[header].text()
                    if header in readonly_fields:
                        id_value = new_value
                    else:
                        updated_values.append(new_value)
                    table_widget.setItem(selected_row, col, QTableWidgetItem(new_value))
            else:
                for col in range(table_widget.columnCount()):
                    header = table_widget.horizontalHeaderItem(col).text()
                    new_value = inputs[header].text()
                    if header in readonly_fields:
                        id_value = new_value
                    else:
                        updated_values.append(new_value)
                    table_widget.setItem(selected_row, col, QTableWidgetItem(new_value))

            if id_value is None:
                QMessageBox.critical(self, "Error", "No ID value found.")
                return

            updated_values.append(id_value)

            try:
                self.cursor.execute(query, updated_values)
                self.connection.commit()
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to update database:\n{str(e)}")
                        

        


    def loadOngoingTours(self):
        self.ongoingTourListWidget.clear()
        self.cursor.execute("SELECT id, destination FROM Tours WHERE status = 'Accepted'")
        tours = self.cursor.fetchall()

        for tour_id, destination in tours:
            self.ongoingTourListWidget.addItem(f"{tour_id} - {destination}")


    def loadOngoingTourDetails(self, tour_id):
        try:
            self.ongoingTourDetailsTable.setRowCount(0)

            self.cursor.execute("""
                SELECT 
                    destination,
                    start_date || ' ➝ ' || end_date,
                    total_income,
                    participants,
                    transportation,
                    transportation_cost,
                    driver,
                    guide
                FROM TourFinancials
                WHERE tour_id = ?
            """, (tour_id,))

            result = self.cursor.fetchone()

            if result:
                self.ongoingTourDetailsTable.insertRow(0)
                for col, value in enumerate(result):
                    self.ongoingTourDetailsTable.setItem(0, col, QTableWidgetItem(str(value)))
            else:
                QMessageBox.warning(self, "No Data", "No financial data found for this tour.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load tour details.\n{e}")

    def on_ongoing_tour_selected(self, item):
        tour_text = item.text()
        tour_id = tour_text.split(" ")[0].strip()  # π.χ. "t12"
        self.selected_tour_id = tour_id
        self.loadOngoingTourDetails(tour_id)


    def complete_tour(self):
        try:
            selected_item = self.ongoingTourListWidget.currentItem()
            if not selected_item:
                QMessageBox.warning(self, "Warning", "No tour selected.")
                return

            tour_id = selected_item.text().split(" - ")[0].strip()

            # Πάρε Transportation και Driver από τον πίνακα TourFinancials
            self.cursor.execute("""
                SELECT transportation, driver, guide FROM TourFinancials WHERE tour_id = ?
            """, (tour_id,))
            result = self.cursor.fetchone()

            if not result:
                QMessageBox.warning(self, "Warning", "Tour information not found in TourFinancials.")
                return

            transportation, driver_code, guide_id = result

            # Αν είναι Bus (τότε transportation περιέχει πινακίδα)
            if transportation not in ["Airplain", "Boat"]:
                # Επαναφορά κατάστασης λεωφορείου
                self.cursor.execute("UPDATE Buses SET status = 'Available' WHERE plate_number = ?", (transportation,))
                
                # Επαναφορά οδηγού (αν υπάρχει)
                if driver_code:
                    self.cursor.execute("UPDATE Drivers SET status = 'Available' WHERE tax_code = ?", (driver_code,))

            # Επαναφορά ξεναγού (αν υπάρχει)
            if guide_id:
                self.cursor.execute("UPDATE TeamLeaders SET status = 'Available' WHERE id = ?", (guide_id,))

            # Ενημέρωση του status του Tour
            self.cursor.execute("UPDATE Tours SET status = 'Completed' WHERE id = ?", (tour_id,))

            # ✅ Ενημέρωση όλων των κρατήσεων σε Completed
            self.cursor.execute("""
                UPDATE Reservations SET status = 'Completed' WHERE tour_id = ? AND status = 'Active'
            """, (tour_id,))
            self.loadOngoingTours()
            self.populate_teamleader_table()
            self.populate_driver_table()
            self.populate_buses_table()
            self.connection.commit()
            QMessageBox.information(self, "Success", f"Tour {tour_id} has been completed.")
            self.loadFreeTours()
            self.populate_tour_table()
            self.ongoingTourDetailsTable.setRowCount(0)


        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to complete tour.\n{e}")
            self.connection.rollback()




             
    
    #Create Tour Description Window
    def createTourDescription(self):
        self.open_createDescription.emit()
        self.createDescriptionShow.show()
        
    

#--LogOut----------
    def to_login_window(self):
        from login import LoginWindow
        login_window_instance = LoginWindow()
        login_window_instance.show()
        self.hide()
        self.login_window_instance = login_window_instance

    



#!REMOVE BEFORE FINAL VERSION------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())