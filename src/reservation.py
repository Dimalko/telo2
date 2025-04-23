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


class ReservationWindow(QMainWindow):
    finished = pyqtSignal()
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
       # self.loadGroupPayments()
        
    #connect buttons
        self.add_Client_button.clicked.connect(self.addClient)    



    def input_clear(self):
        self.PhoneNumberInput.setText("")
        self.FirstNameInput.setText("")
        self.LastNameInput.setText("")
        self.EmailInput.setText("")


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

            total_cost = price_per_person * people

            # Δημιούργησε το Reservation
            self.cursor.execute("""
                INSERT INTO Reservations (tour_id, client_n, people_numb, hotel_id, cost, payment_type)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (tour_id, client_phone, people, hotel_id, total_cost, payment_type))
            reservation_id = self.cursor.lastrowid

            # Αν είναι group (πάνω από 1 άτομο), δημιούργησε και εγγραφή στο ReservationGroup
            if people > 1:
                # Δημιουργία group
                self.cursor.execute("""
                    INSERT INTO ReservationGroup (reservation_id, total_people, total_cost)
                    VALUES (?, ?, ?)
                """, (reservation_id, people, total_cost))

                group_id = self.cursor.lastrowid

                # Υπολογισμός προκαταβολής 30%
                deposit = round(total_cost * 0.30, 2)

                # Καταχώρηση πληρωμής προκαταβολής
                self.cursor.execute("""
                    INSERT INTO GroupPayments (group_id, payment_date, type, amount)
                    VALUES (?, DATE('now'), ?, ?)
                """, (group_id, "Prepayment", deposit))

                # Ενημέρωση amount_paid στο group
                self.cursor.execute("""
                    UPDATE ReservationGroup
                    SET amount_paid = ?
                    WHERE id = ?
                """, (deposit, group_id))

            self.connection.commit()
            QMessageBox.information(self, "Success", "Reservation completed successfully!")

            # Προαιρετικό reset πεδίων
            self.peopleSpinBox.setValue(1)
            self.paymentComboBox.setCurrentIndex(0)
            self.Hotels_comboBox.setCurrentIndex(0)

        except Exception as e:
            print("Reservation error:", e)
            QMessageBox.critical(self, "Error", "An error occurred while adding the reservation.")
            self.connection.rollback()



    def loadGroups(self):
        try:
            self.groupComboBox.clear()
            self.cursor.execute("""
                SELECT id, reservation_id, total_people, total_cost
                FROM ReservationGroup
            """)
            groups = self.cursor.fetchall()
            print("RAW GROUPS:", groups)

            for group_id, reservation_id, people, total_cost in groups:
                display_text = f"Group #{group_id} | Reservation: {reservation_id} | People: {people} | Cost: €{total_cost:.2f}"
                self.groupComboBox.addItem(display_text, userData=group_id)
        except Exception as e:
            print("Error loading groups:", e)



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











#!REMOVE BEFORE FINAL VERSION---------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationWindow()
    window.show()
    sys.exit(app.exec_())