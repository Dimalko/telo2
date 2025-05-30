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
from classes.piechart import PieChart
from classes.barchart import BarChart


""" Main window for the admin interface.
    This class handles the main functionalities of the admin interface,
    including adding, editing, and removing travel agents, team leaders, drivers, buses, tours, and hotels.
    It also provides statistics and charts for tours, drivers, and team leaders.
    The class uses PyQt5 for the GUI and SQLite for the database connection.
    Signals are used to communicate with other windows and components.
"""
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
    tourPiec = PieChart()
    tourBarc = BarChart()
    busBarc = BarChart()
    driversBarc = BarChart()
    leadersBarc = BarChart()
    driversDestPiec = PieChart()
    leadersDestPiec = PieChart()


    """ Initializes the AdminWindow class.
        Sets up the UI, connects to the database, initializes classes for populating tables and creating charts,
        and creates statistics for tours, drivers, and team leaders.
        :param self: The instance of the class. 
        This method also connects buttons to their respective functions and populates tables and lists with data.    
        It handles the navigation between different sections of the admin interface and manages the display of statistics.    
        It also connects to other windows for adding, editing, and removing travel agents, team leaders, drivers, buses, tours, and hotels.
    """
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

    #create stats
        tourPieQuery =  """
                        SELECT CASE 
                        WHEN transportation IN (SELECT plate_number FROM Buses) THEN 'Bus'
                        ELSE transportation
                        END AS transport_type,
                        COUNT(*) AS count
                        FROM TourFinancials
                        GROUP BY transport_type
                        """
        self.tourPiec.create_piechart(tourPieQuery, self.toursPie)

        tourBarQuery =  """
                        SELECT destination, SUM(profit_amount) AS total_profit
                        FROM TourFinancials
                        GROUP BY destination
                        ORDER BY total_profit DESC
                        """
        self.tourBarc.create_barchart(tourBarQuery, self.toursBar)
        
        busBarQuery =   """
                        SELECT transportation AS bus_plate, COUNT(*) AS total_tours
                        FROM TourFinancials
                        WHERE transportation NOT IN ('Airplain', 'Boat')
                        GROUP BY transportation
                        ORDER BY total_tours DESC
                        """
        self.busBarc.create_barchart(busBarQuery, self.busBar)

        driversBarQuery =   """
                            SELECT driver, COUNT(*) AS total_tours
                            FROM TourFinancials
                            WHERE driver != ''
                            GROUP BY driver
                            ORDER BY total_tours DESC
                            """
        self.driversBarc.create_barchart(driversBarQuery, self.driversBar)

        leadersBarQuery =   """
                            SELECT tl.id, COUNT(tf.tour_id) AS total_tours
                            FROM TourFinancials tf
                            JOIN TeamLeaders tl ON tf.guide = tl.id
                            GROUP BY tl.id
                            ORDER BY total_tours DESC
                            """
        self.leadersBarc.create_barchart(leadersBarQuery, self.leadersBar)

        avgPlpTourQuery =   """
                            SELECT AVG(participants) 
                            FROM TourFinancials
                            """
        self.create_label_stats(avgPlpTourQuery, self.avgPeoplePTLbl)

        mostProfTourQuery = """
                            SELECT tour_id, destination, profit_amount
                            FROM TourFinancials
                            ORDER BY profit_amount DESC
                            LIMIT 1
                            """
        self.create_label_stats(mostProfTourQuery, self.mostProfTourLbl)

        tourWithMostPplQuery =  """
                                SELECT tour_id, destination, participants
                                FROM TourFinancials
                                ORDER BY participants DESC
                                LIMIT 1
                                """
        self.create_label_stats(tourWithMostPplQuery, self.tourWthMosPplLbl)

        driverWithMostKmQuery = """
                                SELECT d.tax_code, d.f_name || ' ' || d.l_name AS name, SUM(t.km) AS total_km
                                FROM TourFinancials tf
                                JOIN Drivers d ON tf.driver = d.tax_code
                                JOIN Tours t ON tf.tour_id = t.id
                                GROUP BY d.tax_code
                                ORDER BY total_km DESC
                                LIMIT 1
                                """
        self.create_label_stats(driverWithMostKmQuery, self.driverWithMostKmLbl)

        leastExpensiveDriverQuery = """
                                    SELECT tax_code, f_name || ' ' || l_name AS name, MIN(salary / 22.0) AS cost_per_day
                                    FROM Drivers
                                    WHERE type = 'Permanent'
                                    """
        self.create_label_stats(leastExpensiveDriverQuery, self.leastExpensiveDriverLbl)

        teamLeadersWithMostToursQuery = """
                                        SELECT tl.id, tl.f_name || ' ' || tl.l_name AS name, COUNT(tf.tour_id) AS total_tours
                                        FROM TourFinancials tf
                                        JOIN TeamLeaders tl ON tf.guide = tl.id
                                        GROUP BY tl.id
                                        ORDER BY total_tours DESC
                                        LIMIT 1
                                        """
        self.create_label_stats(teamLeadersWithMostToursQuery, self.leaderWithMostTourLbl)

        leastExpensiveLeaderQuery = """
                                    SELECT id, f_name || ' ' || l_name AS name, ROUND(payment / 22.0, 2) AS cost_per_day
                                    FROM TeamLeaders
                                    ORDER BY cost_per_day ASC
                                    LIMIT 1
                                    """
        self.create_label_stats(leastExpensiveLeaderQuery, self.leastExpensiveLeaderLbl)


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
        #Load Drivers/Team Leaders
       
        
        #LogOut Button
        self.logOutBtn.clicked.connect(self.to_login_window)

        self.ongoingTourListWidget.itemClicked.connect(self.on_ongoing_tour_selected)
        self.ongoingTourListWidget.itemClicked.connect(self.on_ongoing_tour_selected)
        self.guideComboBox.currentIndexChanged.connect(lambda: self.calculate_all_costs())
        self.driverComboBox.currentIndexChanged.connect(lambda: self.calculate_all_costs())
        self.vehicleComboBox.currentIndexChanged.connect(lambda: self.calculate_all_costs())
        
        #Stats List Selection
        driversFavPieQuery =    """
                                SELECT destination, COUNT(*) AS times
                                FROM TourFinancials
                                WHERE driver = ?
                                GROUP BY destination
                                ORDER BY times DESC
                                LIMIT 3
                                """
        driversTourHistoryQuery =   """
                                    SELECT tour_id, destination, driver_cost
                                    FROM TourFinancials
                                    WHERE driver = ?
                                    """
        self.driverStatsListWidget.itemClicked.connect(lambda item: self.select_list_stats(item, self.driversDestPiec, self.driversFavPie, self.driverTourStatList, driversFavPieQuery, driversTourHistoryQuery))
        
        leadersFavPieQuery =    """
                                SELECT destination, COUNT(*) AS times
                                FROM TourFinancials
                                WHERE guide = ?
                                GROUP BY destination
                                ORDER BY times DESC
                                LIMIT 3
                                """
        leadersTourHistoryQuery =   """
                                    SELECT tour_id, destination, driver_cost
                                    FROM TourFinancials
                                    WHERE guide = ?
                                    """
        self.leaderStatsListWidget.itemClicked.connect(lambda item: self.select_list_stats(item, self.leadersDestPiec, self.leadersFavPie, self.leaderTourStatList, leadersFavPieQuery, leadersTourHistoryQuery))
        
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

        driverStatsListQuery =  """
                                SELECT tax_code, f_name || ' ' || l_name AS name
                                FROM Drivers
                                """
        self.load_stats_lists(self.driverStatsListWidget, driverStatsListQuery)


        leaderStatsListQuery =  """
                                SELECT id, f_name || ' ' || l_name AS name
                                FROM TeamLeaders
                                """
        self.load_stats_lists(self.leaderStatsListWidget, leaderStatsListQuery)

        #Search
        searchDriversQuery = """
                             SELECT tax_code, f_name || ' ' || l_name AS name
                             FROM Drivers
                             WHERE f_name LIKE ? OR l_name LIKE ? OR tax_code LIKE ?
                             """
        self.driverslineEdit.textChanged.connect(lambda: self.filterStatLists(driverStatsListQuery, searchDriversQuery, self.driverslineEdit, self.driverStatsListWidget))

        searchLeadersQuery = """
                             SELECT id, f_name || ' ' || l_name AS name
                             FROM TeamLeaders
                             WHERE f_name LIKE ? OR l_name LIKE ? OR id LIKE ?
                             """
        self.teamleaderslineEdit.textChanged.connect(lambda: self.filterStatLists(leaderStatsListQuery, searchLeadersQuery, self.teamleaderslineEdit, self.leaderStatsListWidget))


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
    """ Applies a custom style to the UI elements.
        This method sets the logo image and applies padding to the logo label.
        :param self: The instance of the class.
    """   
    def uiStyle(self):
        pixmap = QPixmap("data//images//logo_image.png")
        self.logoLabel.setPixmap(pixmap)
        self.logoLabel.setStyleSheet("padding-top: 20px; padding-bottom: 20px;")


