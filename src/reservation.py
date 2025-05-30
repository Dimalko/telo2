import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QListView,QListWidget,QListWidgetItem,QComboBox,QFontComboBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont


from classes.populate_table import PopulateTable

"""    Window for managing reservations, including adding clients, tours, and group payments.
    Provides a user interface for filtering clients and tours, adding reservations,
    and managing group payments.
"""
class ReservationWindow(QMainWindow):
    finished = pyqtSignal()
    """
        Initializes the reservation window.
        Loads the UI, connects to the database, and sets up event handlers for various UI elements.
        Connects buttons for adding clients, filtering clients and tours, updating hotels for selected tours,
        adding reservations, and managing group payments.
        """
    def __init__(self): #REMOVE BEFORE FINAL VERSION
        super().__init__()

        loadUi('ui//reservation.ui', self)

    #add style to ui
      #  self.uiStyle()
        self.ClientlineEdit.textChanged.connect(self.filterClients)
        self.TourslineEdit.textChanged.connect(self.filterTours)
        self.Tour_listWidget.itemClicked.connect(self.updateHotelsForTour)
        self.add_reservation_pushButton.clicked.connect(self.addReservation)
        self.groupComboBox.currentIndexChanged.connect(
            lambda _: self.loadGroupPayments(self.groupComboBox.currentData()))

        self.addPaymentButton.clicked.connect(self.addGroupPayment)
        self.editPaymentButton.clicked.connect(self.editGroupPayment)
        self.deletePaymentButton.clicked.connect(self.deleteGroupPayment)

        #self.Hotels_comboBox.addItem(display_text, userData=hotel_id)





    #connect db
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()
        self.loadClients()
        self.loadFreeTours()
        self.loadGroups()
        #self.loadGroupPayments()
        
    #connect buttons
        self.add_Client_button.clicked.connect(self.addClient)    


    """ Clears all input fields in the client registration form.
        Resets the form to its initial state after successful client addition."""
    def input_clear(self):
        self.PhoneNumberInput.setText("")
        self.FirstNameInput.setText("")
        self.LastNameInput.setText("")
        self.EmailInput.setText("")

    """ Creates a new client record in the database.
        Validates that required fields (phone number, first name, last name, email) are provided,
        retrieves form data including phone number, first name, last name, and email.
        Inserts the client data into the database. Shows warning messages
        for invalid input or database constraint violations.
        """
    def addClient(self):
        try:
            phone = self.PhoneNumberInput.text()
            firstName = self.FirstNameInput.text()
            lastName = self.LastNameInput.text()
            email = self.EmailInput.text()
            

            self.cursor.execute("INSERT INTO Client (phone_number, f_name, l_name,email) VALUES (?, ?, ?, ?)",
                                (phone, firstName, lastName,email))
            self.connection.commit()
            self.finished.emit()
            self.input_clear()
            self.loadClients()
            QMessageBox.information(self, "Success", "Client added successfully")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Could not add Client")
            self.input_clear()
            self.connection.rollback()    
    
    
    """ Loads all clients from the database and populates the client list widget.
        Clears the existing items in the client list widget before loading new data.
        Retrieves client information (phone number, first name, last name, email) from the database
        and adds each client as an item in the client list widget.
        If an error occurs during the loading process, it prints the error message."""
    def loadClients(self):
        self.Client_listWidget.clear()
        try:
            self.cursor.execute("SELECT phone_number, f_name, l_name, email FROM Client")
            self.all_clients = self.cursor.fetchall()

            for phone, f_name, l_name, email in self.all_clients:
                item_text = f"{f_name} {l_name} | 📞 {phone} | ✉️ {email}"
                self.Client_listWidget.addItem(item_text)
        except Exception as e:
            print("Error loading clients:", e)
        
    """ Loads all free tours from the database and populates the tour list widget.
        Clears the existing items in the tour list widget before loading new data.
        Retrieves tour information (id, destination, start date, end date, description) from the database
        and adds each tour as an item in the tour list widget."""
    def loadFreeTours(self):
        self.Tour_listWidget.clear()
        try:
            self.cursor.execute("""
                SELECT id, destination, start_date, end_date, description
                FROM Tours
                WHERE status = 'Free'
            """)
            self.all_tours = self.cursor.fetchall()

            for id, destination, start_date, end_date, description in self.all_tours:
                item_text = f"#{id} | {destination} | {start_date} ➝ {end_date} | {description}"
                self.Tour_listWidget.addItem(item_text)
        except Exception as e:
            print("Error loading free tours:", e)

    """ Filters the client list based on the input in the client line edit.
        Clears the existing items in the client list widget before loading new data.
        If the input is empty, it retrieves all clients from the database.
        If there is input, it retrieves clients whose phone number starts with the input text.
        Each client is added as an item in the client list widget with the format:
        "First Name Last Name | 📞 Phone Number | ✉️ Email".
        If no clients match the search criteria, a "No result for this value" item is added in gray italic font.
    """
    def filterClients(self):
        search_text = self.ClientlineEdit.text().strip()
        self.Client_listWidget.clear()

        try:
            if not search_text:
                self.cursor.execute("SELECT phone_number, f_name, l_name, email FROM Client")
            else:
                self.cursor.execute("""
                    SELECT phone_number, f_name, l_name, email
                    FROM Client
                    WHERE phone_number LIKE ?
                """, (f"{search_text}%",))  # ξεκινάει με...

            clients = self.cursor.fetchall()

            if clients:
                for phone, f_name, l_name, email in clients:
                    item_text = f"{f_name} {l_name} | 📞 {phone} | ✉️ {email}"
                    self.Client_listWidget.addItem(item_text)
            else:
                no_result_item = QListWidgetItem("No result for this value")
                no_result_item.setForeground(Qt.gray)
                font = QFont()
                font.setItalic(True)
                no_result_item.setFont(font)
                self.Client_listWidget.addItem(no_result_item)
        except Exception as e:
            print("Error filtering clients:", e)



    """ Filters the tour list based on the input in the tour line edit.
        Clears the existing items in the tour list widget before loading new data.
        If the input is empty, it retrieves all free tours from the database.
        If there is input, it retrieves tours whose id starts with the input text.
        Each tour is added as an item in the tour list widget with the format:
        "#ID | Destination | Start Date ➝ End Date | Description".
        If no tours match the search criteria, a "No result for this value" item is added in gray italic font.
        """
    def filterTours(self):
        search_text = self.TourslineEdit.text().strip()
        self.Tour_listWidget.clear()

        try:
            if not search_text:
                self.cursor.execute("""
                    SELECT id, destination, start_date, end_date, description
                    FROM Tours
                    WHERE status = 'Free'
                """)
            else:
                self.cursor.execute("""
                    SELECT id, destination, start_date, end_date, description
                    FROM Tours
                    WHERE status = 'Free' AND id LIKE ?
                """, (f"{search_text}%",))

            tours = self.cursor.fetchall()

            if tours:
                for id, destination, start_date, end_date, description in tours:
                    item_text = f"#{id} | {destination} | {start_date} ➝ {end_date} | {description}"
                    self.Tour_listWidget.addItem(item_text)
            else:
                no_result_item = QListWidgetItem("No result for this value")
                no_result_item.setForeground(Qt.gray)
                font = QFont()
                font.setItalic(True)
                no_result_item.setFont(font)
                self.Tour_listWidget.addItem(no_result_item)
        except Exception as e:
            print("Error filtering tours:", e)
  
    """ Updates the hotels combo box based on the selected tour in the tour list widget.
        Retrieves the hotels associated with the selected tour from the database.
        Clears the existing items in the hotels combo box before loading new data.
        Each hotel is added as an item in the hotels combo box with the format:
        "Hotel Name - Price€/person".
        If an error occurs during the loading process, it prints the error message.
    """
    def updateHotelsForTour(self, item):
        try:
            # Βρες το ID του επιλεγμένου tour από το κείμενο (π.χ. "#15 | Athens")
            tour_id = item.text().split(" ")[0].replace("#", "").strip()

            # Εκτέλεσε query για να βρεις τα ξενοδοχεία που συνδέονται με αυτό το tour
            self.cursor.execute("""
                SELECT Hotels.id, Hotels.name, Hotels.price_pp
                FROM Hotels
                JOIN ToursHotels ON Hotels.id = ToursHotels.hotel_id
                WHERE ToursHotels.tour_id = ?
            """, (tour_id,))
            hotels = self.cursor.fetchall()

            # Καθάρισε το comboBox
            self.Hotels_comboBox.clear()

            # Πρόσθεσε τα ξενοδοχεία στο comboBox με format: "Όνομα - Τιμή€/άτομο"
            for hotel_id, name, price_pp in hotels:
                display_text = f"{name} - {price_pp}€/άτομο"
                self.Hotels_comboBox.addItem(display_text, userData=hotel_id)  # αποθηκεύουμε και το hotel_id

        except Exception as e:
            print("Error loading hotels for tour:", e)
    
    """ Adds a reservation based on the selected tour, client, and other input fields.
        Retrieves the selected tour and client from the list widgets, validates input fields,
        calculates the total cost based on the number of people, hotel, and transportation type.
        Inserts the reservation into the database, including ticket information if applicable.
        If the reservation is for a group (more than one person), it creates a group record and a prepayment.
        Displays success or error messages based on the outcome of the operation.
        """
    def addReservation(self):
        try:
            # Πάρε το επιλεγμένο tour
            selected_tour = self.Tour_listWidget.currentItem()
            if not selected_tour:
                QMessageBox.warning(self, "Missing data", "Please select a tour.")
                return
            tour_id = selected_tour.text().split(" ")[0].replace("#", "").strip()

            # Πάρε τον επιλεγμένο πελάτη
            selected_client = self.Client_listWidget.currentItem()
            if not selected_client:
                QMessageBox.warning(self, "Missing data", "Please select a client.")
                return
            client_phone = selected_client.text().split("📞")[1].split("|")[0].strip()

            # Πάρε τα υπόλοιπα δεδομένα από το UI
            people = self.peopleSpinBox.value()
            if people <= 0:
                QMessageBox.warning(self, "Invalid data", "Number of people must be at least 1.")
                return

            hotel_id = self.Hotels_comboBox.currentData()
            payment_type = self.paymentComboBox.currentText()

            # Βρες την τιμή ανά άτομο για το συγκεκριμένο ξενοδοχείο
            self.cursor.execute("SELECT price_pp FROM Hotels WHERE id = ?", (hotel_id,))
            result = self.cursor.fetchone()
            if not result:
                QMessageBox.warning(self, "Error", "Could not find selected hotel.")
                return
            price_per_person = result[0]

            # Βρες τις ημερομηνίες της εκδρομής
            self.cursor.execute("SELECT start_date, end_date, transportation FROM Tours WHERE id = ?", (tour_id,))
            date_result = self.cursor.fetchone()

            if not date_result:
                QMessageBox.warning(self, "Error", "Could not find tour details.")
                return

            start_date_str, end_date_str, transportation = date_result
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

            # Υπολογισμός ημερών (συμπεριλαμβανομένης και της τελευταίας μέρας)
            number_of_days = (end_date - start_date).days + 1
            if number_of_days <= 0:
                QMessageBox.warning(self, "Error", "Invalid tour dates.")
                return

            # Κόστος μεταφοράς (αν είναι αεροπλάνο ή πλοίο)
            transportation_cost = 0
            if transportation == 'Airplain':
                transportation_cost = 120 * people
            elif transportation == 'Boat':
                transportation_cost = 60 * people

            # Τελικό κόστος: τιμή * άτομα * ημέρες + extra 50€/άτομο
            f_total_cost = (price_per_person * people * number_of_days) + (50 * people) + transportation_cost
            total_cost = (price_per_person * people * number_of_days) + (50 * people) + transportation_cost

            # Δημιουργία κράτησης
            self.cursor.execute("""
                INSERT INTO Reservations (tour_id, client_n, people_numb, hotel_id, cost, payment_type, status)
                VALUES (?, ?, ?, ?, ?, ?, 'Active')
            """, (tour_id, client_phone, people, hotel_id, total_cost, payment_type))
            reservation_id = self.cursor.lastrowid

            # Εισαγωγή Ticket αν υπάρχει μεταφορά με Airplain ή Boat
            if transportation == "Airplain":
                ticket_price = 120
                self.cursor.execute("""
                    INSERT INTO Tickets (reservation_id, type, price_per_person, total_price)
                    VALUES (?, ?, ?, ?)
                """, (reservation_id, "Airplain", ticket_price, ticket_price * people))
            elif transportation == "Boat":
                ticket_price = 60
                self.cursor.execute("""
                    INSERT INTO Tickets (reservation_id, type, price_per_person, total_price)
                    VALUES (?, ?, ?, ?)
                """, (reservation_id, "Boat", ticket_price, ticket_price * people))

            # Αν είναι group (πάνω από 1 άτομο), δημιούργησε εγγραφή group και προκαταβολή
            if people > 1:
                self.cursor.execute("""
                    INSERT INTO ReservationGroup (reservation_id, total_people, total_cost)
                    VALUES (?, ?, ?)
                """, (reservation_id, people, total_cost))
                group_id = self.cursor.lastrowid
                deposit = round(total_cost * 0.30, 2)

                self.cursor.execute("""
                    INSERT INTO GroupPayments (group_id, payment_date, type, amount)
                    VALUES (?, DATE('now'), ?, ?)
                """, (group_id, "Prepayment", deposit))

                self.cursor.execute("""
                    UPDATE ReservationGroup
                    SET amount_paid = ?
                    WHERE id = ?
                """, (deposit, group_id))

            self.connection.commit()
            QMessageBox.information(
                self,
                "Success",
                f"Reservation completed successfully!\n({number_of_days} days tour)\nTransportation: {transportation} | Ticket Cost: €{transportation_cost:.2f}"
            )

            # Reset πεδίων
            self.peopleSpinBox.setValue(1)
            self.paymentComboBox.setCurrentIndex(0)
            self.Hotels_comboBox.setCurrentIndex(0)

            self.loadGroups()

        except Exception as e:
            print("Reservation error:", e)
            QMessageBox.critical(self, "Error", "An error occurred while adding the reservation.")
            self.connection.rollback()






    """ Loads all active groups from the database and populates the group combo box.
        Clears the existing items in the group combo box before loading new data.
        Retrieves group information (id, reservation id, total people, total cost, destination, tour id)
        from the database and adds each group as an item in the group combo box with the format:
        "Group #ID | Reservation: ID | People: N | Cost: €C | Tour: #T - Destination".
        If an error occurs during the loading process, it prints the error message.
    """
    def loadGroups(self):
        try:
            self.groupComboBox.clear()
            self.cursor.execute("""
                SELECT g.id, g.reservation_id, g.total_people, g.total_cost,
                    t.destination, t.id
                FROM ReservationGroup g
                JOIN Reservations r ON g.reservation_id = r.id
                JOIN Tours t ON r.tour_id = t.id
                WHERE r.status = 'Active'
            """)
            groups = self.cursor.fetchall()

            for group_id, reservation_id, people, total_cost, destination, tour_id in groups:
                display_text = (
                    f"Group #{group_id} | Reservation: {reservation_id} | People: {people} "
                    f"| Cost: €{total_cost:.2f} | Tour: #{tour_id} - {destination}"
                )
                self.groupComboBox.addItem(display_text, userData=group_id)
        except Exception as e:
            print("Error loading groups:", e)




    """ Loads all payments for the selected group and populates the group payments table.
        Clears the existing rows in the group payments table before loading new data.
        Retrieves payment information (id, group id, amount, payment date, type) from the database
        and adds each payment as a row in the group payments table with the format:
        "ID | Group ID | Amount | Payment Date | Type".
        If an error occurs during the loading process, it prints the error message.
    """
    def loadGroupPayments(self, group_id):
        try:
            self.groupPaymentsTable.setRowCount(0)

            self.cursor.execute("""
                SELECT id, group_id, amount, payment_date, type
                FROM GroupPayments
                WHERE group_id = ?
                ORDER BY payment_date
            """, (group_id,))
            payments = self.cursor.fetchall()

            for row_idx, (pid, gid, amount, date, ptype) in enumerate(payments):
                self.groupPaymentsTable.insertRow(row_idx)
                self.groupPaymentsTable.setItem(row_idx, 0, QTableWidgetItem(str(pid)))              # id
                self.groupPaymentsTable.setItem(row_idx, 1, QTableWidgetItem(str(gid)))              # group_id
                self.groupPaymentsTable.setItem(row_idx, 2, QTableWidgetItem(f"€ {amount:.2f}"))     # amount
                self.groupPaymentsTable.setItem(row_idx, 3, QTableWidgetItem(date))                  # payment_date
                self.groupPaymentsTable.setItem(row_idx, 4, QTableWidgetItem(ptype))                 # type

            self.updateGroupStatus(group_id)

        except Exception as e:
            print("Error loading group payments:", e)


    """ Adds a new group payment based on the selected group and input fields.
        Validates that a group is selected, retrieves the payment date, type, and amount from the UI.
        Checks if the amount is valid (greater than 0) and does not exceed the remaining balance of the group.
        Inserts the payment into the database and updates the total amount paid for the group.
        Displays success or error messages based on the outcome of the operation.
    """
    def addGroupPayment(self):
        try:
            group_id = self.groupComboBox.currentData()
            if group_id is None:
                QMessageBox.warning(self, "Error", "You havent selected a group.")
                return

            date = self.paymentDateEdit.date().toString("yyyy-MM-dd")
            ptype = self.paymentTypeComboBox.currentText()
            amount = self.paymentAmountSpinBox.value()

            if amount <= 0:
                QMessageBox.warning(self, "Invalid Amount", "The amount has to be larger than 0.")
                return

        # Έλεγχος να μην ξεπεραστεί το συνολικό ποσό
            self.cursor.execute("SELECT total_cost, COALESCE(amount_paid, 0) FROM ReservationGroup WHERE id = ?", (group_id,))
            result = self.cursor.fetchone()

            if result:
                total_cost, amount_paid = result
                if amount_paid + amount > total_cost:
                    QMessageBox.warning(self, "Error", "This payment exceeds the remaining balance.")
                    return
            # Καταχώρηση πληρωμής
            self.cursor.execute("""
                INSERT INTO GroupPayments (group_id, payment_date, type, amount)
                VALUES (?, ?, ?, ?)
            """, (group_id, date, ptype, amount))

            # Ενημέρωση συνολικού amount_paid στο group
            self.cursor.execute("""
                UPDATE ReservationGroup
                SET amount_paid = COALESCE(amount_paid, 0) + ?
                WHERE id = ?
            """, (amount, group_id))

            self.connection.commit()
            self.loadGroupPayments(group_id)
            QMessageBox.information(self, "Success", "Η Payment inserted succesfully.")
        except Exception as e:
            print("Error adding payment:", e)
            QMessageBox.critical(self, "Failed", "Failure to insert the payment.")
    """ Updates the status label for the selected group based on the total cost and amount paid.
        Retrieves the total cost, amount paid, and reservation ID for the group from the database.
        Determines the payment status (Unpaid, Partially Paid, or Paid) based on the amount paid.
        Retrieves the tour ID from the reservation and the start date of the tour.
        Displays the payment status, amount paid, total cost, and start date in the payment status label.
    """
    def updateGroupStatus(self, group_id):
        try:
            # 1. Πάρε τα βασικά από το group
            self.cursor.execute("""
                SELECT total_cost, amount_paid, reservation_id
                FROM ReservationGroup
                WHERE id = ?
            """, (group_id,))
            group = self.cursor.fetchone()

            if not group:
                self.paymentStatusLabel.setText("Το group δεν βρέθηκε.")
                return

            total_cost, amount_paid, reservation_id = group

            # 2. Υπολόγισε κατάσταση
            if amount_paid == 0:
                status = "Unpaid"
            elif amount_paid < total_cost:
                status = "Partially Paid"
            else:
                status = "Paid"

            # 3. Βρες το tour_id της κράτησης
            self.cursor.execute("SELECT tour_id FROM Reservations WHERE id = ?", (reservation_id,))
            res = self.cursor.fetchone()
            tour_id = res[0] if res else None

            # 4. Βρες την start_date του tour
            if tour_id:
                self.cursor.execute("SELECT start_date FROM Tours WHERE id = ?", (tour_id,))
                tour = self.cursor.fetchone()
                start_date = tour[0] if tour else "N/A"
            else:
                start_date = "N/A"

            # 5. Εμφάνιση label
            self.paymentStatusLabel.setText(
                f"Paid: {amount_paid:.2f} / {total_cost:.2f} € | Status: {status} | Before: {start_date}"
            )

        except Exception as e:
            print("Error updating group status:", e)
            self.paymentStatusLabel.setText("Σφάλμα κατά την ενημέρωση της κατάστασης.")
    """ Deletes a selected group payment from the database.
        Retrieves the current row from the group payments table, checks if a payment is selected,
        retrieves the group ID and payment ID from the selected row.
        Validates that the amount is greater than 0, confirms the deletion with the user,
        deletes the payment from the GroupPayments table, and updates the amount paid for the group.
        Displays success or error messages based on the outcome of the operation.
    """
    def deleteGroupPayment(self):
        current_row = self.groupPaymentsTable.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Warning", "No payment selected.")
            return

        group_id = self.groupComboBox.currentData()
        payment_id = int(self.groupPaymentsTable.item(current_row, 0).text())

        amount_text = self.groupPaymentsTable.item(current_row, 2).text().replace("€", "").strip()
        amount = float(amount_text)

        confirm = QMessageBox.question(self, "Confirm Deletion", "Are you sure you want to delete this payment?",
                                        QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.cursor.execute("DELETE FROM GroupPayments WHERE id = ?", (payment_id,))
            self.cursor.execute("""
                UPDATE ReservationGroup
                SET amount_paid = amount_paid - ?
                WHERE id = ?
            """, (amount, group_id))

            self.connection.commit()
            self.loadGroupPayments(group_id)
            QMessageBox.information(self, "Success", "Payment deleted successfully.")

    """ Edits a selected group payment directly from the group payments table.
        Retrieves the current row from the group payments table, checks if a payment is selected,
        retrieves the group ID and payment ID from the selected row.
        Validates that the new amount is greater than 0, retrieves the old amount from the database,
        updates the payment in the GroupPayments table, and updates the amount paid for the group.
        Displays success or error messages based on the outcome of the operation.
    """
    def editGroupPayment(self):
        current_row = self.groupPaymentsTable.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Warning", "No payment selected to edit.")
            return

        group_id = self.groupComboBox.currentData()

        # Παίρνουμε id και το παλιό ποσό
        payment_id = int(self.groupPaymentsTable.item(current_row, 0).text())

        try:
            # Νέες τιμές απευθείας από το table
            new_amount_text = self.groupPaymentsTable.item(current_row, 2).text().replace("€", "").strip()
            new_amount = float(new_amount_text)

            new_date = self.groupPaymentsTable.item(current_row, 3).text()
            new_type = self.groupPaymentsTable.item(current_row, 4).text()

            # Παλιό ποσό για σύγκριση
            self.cursor.execute("SELECT amount FROM GroupPayments WHERE id = ?", (payment_id,))
            old_amount = self.cursor.fetchone()[0]

            # Ενημέρωση βάσης
            self.cursor.execute("""
                UPDATE GroupPayments
                SET amount = ?, payment_date = ?, type = ?
                WHERE id = ?
            """, (new_amount, new_date, new_type, payment_id))

            difference = new_amount - old_amount
            self.cursor.execute("""
                UPDATE ReservationGroup
                SET amount_paid = amount_paid + ?
                WHERE id = ?
            """, (difference, group_id))

            self.connection.commit()
            self.loadGroupPayments(group_id)
            QMessageBox.information(self, "Success", "Payment updated from table successfully.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not update payment.\n{e}")