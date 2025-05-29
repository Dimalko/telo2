# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agent.ui'
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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(907, 665)
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/app_icon_blue_32x32.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
"}\n"
"\n"
"QTableWidget {\n"
"border:none;\n"
"background-color: white; \n"
"alternate-background-color: #f0f0f0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(18, 65, 141);            \n"
"	color: rgb(243, 249, 254);\n"
"    font: 57 8pt \"Yu Gothic Medium\";\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(24, 89, 193); \n"
"}\n"
"\n"
"#QTableWidget QTableCornerButton::section {\n"
"    background-color: #74b9ff; /* Top-left corner color */\n"
"    border: 1px solid #0984e3;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #dfe6e9;  /* Background color of the scrollbar track */\n"
"    height: 12px;  /* Thickness of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;\n"
""
                        "}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0984e3; /* Color of the scrollbar handle (slider) */\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"    border-radius: 6px; /* Rounded edges */\n"
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
"}\n"
"\n"
"QListWidget{\n"
"	border: 1px solid rgb(161, 161, 161);	\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid rgb(18, 65, 141);	\n"
"	border-radius: 9px;\n"
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
"border-radius: 0px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 10px;\n"
"border-bottom: 2px solid #74b9ff;\n"
"}")

        self.verticalLayout.addWidget(self.homeBtn)

        self.reservationsBtn = QPushButton(self.widget)
        self.reservationsBtn.setObjectName(u"reservationsBtn")
        self.reservationsBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"border-radius: 0px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 10px;\n"
"border-bottom: 2px solid #74b9ff;\n"
"}")

        self.verticalLayout.addWidget(self.reservationsBtn)

        self.staffBtn = QPushButton(self.widget)
        self.staffBtn.setObjectName(u"staffBtn")
        self.staffBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"border-radius: 0px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 10px;\n"
"border-bottom: 2px solid #74b9ff;\n"
"}")

        self.verticalLayout.addWidget(self.staffBtn)

        self.vehiclesBtn = QPushButton(self.widget)
        self.vehiclesBtn.setObjectName(u"vehiclesBtn")
        self.vehiclesBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"border-radius: 0px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 10px;\n"
"border-bottom: 2px solid #74b9ff;\n"
"}")

        self.verticalLayout.addWidget(self.vehiclesBtn)

        self.statsBtn = QPushButton(self.widget)
        self.statsBtn.setObjectName(u"statsBtn")
        self.statsBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"border-radius: 0px;\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 10px;\n"
"border-bottom: 2px solid #74b9ff;\n"
"}")

        self.verticalLayout.addWidget(self.statsBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logOutBtn = QPushButton(self.widget)
        self.logOutBtn.setObjectName(u"logOutBtn")
        self.logOutBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\n"
"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(233, 128, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}\n"
"*/")

        self.verticalLayout.addWidget(self.logOutBtn)


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
        self.tourTableWidget.setStyleSheet(u"")
        self.tourTableWidget.setCornerButtonEnabled(True)

        self.gridLayout.addWidget(self.tourTableWidget, 1, 0, 1, 3)

        self.createTourDescriptionBtn = QPushButton(self.homePage)
        self.createTourDescriptionBtn.setObjectName(u"createTourDescriptionBtn")
        self.createTourDescriptionBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:#74b9ff;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(136, 205, 255);\n"