#--Update Tables After An Action----------
    """ Updates the specified table after an action is performed.
        This method checks which table needs to be updated based on the provided table name
        and calls the corresponding populate method to refresh the table data.
        :param self: The instance of the class.
        :param table_name: The name of the table to be updated.
    """
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
    """ Populates the tour table with data from the database.
        This method executes a SQL query to fetch all tours and fills the tour table widget with the results.
        :param self: The instance of the class.
    """  
    def populate_tour_table(self):
        self.populate_table.populate_table(self.tourTableWidget, "SELECT * FROM Tours", 11, 2)


    """ Populates the travel agent table with data from the database.
        This method executes a SQL query to fetch all travel agents and fills the travel agent table widget with the results.
        :param self: The instance of the class.
    """    
    def populate_travelagent_table(self):
        self.populate_table.populate_table(self.travelagentTableWidget, "SELECT * FROM Staff WHERE role='Travel_Agent'", 8)


    """ Populates the team leader table with data from the database.
        This method executes a SQL query to fetch all team leaders and fills the team leader table widget with the results.
        :param self: The instance of the class.
    """
    def populate_teamleader_table(self):
        self.populate_table.populate_table(self.teamleaderTableWidget, "SELECT * FROM TeamLeaders", 6)  


    """ Populates the driver table with data from the database.
        This method executes a SQL query to fetch all drivers and fills the driver table widget with the results.
        :param self: The instance of the class.
    """
    def populate_driver_table(self):
        self.populate_table.populate_table(self.driverTableWidget, "SELECT * FROM Drivers", 6)    


    """ Populates the buses table with data from the database.
        This method executes a SQL query to fetch all buses and fills the buses table widget with the results.
        :param self: The instance of the class.
    """
    def populate_buses_table(self):
        self.populate_table.populate_table(self.busesTableWidget, "SELECT * FROM Buses", 10)


    """ Populates the hotels table with data from the database.
        This method executes a SQL query to fetch all hotels and fills the hotel table widget with the results.
        :param self: The instance of the class.
    """
    def populate_hotels_table(self):
        self.populate_table.populate_table(self.hotelTableWidget, "SELECT * FROM Hotels", 5)


    """ Loads the ongoing tours into the ongoing tour list widget.
        This method clears the existing items in the list widget and fetches ongoing tours from the database,
        adding each tour as an item in the list widget with its ID and destination.
        :param self: The instance of the class.
    """
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
    """ Opens the travel agent registration window and populates the travel agent table."""
    def addTravelAgent(self):
        self.open_TravelAgentReg.emit()
        self.TravelAgentRegister.show()
        self.populate_travelagent_table()

    """ Opens the team leader registration window and populates the team leader table."""
    def addTeamLeader(self):
        self.open_TeamLeaderReg.emit()
        self.TeamLeaderRegister.show()    
        self.populate_teamleader_table()  

    """ Opens the driver registration window and populates the driver table."""
    def addDriver(self):
        self.open_DriverReg.emit()
        self.DriverRegister.show()   

    """ Opens the bus registration window and populates the bus table."""
    def addBus(self):
        self.open_BusReg.emit()
        self.BusRegister.show()

    """ Opens the tour registration window and populates the tour table."""
    def addTour(self):
        self.open_TourReg.emit()
        self.ToursRegister.show()  

    """ Opens the hotel registration window and populates the hotel table."""
    def addHotel(self):
        self.open_HotelReg.emit()
        self.HotelRegister.show() 
    
    #Remove/Delete Windows
    """ Opens the remove agent window for deleting a travel agent."""
    def removeAgent(self):
        self.open_delete.emit()
        self.removeAgentShow.show()

    """ Opens the remove tour window for deleting a tour."""
    def removeTour(self):
        self.open_delete.emit()
        self.removeTourShow.show()

    """ Opens the remove team leader window for deleting a team leader."""
    def removeTeamLeader(self):
        self.open_delete.emit()
        self.removeTeamLeaderShow.show()

    """ Opens the remove driver window for deleting a driver."""
    def removeDriver(self):
        self.open_delete.emit()
        self.removeDriverShow.show()

    """ Opens the remove bus window for deleting a bus."""
    def removeBus(self):
        self.open_delete.emit()
        self.removeBusShow.show()

    """ Opens the remove hotel window for deleting a hotel."""
    def removeHotel(self):
        self.open_delete.emit()
        self.removeHotelShow.show()

    #Create Tour Description Window
    """ Opens the create tour description window for creating a description for a tour."""
    def createTourDescription(self):
        self.open_createDescription.emit()
        self.createDescriptionShow.show()



