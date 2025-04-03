import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem


class PopulateTable:
    def __init__(self, db_path="data//database.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()


    def populate_table(self, table_widget, query, col):
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        if not data:
            return

        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(col)  

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                table_widget.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))





    def close_connection(self):
        """Close the database connection"""
        self.connection.close()