"}")

        self.gridLayout.addWidget(self.createTourDescriptionBtn, 2, 0, 1, 3)

        self.label_2 = QLabel(self.homePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.homePage)
        self.reservationsPage = QWidget()
        self.reservationsPage.setObjectName(u"reservationsPage")
        self.reservationsPage.setStyleSheet(u"QListWidget {\n"
"    border: none;\n"
"    background-color: white;\n"
"    alternate-background-color: #f0f0f0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0078d7;  /* \u039c\u03c0\u03bb\u03b5 highlight */\n"
"    color: white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.reservationsPage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.reservationsPage)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.TourlistWidget = QListWidget(self.reservationsPage)
        self.TourlistWidget.setObjectName(u"TourlistWidget")
        self.TourlistWidget.setStyleSheet(u"QListWidget {\n"
"        font-size: 16px;\n"
"        color: rgb(18, 65, 141);\n"
"        background-color: white;\n"
"        border: 2px solid rgb(18, 65, 141);\n"
"        border-radius: 6px;\n"
"    }\n"
"    QListWidget::item {\n"
"        padding: 6px;\n"
"    }\n"
"    QListWidget::item:selected {\n"
"        background-color: rgb(18, 65, 141);\n"
"        color: white;\n"
"        border-radius: 4px;\n"
"    }")

        self.verticalLayout_2.addWidget(self.TourlistWidget)

        self.TourslineEdit = QLineEdit(self.reservationsPage)
        self.TourslineEdit.setObjectName(u"TourslineEdit")
        self.TourslineEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid rgb(18, 65, 141);	\n"
"	border-radius: 9px;\n"
"}")

        self.verticalLayout_2.addWidget(self.TourslineEdit)

        self.add_Reservation_Button = QPushButton(self.reservationsPage)
        self.add_Reservation_Button.setObjectName(u"add_Reservation_Button")
        self.add_Reservation_Button.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.verticalLayout_2.addWidget(self.add_Reservation_Button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.ReservationtableWidget = QTableWidget(self.reservationsPage)
        if (self.ReservationtableWidget.columnCount() < 6):
            self.ReservationtableWidget.setColumnCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ReservationtableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ReservationtableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ReservationtableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ReservationtableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ReservationtableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ReservationtableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        self.ReservationtableWidget.setObjectName(u"ReservationtableWidget")

        self.verticalLayout_3.addWidget(self.ReservationtableWidget)

        self.widget_3 = QWidget(self.reservationsPage)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_3.addWidget(self.widget_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.widget_4 = QWidget(self.reservationsPage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(246, 32))
        self.widget_4.setMaximumSize(QSize(246, 32))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"    border: 1px solid rgb(161, 161, 161);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QWidget QLabel {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: rgb(18, 65, 141);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border: none;")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.TotalCostlabel = QLabel(self.widget_4)
        self.TotalCostlabel.setObjectName(u"TotalCostlabel")
        self.TotalCostlabel.setStyleSheet(u"border:none;")

        self.horizontalLayout_4.addWidget(self.TotalCostlabel)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 6)

        self.horizontalLayout_3.addWidget(self.widget_4)

        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)
        self.stackedWidget.addWidget(self.reservationsPage)
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
        self.travelagentTableWidget = QTableWidget(self.tab_2)
        if (self.travelagentTableWidget.columnCount() < 8):
            self.travelagentTableWidget.setColumnCount(8)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        self.travelagentTableWidget.setObjectName(u"travelagentTableWidget")
        self.travelagentTableWidget.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.travelagentTableWidget, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.teamleaderTableWidget = QTableWidget(self.widget_2)
        if (self.teamleaderTableWidget.columnCount() < 5):
            self.teamleaderTableWidget.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.teamleaderTableWidget.setObjectName(u"teamleaderTableWidget")
        self.teamleaderTableWidget.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.teamleaderTableWidget, 0, 0, 1, 2)

        self.tabWidget.addTab(self.widget_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.driverTableWidget = QTableWidget(self.tab)
        if (self.driverTableWidget.columnCount() < 6):
            self.driverTableWidget.setColumnCount(6)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        self.driverTableWidget.setObjectName(u"driverTableWidget")

        self.gridLayout_5.addWidget(self.driverTableWidget, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.staffPage)
        self.vehiclePage = QWidget()
        self.vehiclePage.setObjectName(u"vehiclePage")
        self.gridLayout_6 = QGridLayout(self.vehiclePage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.busesTableWidget = QTableWidget(self.vehiclePage)
        if (self.busesTableWidget.columnCount() < 9):
            self.busesTableWidget.setColumnCount(9)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem42)
        self.busesTableWidget.setObjectName(u"busesTableWidget")

        self.gridLayout_6.addWidget(self.busesTableWidget, 0, 0, 1, 2)

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

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Agent Window", None))
        self.logoLabel.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Tours", None))
        self.reservationsBtn.setText(QCoreApplication.translate("MainWindow", u"Reservations", None))
        self.staffBtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.vehiclesBtn.setText(QCoreApplication.translate("MainWindow", u"Vehicles", None))
        self.statsBtn.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.logOutBtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
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
        self.createTourDescriptionBtn.setText(QCoreApplication.translate("MainWindow", u"Create Tour Description \ud83d\udcdd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tours", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Scheduled Tours</p></body></html>", None))
        self.add_Reservation_Button.setText(QCoreApplication.translate("MainWindow", u"Create Reservation", None))
        ___qtablewidgetitem9 = self.ReservationtableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem10 = self.ReservationtableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Client Name", None));
        ___qtablewidgetitem11 = self.ReservationtableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Number Of People", None));
        ___qtablewidgetitem12 = self.ReservationtableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Hotel", None));
        ___qtablewidgetitem13 = self.ReservationtableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        ___qtablewidgetitem14 = self.ReservationtableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Payment Type", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Cost:", None))
        self.TotalCostlabel.setText(QCoreApplication.translate("MainWindow", u"--", None))
        ___qtablewidgetitem15 = self.travelagentTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem16 = self.travelagentTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Usename", None));
        ___qtablewidgetitem17 = self.travelagentTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem18 = self.travelagentTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem19 = self.travelagentTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem20 = self.travelagentTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        ___qtablewidgetitem21 = self.travelagentTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Hours", None));
        ___qtablewidgetitem22 = self.travelagentTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Travel Agents", None))
        ___qtablewidgetitem23 = self.teamleaderTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem24 = self.teamleaderTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem25 = self.teamleaderTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem26 = self.teamleaderTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Payment", None));
        ___qtablewidgetitem27 = self.teamleaderTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Skills", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_2), QCoreApplication.translate("MainWindow", u"Team Leaders", None))
        ___qtablewidgetitem28 = self.driverTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Tax Code", None));
        ___qtablewidgetitem29 = self.driverTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem30 = self.driverTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem31 = self.driverTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem32 = self.driverTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem33 = self.driverTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Drivers", None))
        ___qtablewidgetitem34 = self.busesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Plate Number", None));
        ___qtablewidgetitem35 = self.busesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Model", None));
        ___qtablewidgetitem36 = self.busesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Year", None));
        ___qtablewidgetitem37 = self.busesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Mileage", None));
        ___qtablewidgetitem38 = self.busesTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem39 = self.busesTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"RentalCost", None));
        ___qtablewidgetitem40 = self.busesTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Seats", None));
        ___qtablewidgetitem41 = self.busesTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem42 = self.busesTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Contract Date", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">STATS TO DO!!</span></p></body></html>", None))
    # retranslateUi