#--Functions To Categorize!!!----------
    """ Loads the tour summary into the tour summary table.
        This method executes a SQL query to calculate the total number of people and total cost for the specified tour.
        It updates the tour summary table with the results, displaying "No Reservations were made" if there are no active reservations.
        :param self: The instance of the class.
        :param tour_id: The identifier of the selected tour.
    """
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


    """ Triggered when an ongoing tour is selected from the list.
        Loads ongoing tour details, updates related UI components, and calculates costs.
        Args:
        item (QListWidgetItem): The selected item from the ongoing tour list.
    """
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
    

    """ Calculates the cost for a guide based on their monthly salary and the number of tour days.
        This method takes the monthly salary of the guide and the number of days for the tour,
        and calculates the cost based on a standard working month of 22 days.
        :param self: The instance of the class.
        :param monthly_salary: The monthly salary of the guide.
        :param tour_days: The number of days for the tour.
        :return: The calculated cost for the guide.
    """
    def calculate_guide_cost(self, monthly_salary, tour_days):
        working_days_month = 22
        return (monthly_salary / working_days_month) * tour_days
    

    """Calculates the cost for a bus based on its rental cost, fuel consumption, and the distance of the tour.
        This method takes the bus row data and the total kilometers for the tour,
        and calculates the total cost including rental cost and fuel cost.
        :param self: The instance of the class.
        :param bus_row: The row data of the bus from the database.
        :param tour_km: The total kilometers for the tour.
        :return: The total cost for the bus.
    """
    def calculate_bus_cost(self, bus_row, tour_km):
        rental_cost = bus_row[5] or 0
        consumption = bus_row[6]
        fuel_price_per_liter = 1.80

        fuel_cost = (tour_km * consumption / 100) * fuel_price_per_liter
        return rental_cost + fuel_cost
    

    """ Calculates the cost for a driver based on their type (Permanent or Freelancer) and the number of tour days.
        This method takes the driver row data and the number of days for the tour,
        and calculates the cost based on whether the driver is a freelancer (paid per day) or a permanent employee (paid monthly).
        :param self: The instance of the class.
        :param driver_row: The row data of the driver from the database.
        :param tour_days: The number of days for the tour.
        :return: The total cost for the driver.
    """
    def calculate_driver_cost(self, driver_row, tour_days):

        driver_type = driver_row[3]  # 'Permanent' or 'Freelancer'
        salary = driver_row[4]

        if driver_type == 'Freelancer':
            return salary * tour_days  # salary είναι ημερομίσθιο
        else:
            working_days_month = 22
            return (salary / working_days_month) * tour_days


    """ Calculates the number of days for a tour based on the start and end dates.
        This method takes the start and end dates of the tour in the format "YYYY-MM-DD",
        and calculates the total number of days for the tour, including both start and end dates.
        :param self: The instance of the class.
        :param start_date: The start date of the tour in "YYYY-MM-DD" format.
        :param end_date: The end date of the tour in "YYYY-MM-DD" format.
        :return: The total number of days for the tour.
    """
    def calculate_tour_days(self, start_date, end_date):
        from datetime import datetime
        fmt = "%Y-%m-%d"
        start = datetime.strptime(start_date, fmt)
        end = datetime.strptime(end_date, fmt)
        return (end - start).days + 1
    

    """ Loads the comboboxes for the selected tour based on its transportation type.
        This method fetches the transportation type for the selected tour and populates the driver, vehicle, and guide comboboxes accordingly.
        If the transportation type is "Bus", it populates the driver and vehicle comboboxes with available drivers and buses.
        If the transportation type is "Airplane" or "Boat", it adds a single item to the vehicle combobox.
        :param self: The instance of the class.
        :param tour_id: The identifier of the selected tour.
    """
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


    """ Calculates all costs associated with the selected tour.
        This method retrieves the tour details, calculates costs for the driver, guide, and vehicle,
        and updates the UI labels with the calculated values. It also calculates the total income, profit amount, and hotel share.
        If `return_values_only` is set to True, it returns a dictionary with the calculated values instead of updating the UI.
        :param self: The instance of the class.
        :param return_values_only: If True, returns a dictionary with calculated values instead of updating UI labels.
    """
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
            # Υπολογισμός αριθμού συμμετεχόντων
            self.cursor.execute("SELECT SUM(people_numb) FROM Reservations WHERE tour_id = ? AND status = 'Active'", (tour_id,))
            total_people = self.cursor.fetchone()[0] or 0

            # Υπολογισμός του μεριδίου των ξενοδοχείων (70% από το υπόλοιπο μετά την αφαίρεση 50€/άτομο)
            hotel_share = 0.7 * max(total_income - (50 * total_people), 0)

            if total_income > 0:
                profit_amount = total_income - total_service_cost - hotel_share
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
            round(profit_percent, 2),
            round(hotel_share, 2)
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
            self.hotelshare_label.setText(f"Hotel Share: €{hotel_share:.2f}")
            self.totalCostLabel.setText(f"Total Cost: €{total_service_cost:.2f}")
            self.profitLabel.setText(f"Profit: €{profit_amount:.2f} ({profit_percent:.1f}%)")

            return True

        except Exception as e:
            print("Error calculating all costs:", e)
            return False
        

    """ Accepts the selected tour, updates its status, and calculates financials.
        This method retrieves the selected tour ID, calculates financials, updates the tour status to 'Accepted',
        and updates the status of the associated driver, vehicle, and guide. It also inserts financial data into the TourFinancials table.
        If the tour is successfully accepted, it updates the UI and shows a success message.
        :param self: The instance of the class.
    """
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
            self.populate_teamleader_table()
            self.populate_driver_table()
            self.populate_buses_table()
    

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not accept tour.\n{e}")
            self.connection.rollback()


    """ Declines the selected tour and cancels all associated reservations.
        This method retrieves the selected tour ID, updates its status to 'Declined',
        cancels all reservations associated with the tour, and updates the UI accordingly.
        If the tour is successfully declined, it shows a success message and updates the ongoing tours list.
        :param self: The instance of the class.
    """        
    def decline_tour(self):
        try:
                if not hasattr(self, "selected_tour_id"):
                    return

                tour_id = self.selected_tour_id

                # Αλλαγή το status του Tour σε Declined
                self.cursor.execute("UPDATE Tours SET status = 'Declined' WHERE id = ?", (tour_id,))
                self.loadOngoingTours()
                # Αλλαγή των κρατήσεων σε Cancelled
                self.cursor.execute("UPDATE Reservations SET status = 'Cancelled' WHERE tour_id = ?", (tour_id,))
                self.connection.commit()
                QMessageBox.information(self, "Declined", f"All reservations for tour {tour_id} were cancelled and the tour was declined.")
                self.load_tour_summary(tour_id)
                self.calculate_all_costs()

        except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not decline tour.\n{e}")
                self.connection.rollback()


    """ Loads the ongoing tours into the ongoing tour list widget.
        This method clears the existing items in the list widget and fetches ongoing tours from the database,
        adding each tour as an item in the list widget with its ID and destination.
        :param self: The instance of the class.
    """                     
    def loadOngoingTours(self):
        self.ongoingTourListWidget.clear()
        self.cursor.execute("SELECT id, destination FROM Tours WHERE status = 'Accepted'")
        tours = self.cursor.fetchall()

        for tour_id, destination in tours:
            self.ongoingTourListWidget.addItem(f"{tour_id} - {destination}")


    """ Loads the details of the selected ongoing tour into the ongoing tour details table.
        This method clears the existing rows in the table and fetches financial details for the selected tour from the TourFinancials table.
        It populates the table with the fetched data, including destination, start and end dates, total income, participants, transportation type, transportation cost, driver, and guide.
        :param self: The instance of the class.
        :param tour_id: The identifier of the selected ongoing tour.
    """
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


    """ Triggered when an ongoing tour is selected from the list.
        This method retrieves the selected tour ID from the list item, loads the ongoing tour details,
        and updates the selected tour ID for further operations.
        :param self: The instance of the class.
        :param item: The selected item from the ongoing tour list widget.
    """
    def on_ongoing_tour_selected(self, item):
        tour_text = item.text()
        tour_id = tour_text.split(" ")[0].strip()  # π.χ. "t12"
        self.selected_tour_id = tour_id
        self.loadOngoingTourDetails(tour_id)


    """ Completes the selected ongoing tour by updating its status and resetting associated resources.
        This method retrieves the selected tour ID, updates the status of the tour to 'Completed',
        resets the status of the associated transportation, driver, and guide, and updates all active reservations to 'Completed'.
        If the tour is successfully completed, it shows a success message and updates the ongoing tours list and related tables.
        :param self: The instance of the class.
    """
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

            # Ενημέρωση όλων των κρατήσεων σε Completed
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
            self.populate_teamleader_table()
            self.populate_driver_table()
            self.populate_buses_table()
            self.ongoingTourDetailsTable.setRowCount(0)


        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to complete tour.\n{e}")
            self.connection.rollback()

