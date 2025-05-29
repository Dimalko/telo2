import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
"""
    Class to create and manage a bar chart using data from a SQLite database.
    It connects to the database, executes a query, and populates the bar chart with the results.
    The class can handle different types of queries and formats the data accordingly.
    The bar chart is displayed in a QChartView widget.
    The bar chart can be created dynamically based on the provided query and layout.
"""
class BarChart():
    """ Initializes the BarChart class.
        Sets up the chart view and series for the bar chart.
    """
    def __init__(self):
        self.chartview = None
        self.series = None
        
        
    """ Creates a bar chart based on the provided query and layout.
        The method connects to the SQLite database, executes the query, and populates the bar chart with the results.
        If the query returns no data, it will not display the chart.
        :param query: The SQL query to execute.
        :param layout: The layout where the chart view will be added.
    """
    def create_barchart(self, query, layout):
        connection = sqlite3.connect("data//database.db")
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        if not data:
            print("No data to display.")
            return

        if self.series is None:
                self.series = QBarSeries()
                self.chartview = QChartView()
                layout.addWidget(self.chartview)

        self.series.clear()

        # Bar Set
        bar_set = QBarSet("")
        categories = []

        for item in data:
            categories.append(item[0])     
            bar_set.append(item[1])        

        # Bar Series
        series = QBarSeries()
        series.append(bar_set)

        # Chart
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Axes
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axisX, series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        # Chart View
        self.chartview.setChart(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        layout.addWidget(self.chartview)