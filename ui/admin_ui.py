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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 665)
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
"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
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

        self.requestBtn = QPushButton(self.widget)
        self.requestBtn.setObjectName(u"requestBtn")
        self.requestBtn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.requestBtn)

        self.ongoingBtn = QPushButton(self.widget)
        self.ongoingBtn.setObjectName(u"ongoingBtn")
        self.ongoingBtn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.ongoingBtn)

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

        self.hotelsBtn = QPushButton(self.widget)
        self.hotelsBtn.setObjectName(u"hotelsBtn")
        self.hotelsBtn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.hotelsBtn)

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


        self.gridLayout_9.addWidget(self.widget, 0, 0, 1, 1)

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
        self.removeTourBtn = QPushButton(self.homePage)
        self.removeTourBtn.setObjectName(u"removeTourBtn")
        self.removeTourBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout.addWidget(self.removeTourBtn, 2, 1, 1, 1)

        self.add_Tour_button = QPushButton(self.homePage)
        self.add_Tour_button.setObjectName(u"add_Tour_button")
        self.add_Tour_button.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.add_Tour_button, 2, 0, 1, 1)

        self.editTourBtn = QPushButton(self.homePage)
        self.editTourBtn.setObjectName(u"editTourBtn")
        self.editTourBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:rgb(234, 129, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}")

        self.gridLayout.addWidget(self.editTourBtn, 2, 2, 1, 1)

        self.tourTableWidget = QTableWidget(self.homePage)
        if (self.tourTableWidget.columnCount() < 11):
            self.tourTableWidget.setColumnCount(11)
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
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tourTableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
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
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(136, 205, 255);\n"
"}")

        self.gridLayout.addWidget(self.createTourDescriptionBtn, 3, 0, 1, 3)

        self.label_2 = QLabel(self.homePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color:rgb(170, 217, 231);\n"
"padding: 5px;\n"
"border-radius: 7px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.homePage)
        self.requestPage = QWidget()
        self.requestPage.setObjectName(u"requestPage")
        self.gridLayout_8 = QGridLayout(self.requestPage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.totalCostLabel = QLabel(self.requestPage)
        self.totalCostLabel.setObjectName(u"totalCostLabel")

        self.gridLayout_8.addWidget(self.totalCostLabel, 9, 1, 1, 1)

        self.profitLabel = QLabel(self.requestPage)
        self.profitLabel.setObjectName(u"profitLabel")

        self.gridLayout_8.addWidget(self.profitLabel, 10, 1, 1, 1)

        self.guideCostLabel = QLabel(self.requestPage)
        self.guideCostLabel.setObjectName(u"guideCostLabel")

        self.gridLayout_8.addWidget(self.guideCostLabel, 8, 1, 1, 1)

        self.vehicleCostLabel = QLabel(self.requestPage)
        self.vehicleCostLabel.setObjectName(u"vehicleCostLabel")

        self.gridLayout_8.addWidget(self.vehicleCostLabel, 7, 1, 1, 1)

        self.tourSummaryTable = QTableWidget(self.requestPage)
        if (self.tourSummaryTable.columnCount() < 2):
            self.tourSummaryTable.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tourSummaryTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tourSummaryTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        self.tourSummaryTable.setObjectName(u"tourSummaryTable")

        self.gridLayout_8.addWidget(self.tourSummaryTable, 1, 1, 1, 1)

        self.driverCostLabel = QLabel(self.requestPage)
        self.driverCostLabel.setObjectName(u"driverCostLabel")

        self.gridLayout_8.addWidget(self.driverCostLabel, 6, 1, 1, 1)

        self.LabelLayout = QHBoxLayout()
        self.LabelLayout.setObjectName(u"LabelLayout")
        self.Driver_label = QLabel(self.requestPage)
        self.Driver_label.setObjectName(u"Driver_label")
        self.Driver_label.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"")

        self.LabelLayout.addWidget(self.Driver_label)

        self.Vehicle_label = QLabel(self.requestPage)
        self.Vehicle_label.setObjectName(u"Vehicle_label")
        self.Vehicle_label.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.LabelLayout.addWidget(self.Vehicle_label)

        self.Tour_Guide_label = QLabel(self.requestPage)
        self.Tour_Guide_label.setObjectName(u"Tour_Guide_label")
        self.Tour_Guide_label.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.LabelLayout.addWidget(self.Tour_Guide_label)


        self.gridLayout_8.addLayout(self.LabelLayout, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.driverComboBox = QComboBox(self.requestPage)
        self.driverComboBox.setObjectName(u"driverComboBox")
        self.driverComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.driverComboBox)

        self.vehicleComboBox = QComboBox(self.requestPage)
        self.vehicleComboBox.setObjectName(u"vehicleComboBox")
        self.vehicleComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.vehicleComboBox)

        self.guideComboBox = QComboBox(self.requestPage)
        self.guideComboBox.setObjectName(u"guideComboBox")
        self.guideComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.guideComboBox)


        self.gridLayout_8.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)

        self.label_7 = QLabel(self.requestPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color:rgb(170, 217, 231);\n"
"padding: 5px;\n"
"border-radius: 7px;")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.TourlistWidget = QListWidget(self.requestPage)
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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.acceptTourButton = QPushButton(self.requestPage)
        self.acceptTourButton.setObjectName(u"acceptTourButton")
        self.acceptTourButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.acceptTourButton)

        self.declineTourButton = QPushButton(self.requestPage)
        self.declineTourButton.setObjectName(u"declineTourButton")
        self.declineTourButton.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"	background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.horizontalLayout_2.addWidget(self.declineTourButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 1, 0, 10, 1)

        self.gridLayout_8.setColumnStretch(0, 2)
        self.gridLayout_8.setColumnStretch(1, 8)
        self.stackedWidget.addWidget(self.requestPage)
        self.ongoingPage = QWidget()
        self.ongoingPage.setObjectName(u"ongoingPage")
        self.gridLayout_10 = QGridLayout(self.ongoingPage)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.completeTourButton = QPushButton(self.ongoingPage)
        self.completeTourButton.setObjectName(u"completeTourButton")
        self.completeTourButton.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(8, 123, 225);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"border-bottom: 2px solid #74b9ff;\n"