#--Edit Function----------
    """ Opens a dialog to edit the selected row in the given table widget.
        This method retrieves the currently selected row in the table widget, creates a dialog with input fields for each column,
        and allows the user to edit the values. If the dialog is accepted, it updates the table and executes the provided SQL query with the new values.
        :param self: The instance of the class.
        :param table_widget: The QTableWidget containing the data to be edited.
        :param query: The SQL query to execute for updating the database.
        :param q_num: The number of columns in the table (default is 1).
        :param readonly_fields: A list of fields that should be read-only in the dialog (default is None).
    """
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


        
#--Stats Functions----------
    """ Creates a label with statistics based on the provided SQL query.
        This method executes the given SQL query, fetches the result, and formats it for display in the provided label.
        If the result is None or empty, it sets the label text to "N/A".
        :param self: The instance of the class.
        :param query: The SQL query to execute for fetching statistics.
        :param label: The QLabel where the statistics will be displayed.
    """
    def create_label_stats(self, query, label):
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        fdata = ""
        if data and data[0] is not None:
            for i in range(len(data)):
                if isinstance(data[i], float):
                    fdata += f"{data[i]:.2f} "
                else:
                    fdata += str(data[i]) + " "
            
            label.setText(str(fdata))
        else:
            label.setText("N/A")


    """ Loads a list of statistics into the provided QListWidget based on the given SQL query.
        This method clears the existing items in the list widget, executes the SQL query to fetch statistics,
        and adds each result as an item in the list widget formatted as "data1 - data2".
        param self: The instance of the class.
        param list: The QListWidget where the statistics will be displayed.
        param query: The SQL query to execute for fetching statistics.
    """
    def load_stats_lists(self, list, query):
        list.clear()
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        for data1, data2 in data:
            list.addItem(f"{data1} - {data2}")


    """ Selects a list item and updates the pie chart and table based on the selected item.
        This method retrieves the text of the selected item, extracts the ID from it,
        and uses it to create a pie chart and populate a table with statistics related to the selected item.
        :param self: The instance of the class.
        :param item: The selected QListWidgetItem from the statistics list.
        :param pie: An instance of a PieChart class to create the pie chart.
        :param p_layout: The layout for the pie chart.
        :param l_layout: The layout for the table.
        :param p_query: The SQL query for the pie chart.
        :param l_query: The SQL query for the table.
    """
    def select_list_stats(self, item, pie, p_layout, l_layout, p_query, l_query):
        text = item.text()
        text_id = text.split(" ")[0].strip()
        self.selected_text_id = text_id
        pie.create_piechart(p_query, p_layout, text_id)
        self.populate_table.populate_table(l_layout, l_query, 3, 1, text_id)


    """ Filters the statistics list based on the search text entered in the provided line edit.
        This method retrieves the text from the line edit, clears the list widget,
        and executes the SQL query to fetch statistics that match the search text.
        If no search text is provided, it reloads the full statistics list.
        If no results are found, it adds a message to the list widget indicating no results.
        :param self: The instance of the class.
        :param p_query: The SQL query to fetch the full statistics list.
        :param s_query: The SQL query to search for statistics based on the search text.
        :param e_layout: The QLineEdit where the search text is entered.
        :param w_layout: The QListWidget where the filtered statistics will be displayed.
    """
    def filterStatLists(self,p_query, s_query, e_layout, w_layout):
            search_text = e_layout.text().strip().lower()
            w_layout.clear()

            if not search_text:
                self.load_stats_lists(w_layout, p_query)
                return

            self.cursor.execute(s_query, (f"{search_text}%",f"{search_text}%",f"{search_text}%"))
            data = self.cursor.fetchall()

            if not data:
                w_layout.addItem("No results for this value")
                return

            for item in data:
                item = QListWidgetItem(f"{item[0]} - {item[1]}")
                w_layout.addItem(item)



#--LogOut----------
    """ Closes the current window and opens the login window.
        This method hides the current window and creates an instance of the LoginWindow class,
        which is then shown to the user.
        :param self: The instance of the class.
    """
    def to_login_window(self):
        from login import LoginWindow
        login_window_instance = LoginWindow()
        login_window_instance.show()
        self.hide()
        self.login_window_instance = login_window_instance