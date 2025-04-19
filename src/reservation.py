import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QListView,QListWidget,QListWidgetItem
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


    #connect db
        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()
        self.loadClients()
        self.loadFreeTours()
        
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

                

        








#!REMOVE BEFORE FINAL VERSION---------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationWindow()
    window.show()
    sys.exit(app.exec_())