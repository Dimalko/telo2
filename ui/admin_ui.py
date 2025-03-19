# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(907, 665)
        MainWindow.setStyleSheet(u"QWidget{\n"
"font: 57 8pt \"Yu Gothic Medium\";\n"
"}\n"
"\n"
"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(8, 123, 225);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.widget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setPixmap(QPixmap(u"../Downloads/travel-agency (2).png"))
        self.logoLabel.setAlignment(Qt.AlignCenter)
        self.logoLabel.setMargin(20)

        self.verticalLayout.addWidget(self.logoLabel)

        self.homeBtn = QPushButton(self.widget)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.verticalLayout.addWidget(self.homeBtn)

        self.requestBtn = QPushButton(self.widget)
        self.requestBtn.setObjectName(u"requestBtn")
        self.requestBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.verticalLayout.addWidget(self.requestBtn)

        self.ongoingBtn = QPushButton(self.widget)
        self.ongoingBtn.setObjectName(u"ongoingBtn")
        self.ongoingBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.verticalLayout.addWidget(self.ongoingBtn)

        self.staffBtn = QPushButton(self.widget)
        self.staffBtn.setObjectName(u"staffBtn")
        self.staffBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.verticalLayout.addWidget(self.staffBtn)

        self.vehiclesBtn = QPushButton(self.widget)
        self.vehiclesBtn.setObjectName(u"vehiclesBtn")
        self.vehiclesBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.verticalLayout.addWidget(self.vehiclesBtn)

        self.statsBtn = QPushButton(self.widget)
        self.statsBtn.setObjectName(u"statsBtn")
        self.statsBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.verticalLayout.addWidget(self.statsBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(243, 249, 254);")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.gridLayout = QGridLayout(self.homePage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_6 = QPushButton(self.homePage)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.homePage)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.label_2 = QLabel(self.homePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.tourTableWidget = QTableWidget(self.homePage)
        if (self.tourTableWidget.columnCount() < 9):
            self.tourTableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tourTableWidget.setObjectName(u"tourTableWidget")
        self.tourTableWidget.setStyleSheet(u"QTableWidget {\n"
"border:none;\n"
"background-color: white; \n"
"alternate-background-color: #f0f0f0; /* Alternating row color */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #0984e3; /* Header background */\n"
"    color: white;              /* Header text color */\n"
"    font: bold 12px Arial;     /* Header font */\n"
"    padding: 5px;\n"
"    border: 1px solid #74b9ff; /* Border color */\n"
"}\n"
"\n"
"#QTableWidget QTableCornerButton::section {\n"
"    background-color: #74b9ff; /* Top-left corner color */\n"
"    border: 1px solid #0984e3;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #dfe6e9;  /* Background color of the scrollbar track */\n"
"    height: 12px;  /* Thickness of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0984e3; /* Color of the scrollbar handle (slider) */\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"    border-radius: 6px; /* Rounded edges *"
                        "/\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #74b9ff; /* Lighter color when hovered */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none; /* Removes the small arrow buttons */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none; /* Keeps empty space color same */\n"
"}")
        self.tourTableWidget.setCornerButtonEnabled(True)

        self.gridLayout.addWidget(self.tourTableWidget, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.homePage)
        self.requestPage = QWidget()
        self.requestPage.setObjectName(u"requestPage")
        self.horizontalLayout_3 = QHBoxLayout(self.requestPage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.listWidget = QListWidget(self.requestPage)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_18 = QPushButton(self.requestPage)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_18)

        self.pushButton_17 = QPushButton(self.requestPage)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.tableWidget_4 = QTableWidget(self.requestPage)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.horizontalLayout_3.addWidget(self.tableWidget_4)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)
        self.stackedWidget.addWidget(self.requestPage)
        self.ongoingPage = QWidget()
        self.ongoingPage.setObjectName(u"ongoingPage")
        self.stackedWidget.addWidget(self.ongoingPage)
        self.staffPage = QWidget()
        self.staffPage.setObjectName(u"staffPage")
        self.gridLayout_2 = QGridLayout(self.staffPage)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.staffPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar{\n"
"border:none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"        background: rgb(220, 228, 231);\n"
"        \n"
"       \n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"        background: #087be1;\n"
"        color: white; \n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"        background: #2f8ee4;\n"
"		color: white; \n"
"}")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_10 = QPushButton(self.tab_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_10, 1, 2, 1, 1)

        self.add_Travel_Agent_button = QPushButton(self.tab_2)
        self.add_Travel_Agent_button.setObjectName(u"add_Travel_Agent_button")
        self.add_Travel_Agent_button.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_3.addWidget(self.add_Travel_Agent_button, 1, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.travelagentTableWidget = QTableWidget(self.tab_2)
        if (self.travelagentTableWidget.columnCount() < 8):
            self.travelagentTableWidget.setColumnCount(8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        self.travelagentTableWidget.setObjectName(u"travelagentTableWidget")
        self.travelagentTableWidget.setStyleSheet(u"QTableWidget {\n"
"border:none;\n"
"background-color: white; \n"
"alternate-background-color: #f0f0f0; /* Alternating row color */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #0984e3; /* Header background */\n"
"    color: white;              /* Header text color */\n"
"    font: bold 12px Arial;     /* Header font */\n"
"    padding: 5px;\n"
"    border: 1px solid #74b9ff; /* Border color */\n"
"}\n"
"\n"
"#QTableWidget QTableCornerButton::section {\n"
"    background-color: #74b9ff; /* Top-left corner color */\n"
"    border: 1px solid #0984e3;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #dfe6e9;  /* Background color of the scrollbar track */\n"
"    height: 12px;  /* Thickness of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0984e3; /* Color of the scrollbar handle (slider) */\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"    border-radius: 6px; /* Rounded edges *"
                        "/\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #74b9ff; /* Lighter color when hovered */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none; /* Removes the small arrow buttons */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none; /* Keeps empty space color same */\n"
"}")

        self.gridLayout_3.addWidget(self.travelagentTableWidget, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_2 = QTableWidget(self.widget_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 0, 1, 3)

        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_11, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_12, 1, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_13, 1, 2, 1, 1)

        self.tabWidget.addTab(self.widget_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_14 = QPushButton(self.tab)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton_14, 1, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.tab)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton_15, 1, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.tab)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton_16, 1, 2, 1, 1)

        self.tableWidget_3 = QTableWidget(self.tab)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.gridLayout_5.addWidget(self.tableWidget_3, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.staffPage)
        self.vehiclePage = QWidget()
        self.vehiclePage.setObjectName(u"vehiclePage")
        self.gridLayout_6 = QGridLayout(self.vehiclePage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_19 = QPushButton(self.vehiclePage)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_19, 1, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.vehiclePage)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_21, 1, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.vehiclePage)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_22, 1, 2, 1, 1)

        self.tableWidget_5 = QTableWidget(self.vehiclePage)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.gridLayout_6.addWidget(self.tableWidget_5, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.vehiclePage)
        self.statsPage = QWidget()
        self.statsPage.setObjectName(u"statsPage")
        self.label_3 = QLabel(self.statsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 270, 201, 81))
        self.stackedWidget.addWidget(self.statsPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.requestBtn.setText(QCoreApplication.translate("MainWindow", u"Requests", None))
        self.ongoingBtn.setText(QCoreApplication.translate("MainWindow", u"Ongoing Trips", None))
        self.staffBtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.vehiclesBtn.setText(QCoreApplication.translate("MainWindow", u"Vehicles", None))
        self.statsBtn.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Available Destinations", None))
        ___qtablewidgetitem = self.tourTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tourTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem2 = self.tourTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Starting Date", None));
        ___qtablewidgetitem3 = self.tourTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"End Date", None));
        ___qtablewidgetitem4 = self.tourTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem5 = self.tourTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Distance", None));
        ___qtablewidgetitem6 = self.tourTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Agent", None));
        ___qtablewidgetitem7 = self.tourTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Transportation", None));
        ___qtablewidgetitem8 = self.tourTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Decline", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.add_Travel_Agent_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem9 = self.travelagentTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem10 = self.travelagentTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Usename", None));
        ___qtablewidgetitem11 = self.travelagentTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem12 = self.travelagentTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem13 = self.travelagentTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem14 = self.travelagentTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        ___qtablewidgetitem15 = self.travelagentTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Hours", None));
        ___qtablewidgetitem16 = self.travelagentTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Travel Agents", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_2), QCoreApplication.translate("MainWindow", u"Team Leaders", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Drivers", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">STATS TO DO!!</span></p></body></html>", None))
    # retranslateUi

