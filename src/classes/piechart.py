import sys
import sqlite3
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice


"""
    Class to create and manage a pie chart using data from a SQLite database.
    It connects to the database, executes a query, and populates the pie chart with the results.
    The class can handle different types of queries and formats the data accordingly.
    The pie chart is displayed in a QChartView widget.  
"""
class PieChart():
    
    """ Initializes the PieChart class.
        Sets up the chart view and series for the pie chart.
    """
    def __init__(self):
        self.chartview = None
        self.series = None
        

    """ Creates a pie chart based on the provided query and layout.
        The method connects to the SQLite database, executes the query, and populates the pie chart with the results.
        If the query returns no data or all values are zero, it will not display the chart.
        :param query: The SQL query to execute.
        :param layout: The layout where the chart view will be added.
        :param key: An optional parameter to filter the query results (default is None).
    """
    def create_piechart(self, query, layout, key = None):
        try:
            connection = sqlite3.connect("data//database.db")
            cursor = connection.cursor()
            if key==None:
                cursor.execute(query)
            else:
                cursor.execute(query,(key,))
            
            data = cursor.fetchall()
            
            if self.series is None:
                self.series = QPieSeries()
                self.chartview = QChartView()
                self.chartview.setRenderHint(QPainter.Antialiasing)
                layout.addWidget(self.chartview)
                
            
            self.series.clear()
            
            if not data or all(float(item[1]) == 0 for item in data):
                chart = QChart()
                chart.setTitle("No Data Available")
                self.chartview.setChart(chart)
                return

            num_colors = len(data)
            if num_colors > 1:
                colors = [QColor.fromHsv(220, int(100 + (155 * i / (num_colors - 1))), 200) for i in range(num_colors)]
            else:
                colors = [QColor.fromHsv(220, 200, 200)]

            for i, item in enumerate(data):
                label = f"{item[0]} - {item[1]}"
                value = float(item[1])
                slice = self.series.append(label, value)
                self.series.slices()[-1].setColor(colors[i % len(colors)])

            self.series.setLabelsVisible(True)
            self.series.setLabelsPosition(QPieSlice.LabelOutside)

            chart = QChart()
            chart.addSeries(self.series)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            
            if key==None:
                chart.legend().setAlignment(Qt.AlignRight)
            else:
                chart.legend().setAlignment(Qt.AlignBottom)

            self.chartview.setChart(chart)
            print("finished pie\n")
        except Exception as e:
            print("an error ocurred", str(e))