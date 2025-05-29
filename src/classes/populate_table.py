import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem

"""
    Class to populate a table widget with data from a SQLite database.
    It executes a query, fetches the results, and fills the table widget with the data.
    The class can handle different types of queries and formats the data accordingly.
"""
class PopulateTable:
    """ Initializes the PopulateTable class.
        Connects to the SQLite database specified by the db_path parameter.
        :param db_path: Path to the SQLite database file (default is "data//database.db").
    """
    
    def __init__(self, db_path="data//database.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    """
        Populates a table widget with data from the database based on the provided query.
        The method executes the query, fetches the results, and fills the table widget with the data.
        It can handle different query types and formats the data accordingly.
        :param table_widget: The QTableWidget to populate with data.
        :param query: The SQL query to execute.
        :param col: The number of columns in the table.
        :param q_num: An optional parameter to determine the type of query (default is 1).
        :param key: An optional parameter to filter the query results (default is None).
    """
    def populate_table(self, table_widget, query, col, q_num = 1, key=None):
        if key == None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query,(key,))

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