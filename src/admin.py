import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QListWidgetItem,QMessageBox
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
        #Create Tour Description Button
        self.createTourDescriptionBtn.clicked.connect(self.createTourDescription)
        self.TourlistWidget.itemClicked.connect(self.on_tour_selected)
        self.driverComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        self.vehicleComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        self.guideComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        self.driverComboBox.currentIndexChanged.connect(self.calculate_all_costs)
        # Τέλος load_comboboxes_for_tour
        self.driverComboBox.setCurrentIndex(0)
        self.vehicleComboBox.setCurrentIndex(0)
        self.guideComboBox.setCurrentIndex(0)
        #Accept/Decline Tour Buttons
        self.acceptTourButton.clicked.connect(self.accept_tour)
        self.declineTourButton.clicked.connect(self.decline_tour)



    #Populate Tables/Lists
        self.populate_tour_table()
        self.populate_travelagent_table()
        self.populate_teamleader_table()
        self.populate_driver_table()
        self.populate_buses_table()
        self.populate_hotels_table()
        self.loadFreeTours()

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
        self.populate_table.populate_table(self.tourTableWidget, "SELECT * FROM Tours", 10, 2)
        
    def populate_travelagent_table(self):
        self.populate_table.populate_table(self.travelagentTableWidget, "SELECT * FROM Staff WHERE role='Travel_Agent'", 8)
    
    def populate_teamleader_table(self):
        self.populate_table.populate_table(self.teamleaderTableWidget, "SELECT * FROM TeamLeaders", 5)  
    
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

            

    def calculate_guide_cost(self, guide_row, tour_days):
        monthly_salary = guide_row[3]
        working_days_month = 22  # όπως στους οδηγούς
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
            """)
            for tid, f_name, l_name in self.cursor.fetchall():
                full_name = f"{f_name} {l_name}"
                self.guideComboBox.addItem(full_name, tid)

        except Exception as e:
            print("Error loading comboboxes:", e)


    
    def calculate_all_costs(self):
        try:
            tour_id = self.selected_tour_id

            self.cursor.execute("SELECT start_date, end_date, km FROM Tours WHERE id = ?", (tour_id,))
            result = self.cursor.fetchone()
            if not result:
                return
            start_date, end_date, tour_km = result
            tour_days = self.calculate_tour_days(start_date, end_date)

            driver_code = self.driverComboBox.currentData()
            if driver_code:
                self.cursor.execute("SELECT * FROM Drivers WHERE tax_code = ?", (driver_code,))
                driver_row = self.cursor.fetchone()
                driver_cost = self.calculate_driver_cost(driver_row, tour_days)
            else:
                driver_cost = 0.0

            vehicle_plate = self.vehicleComboBox.currentData()
            if vehicle_plate and vehicle_plate not in ['Boat', 'Airplane']:
                self.cursor.execute("SELECT * FROM Buses WHERE plate_number = ?", (vehicle_plate,))
                bus_row = self.cursor.fetchone()
                vehicle_cost = self.calculate_bus_cost(bus_row, tour_km)
            else:
                vehicle_cost = 0.0

            guide_id = self.guideComboBox.currentData()
            if guide_id:
                self.cursor.execute("SELECT * FROM TeamLeaders WHERE id = ?", (guide_id,))
                guide_row = self.cursor.fetchone()
                guide_cost = self.calculate_guide_cost(guide_row, tour_days)
            else:
                guide_cost = 0.0

            total_service_cost = driver_cost + vehicle_cost + guide_cost

            self.cursor.execute("SELECT SUM(cost) FROM Reservations WHERE tour_id = ?", (tour_id,))
            total_income = self.cursor.fetchone()[0] or 0.0

            if total_income > 0:
                profit_amount = total_income - total_service_cost
                profit_percent = (profit_amount / total_income) * 100
            else:
                profit_amount = 0
                profit_percent = 0

            self.driverCostLabel.setText(f"Driver Cost: €{driver_cost:.2f}")
            self.vehicleCostLabel.setText(f"Vehicle Cost: €{vehicle_cost:.2f}")
            self.guideCostLabel.setText(f"Guide Cost: €{guide_cost:.2f}")
            self.totalCostLabel.setText(f"Total Cost: €{total_service_cost:.2f}")
            self.profitLabel.setText(f"Profit: €{profit_amount:.2f} ({profit_percent:.1f}%)")

        except Exception as e:
            print("Error calculating all costs:", e)

    def accept_tour(self):
        try:
            if not hasattr(self, "selected_tour_id"):
                return

            tour_id = self.selected_tour_id
            self.cursor.execute("UPDATE Tours SET status = 'Accepted' WHERE id = ?", (tour_id,))
            self.connection.commit()
            QMessageBox.information(self, "Success", f"Tour {tour_id} has been accepted.")
            self.loadFreeTours()
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


                
    
    #Create Tour Description Window
    def createTourDescription(self):
        self.open_createDescription.emit()
        self.createDescriptionShow.show()

    



#!REMOVE BEFORE FINAL VERSION------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())