"}")

        self.gridLayout_10.addWidget(self.completeTourButton, 2, 1, 1, 1)

        self.ongoingTourListWidget = QListWidget(self.ongoingPage)
        self.ongoingTourListWidget.setObjectName(u"ongoingTourListWidget")
        self.ongoingTourListWidget.setStyleSheet(u"QListWidget {\n"
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

        self.gridLayout_10.addWidget(self.ongoingTourListWidget, 1, 0, 2, 1)

        self.label = QLabel(self.ongoingPage)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color:rgb(170, 217, 231);\n"
"padding: 5px;\n"
"border-radius: 7px;")

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 2)

        self.ongoingTourDetailsTable = QTableWidget(self.ongoingPage)
        if (self.ongoingTourDetailsTable.columnCount() < 8):
            self.ongoingTourDetailsTable.setColumnCount(8)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.ongoingTourDetailsTable.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        self.ongoingTourDetailsTable.setObjectName(u"ongoingTourDetailsTable")

        self.gridLayout_10.addWidget(self.ongoingTourDetailsTable, 1, 1, 1, 1)

        self.gridLayout_10.setColumnStretch(0, 2)
        self.gridLayout_10.setColumnStretch(1, 8)
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

        self.editAgentBtn = QPushButton(self.tab_2)
        self.editAgentBtn.setObjectName(u"editAgentBtn")
        self.editAgentBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:rgb(234, 129, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}")

        self.gridLayout_3.addWidget(self.editAgentBtn, 1, 2, 1, 1)

        self.removeAgentBtn = QPushButton(self.tab_2)
        self.removeAgentBtn.setObjectName(u"removeAgentBtn")
        self.removeAgentBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_3.addWidget(self.removeAgentBtn, 1, 1, 1, 1)

        self.travelagentTableWidget = QTableWidget(self.tab_2)
        if (self.travelagentTableWidget.columnCount() < 8):
            self.travelagentTableWidget.setColumnCount(8)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.travelagentTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem28)
        self.travelagentTableWidget.setObjectName(u"travelagentTableWidget")
        self.travelagentTableWidget.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.travelagentTableWidget, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.teamleaderTableWidget = QTableWidget(self.widget_2)
        if (self.teamleaderTableWidget.columnCount() < 6):
            self.teamleaderTableWidget.setColumnCount(6)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.teamleaderTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        self.teamleaderTableWidget.setObjectName(u"teamleaderTableWidget")
        self.teamleaderTableWidget.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.teamleaderTableWidget, 0, 0, 1, 3)

        self.add_Team_Leader_button = QPushButton(self.widget_2)
        self.add_Team_Leader_button.setObjectName(u"add_Team_Leader_button")
        self.add_Team_Leader_button.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_4.addWidget(self.add_Team_Leader_button, 1, 0, 1, 1)

        self.removeTeamLeaderBtn = QPushButton(self.widget_2)
        self.removeTeamLeaderBtn.setObjectName(u"removeTeamLeaderBtn")
        self.removeTeamLeaderBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_4.addWidget(self.removeTeamLeaderBtn, 1, 1, 1, 1)

        self.editLeaderBtn = QPushButton(self.widget_2)
        self.editLeaderBtn.setObjectName(u"editLeaderBtn")
        self.editLeaderBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:rgb(234, 129, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}")

        self.gridLayout_4.addWidget(self.editLeaderBtn, 1, 2, 1, 1)

        self.tabWidget.addTab(self.widget_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.driverTableWidget = QTableWidget(self.tab)
        if (self.driverTableWidget.columnCount() < 6):
            self.driverTableWidget.setColumnCount(6)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.driverTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        self.driverTableWidget.setObjectName(u"driverTableWidget")

        self.gridLayout_5.addWidget(self.driverTableWidget, 0, 0, 1, 3)

        self.removeDriverBtn = QPushButton(self.tab)
        self.removeDriverBtn.setObjectName(u"removeDriverBtn")
        self.removeDriverBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_5.addWidget(self.removeDriverBtn, 1, 1, 1, 1)

        self.add_Driver_Button = QPushButton(self.tab)
        self.add_Driver_Button.setObjectName(u"add_Driver_Button")
        self.add_Driver_Button.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_5.addWidget(self.add_Driver_Button, 1, 0, 1, 1)

        self.editDriverBtn = QPushButton(self.tab)
        self.editDriverBtn.setObjectName(u"editDriverBtn")
        self.editDriverBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:rgb(234, 129, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}")

        self.gridLayout_5.addWidget(self.editDriverBtn, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.staffPage)
        self.vehiclePage = QWidget()
        self.vehiclePage.setObjectName(u"vehiclePage")
        self.gridLayout_6 = QGridLayout(self.vehiclePage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.busesTableWidget = QTableWidget(self.vehiclePage)
        if (self.busesTableWidget.columnCount() < 10):
            self.busesTableWidget.setColumnCount(10)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.busesTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem50)
        self.busesTableWidget.setObjectName(u"busesTableWidget")

        self.gridLayout_6.addWidget(self.busesTableWidget, 1, 0, 1, 3)

        self.Add_Buses_Button = QPushButton(self.vehiclePage)
        self.Add_Buses_Button.setObjectName(u"Add_Buses_Button")
        self.Add_Buses_Button.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_6.addWidget(self.Add_Buses_Button, 2, 0, 1, 1)

        self.editVehicleBtn = QPushButton(self.vehiclePage)
        self.editVehicleBtn.setObjectName(u"editVehicleBtn")
        self.editVehicleBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:rgb(234, 129, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}")

        self.gridLayout_6.addWidget(self.editVehicleBtn, 2, 2, 1, 1)

        self.removeBusBtn = QPushButton(self.vehiclePage)
        self.removeBusBtn.setObjectName(u"removeBusBtn")
        self.removeBusBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_6.addWidget(self.removeBusBtn, 2, 1, 1, 1)

        self.label_4 = QLabel(self.vehiclePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color:rgb(170, 217, 231);\n"
"padding: 5px;\n"
"border-radius: 7px;")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.vehiclePage)
        self.hotelsPage = QWidget()
        self.hotelsPage.setObjectName(u"hotelsPage")
        self.gridLayout_7 = QGridLayout(self.hotelsPage)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.editHotelBtn = QPushButton(self.hotelsPage)
        self.editHotelBtn.setObjectName(u"editHotelBtn")
        self.editHotelBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:rgb(234, 129, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}")

        self.gridLayout_7.addWidget(self.editHotelBtn, 2, 2, 1, 1)

        self.removeHotelBtn = QPushButton(self.hotelsPage)
        self.removeHotelBtn.setObjectName(u"removeHotelBtn")
        self.removeHotelBtn.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")

        self.gridLayout_7.addWidget(self.removeHotelBtn, 2, 1, 1, 1)

        self.hotelTableWidget = QTableWidget(self.hotelsPage)
        if (self.hotelTableWidget.columnCount() < 5):
            self.hotelTableWidget.setColumnCount(5)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.hotelTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.hotelTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.hotelTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.hotelTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.hotelTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem55)
        self.hotelTableWidget.setObjectName(u"hotelTableWidget")

        self.gridLayout_7.addWidget(self.hotelTableWidget, 1, 0, 1, 3)

        self.addHotelBtn = QPushButton(self.hotelsPage)
        self.addHotelBtn.setObjectName(u"addHotelBtn")
        self.addHotelBtn.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_7.addWidget(self.addHotelBtn, 2, 0, 1, 1)

        self.label_5 = QLabel(self.hotelsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color:rgb(170, 217, 231);\n"
"padding: 5px;\n"
"border-radius: 7px;")

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.hotelsPage)
        self.statsPage = QWidget()
        self.statsPage.setObjectName(u"statsPage")
        self.label_3 = QLabel(self.statsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 270, 201, 81))
        self.label_6 = QLabel(self.statsPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 30, 361, 61))
        self.label_6.setStyleSheet(u"background-color:rgb(170, 217, 231);\n"
"padding: 5px;\n"
"border-radius: 7px;")
        self.stackedWidget.addWidget(self.statsPage)

        self.gridLayout_9.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLabel.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Tours", None))
        self.requestBtn.setText(QCoreApplication.translate("MainWindow", u"Requests", None))
        self.ongoingBtn.setText(QCoreApplication.translate("MainWindow", u"Ongoing Trips", None))
        self.staffBtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.vehiclesBtn.setText(QCoreApplication.translate("MainWindow", u"Vehicles", None))
        self.hotelsBtn.setText(QCoreApplication.translate("MainWindow", u"Hotels", None))
        self.statsBtn.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.logOutBtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.removeTourBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.add_Tour_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editTourBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
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
        ___qtablewidgetitem9 = self.tourTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Activities", None));
        ___qtablewidgetitem10 = self.tourTableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Hotels", None));
        self.createTourDescriptionBtn.setText(QCoreApplication.translate("MainWindow", u"Create Tour Description \ud83d\udcdd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#12418d;\">Tours</span></p></body></html>", None))
        self.totalCostLabel.setText(QCoreApplication.translate("MainWindow", u"Total Cost:", None))
        self.profitLabel.setText(QCoreApplication.translate("MainWindow", u"Profit:", None))
        self.guideCostLabel.setText(QCoreApplication.translate("MainWindow", u" Guide Cost:", None))
        self.vehicleCostLabel.setText(QCoreApplication.translate("MainWindow", u"Vehicle Cost:", None))
        ___qtablewidgetitem11 = self.tourSummaryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Total People", None));
        ___qtablewidgetitem12 = self.tourSummaryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None));
        self.driverCostLabel.setText(QCoreApplication.translate("MainWindow", u"Driver Cost:", None))
        self.Driver_label.setText(QCoreApplication.translate("MainWindow", u"Select Driver", None))
        self.Vehicle_label.setText(QCoreApplication.translate("MainWindow", u"Select vehicle", None))
        self.Tour_Guide_label.setText(QCoreApplication.translate("MainWindow", u"Select Tour Guide", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#12418d;\">Requests</span></p></body></html>", None))
        self.acceptTourButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.declineTourButton.setText(QCoreApplication.translate("MainWindow", u"Decline", None))
        self.completeTourButton.setText(QCoreApplication.translate("MainWindow", u"Complete Tour", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Ongoing Trips</span></p></body></html>", None))
        ___qtablewidgetitem13 = self.ongoingTourDetailsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem14 = self.ongoingTourDetailsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Dates", None));
        ___qtablewidgetitem15 = self.ongoingTourDetailsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Total Income", None));
        ___qtablewidgetitem16 = self.ongoingTourDetailsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Participants", None));
        ___qtablewidgetitem17 = self.ongoingTourDetailsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Transportation", None));
        ___qtablewidgetitem18 = self.ongoingTourDetailsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Transportation Cost", None));
        ___qtablewidgetitem19 = self.ongoingTourDetailsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Driver", None));
        ___qtablewidgetitem20 = self.ongoingTourDetailsTable.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Tour Guide", None));
        self.add_Travel_Agent_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editAgentBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.removeAgentBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem21 = self.travelagentTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem22 = self.travelagentTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Usename", None));
        ___qtablewidgetitem23 = self.travelagentTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem24 = self.travelagentTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem25 = self.travelagentTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem26 = self.travelagentTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        ___qtablewidgetitem27 = self.travelagentTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Hours", None));
        ___qtablewidgetitem28 = self.travelagentTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Travel Agents", None))
        ___qtablewidgetitem29 = self.teamleaderTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem30 = self.teamleaderTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem31 = self.teamleaderTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem32 = self.teamleaderTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Payment", None));
        ___qtablewidgetitem33 = self.teamleaderTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Skills", None));
        ___qtablewidgetitem34 = self.teamleaderTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.add_Team_Leader_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeTeamLeaderBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.editLeaderBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget_2), QCoreApplication.translate("MainWindow", u"Team Leaders", None))
        ___qtablewidgetitem35 = self.driverTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Tax Code", None));
        ___qtablewidgetitem36 = self.driverTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem37 = self.driverTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem38 = self.driverTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem39 = self.driverTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem40 = self.driverTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.removeDriverBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.add_Driver_Button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editDriverBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Drivers", None))
        ___qtablewidgetitem41 = self.busesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Plate Number", None));
        ___qtablewidgetitem42 = self.busesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Model", None));
        ___qtablewidgetitem43 = self.busesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Year", None));
        ___qtablewidgetitem44 = self.busesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Mileage", None));
        ___qtablewidgetitem45 = self.busesTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Company", None));
        ___qtablewidgetitem46 = self.busesTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"RentalCost", None));
        ___qtablewidgetitem47 = self.busesTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Consumption", None));
        ___qtablewidgetitem48 = self.busesTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Seats", None));
        ___qtablewidgetitem49 = self.busesTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem50 = self.busesTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Contract Date", None));
        self.Add_Buses_Button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.editVehicleBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.removeBusBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#12418d;\">Vehicles</span></p></body></html>", None))
        self.editHotelBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.removeHotelBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem51 = self.hotelTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem52 = self.hotelTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem53 = self.hotelTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem54 = self.hotelTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem55 = self.hotelTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Price Per Person", None));
        self.addHotelBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#12418d;\">Hotels</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">STATS TO DO!!</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#12418d;\">Statistics</span></p></body></html>", None))
    # retranslateUi

