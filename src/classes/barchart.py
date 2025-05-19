import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class BarChart():
    def __init__(self):
        self.chartview = None
        self.series = None
        
        

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
            categories.append(item[0])     # bus_plate
            bar_set.append(item[1])        # total_tours

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