import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem


class PopulateTable:
    def __init__(self, db_path="data//database.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()


    def populate_table(self, table_widget, query, col, q_num = 1):
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        if not data:
            return

        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(col)  

        if q_num == 2:
            for row_num, row_data in enumerate(data):
                hotel_cell = ""
                
                for col_num, col_data in enumerate(row_data):
                    table_widget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
                
                tour_id = row_data[0]

                self.cursor.execute("""
                    SELECT Hotels.name
                    FROM Hotels
                    JOIN ToursHotels ON Hotels.id = ToursHotels.hotel_id
                    WHERE ToursHotels.tour_id = ?
                """, (tour_id,))

                hotels = self.cursor.fetchall()
                hotel_names = [hotel[0] for hotel in hotels]
                hotel_cell = ", ".join(hotel_names)

                table_widget.setItem(row_num, 10, QTableWidgetItem(hotel_cell))
        else:
            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    table_widget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))