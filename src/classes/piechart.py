import sys
import sqlite3
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice

class PieChart():
    def __init__(self):
        self.chartview = None
        self.series = None
        
        
    def create_piechart(self, query, layout):
        try:
            connection = sqlite3.connect("data//database.db")
            cursor = connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            
            if self.series is None:
                self.series = QPieSeries()
                self.chartview = QChartView()
                layout.addWidget(self.chartview)
                
            
            self.series.clear()
            
            if all(float(item[1]) == 0 for item in data):
                print("All values are 0")
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
            chart.legend().setAlignment(Qt.AlignRight)

            self.chartview.setChart(chart)
            self.chartview.setRenderHint(QPainter.Antialiasing)
            layout.addWidget(self.chartview)
        except Exception as e:
            print("an error ocurred", str(e))