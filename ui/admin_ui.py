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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.profitLabel = QLabel(self.requestPage)
        self.profitLabel.setObjectName(u"profitLabel")

        self.gridLayout_8.addWidget(self.profitLabel, 11, 1, 1, 1)

        self.totalCostLabel = QLabel(self.requestPage)
        self.totalCostLabel.setObjectName(u"totalCostLabel")

        self.gridLayout_8.addWidget(self.totalCostLabel, 10, 1, 1, 1)

        self.vehicleCostLabel = QLabel(self.requestPage)
        self.vehicleCostLabel.setObjectName(u"vehicleCostLabel")

        self.gridLayout_8.addWidget(self.vehicleCostLabel, 7, 1, 1, 1)

        self.guideCostLabel = QLabel(self.requestPage)
        self.guideCostLabel.setObjectName(u"guideCostLabel")

        self.gridLayout_8.addWidget(self.guideCostLabel, 8, 1, 1, 1)

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

        self.label_7 = QLabel(self.requestPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color:rgb(170, 217, 231);\n"
"padding: 5px;\n"
"border-radius: 7px;")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 3, 1, 1, 1)

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


        self.gridLayout_8.addLayout(self.verticalLayout_2, 1, 0, 11, 1)

        self.hotelshare_label = QLabel(self.requestPage)
        self.hotelshare_label.setObjectName(u"hotelshare_label")

        self.gridLayout_8.addWidget(self.hotelshare_label, 9, 1, 1, 1)

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
        self.verticalLayout_3 = QVBoxLayout(self.statsPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.statsPage)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"QTabBar{\n"
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
        self.tourStatsTab = QWidget()
        self.tourStatsTab.setObjectName(u"tourStatsTab")
        self.horizontalLayout = QHBoxLayout(self.tourStatsTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.tourStatsTab)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.toursPie = QHBoxLayout()
        self.toursPie.setObjectName(u"toursPie")

        self.verticalLayout_4.addLayout(self.toursPie)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_4.addWidget(self.label_13)

        self.toursBar = QHBoxLayout()
        self.toursBar.setObjectName(u"toursBar")

        self.verticalLayout_4.addLayout(self.toursBar)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.avgPeoplePTLbl = QLabel(self.widget_3)
        self.avgPeoplePTLbl.setObjectName(u"avgPeoplePTLbl")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.avgPeoplePTLbl)

        self.mostProfTourLbl = QLabel(self.widget_3)
        self.mostProfTourLbl.setObjectName(u"mostProfTourLbl")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.mostProfTourLbl)

        self.tourWthMosPplLbl = QLabel(self.widget_3)
        self.tourWthMosPplLbl.setObjectName(u"tourWthMosPplLbl")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.tourWthMosPplLbl)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.verticalLayout_4.setStretch(1, 4)
        self.verticalLayout_4.setStretch(3, 4)
        self.verticalLayout_4.setStretch(4, 2)

        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalLayout.setStretch(0, 5)
        self.tabWidget_2.addTab(self.tourStatsTab, "")
        self.vehiclesStatsTab = QWidget()
        self.vehiclesStatsTab.setObjectName(u"vehiclesStatsTab")
        self.horizontalLayout_5 = QHBoxLayout(self.vehiclesStatsTab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_8 = QWidget(self.vehiclesStatsTab)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_5.addWidget(self.label_14)

        self.busBar = QHBoxLayout()
        self.busBar.setObjectName(u"busBar")

        self.verticalLayout_5.addLayout(self.busBar)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.avgBusCostLbl = QLabel(self.widget_8)
        self.avgBusCostLbl.setObjectName(u"avgBusCostLbl")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.avgBusCostLbl)


        self.verticalLayout_5.addLayout(self.formLayout_2)

        self.verticalLayout_5.setStretch(1, 9)
        self.verticalLayout_5.setStretch(2, 1)

        self.horizontalLayout_4.addWidget(self.widget_8)

        self.horizontalLayout_4.setStretch(0, 5)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5.setStretch(0, 5)
        self.tabWidget_2.addTab(self.vehiclesStatsTab, "")
        self.driversStatsTab = QWidget()
        self.driversStatsTab.setObjectName(u"driversStatsTab")
        self.horizontalLayout_7 = QHBoxLayout(self.driversStatsTab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_10 = QWidget(self.driversStatsTab)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_6 = QVBoxLayout(self.widget_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_15 = QLabel(self.widget_10)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_6.addWidget(self.label_15)

        self.driversBar = QHBoxLayout()
        self.driversBar.setObjectName(u"driversBar")

        self.verticalLayout_6.addLayout(self.driversBar)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_16 = QLabel(self.widget_10)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.driverWithMostKmLbl = QLabel(self.widget_10)
        self.driverWithMostKmLbl.setObjectName(u"driverWithMostKmLbl")
        self.driverWithMostKmLbl.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.driverWithMostKmLbl)

        self.leastExpensiveDriverLbl = QLabel(self.widget_10)
        self.leastExpensiveDriverLbl.setObjectName(u"leastExpensiveDriverLbl")
        self.leastExpensiveDriverLbl.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.leastExpensiveDriverLbl)


        self.verticalLayout_6.addLayout(self.formLayout_3)

        self.verticalLayout_6.setStretch(1, 9)
        self.verticalLayout_6.setStretch(2, 1)

        self.horizontalLayout_6.addWidget(self.widget_10)

        self.widget_12 = QWidget(self.driversStatsTab)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.label_19 = QLabel(self.widget_12)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_8.addWidget(self.label_19)

        self.driverStatsListWidget = QListWidget(self.widget_12)
        self.driverStatsListWidget.setObjectName(u"driverStatsListWidget")
        self.driverStatsListWidget.setStyleSheet(u"QListWidget {\n"
"        font-size: 16px;\n"
"        color: rgb(18, 65, 141);\n"
"        background-color: white;\n"
"        border: 1px solid rgb(18, 65, 141);\n"
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

        self.verticalLayout_8.addWidget(self.driverStatsListWidget)

        self.driverslineEdit = QLineEdit(self.widget_12)
        self.driverslineEdit.setObjectName(u"driverslineEdit")
        self.driverslineEdit.setStyleSheet(u"QLineEdit {\n"
"        font-size: 16px;\n"
"        color: rgb(18, 65, 141);\n"
"        background-color: white;\n"
"        border: 1px solid rgb(18, 65, 141);\n"
"        border-radius: 6px;\n"
"    }")

        self.verticalLayout_8.addWidget(self.driverslineEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_7 = QVBoxLayout(self.widget_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_18 = QLabel(self.widget_13)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_7.addWidget(self.label_18)

        self.driversFavPie = QVBoxLayout()
        self.driversFavPie.setObjectName(u"driversFavPie")

        self.verticalLayout_7.addLayout(self.driversFavPie)

        self.label_10 = QLabel(self.widget_13)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.driverTourStatList = QTableWidget(self.widget_13)
        if (self.driverTourStatList.columnCount() < 3):
            self.driverTourStatList.setColumnCount(3)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.driverTourStatList.setHorizontalHeaderItem(0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.driverTourStatList.setHorizontalHeaderItem(1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.driverTourStatList.setHorizontalHeaderItem(2, __qtablewidgetitem58)
        self.driverTourStatList.setObjectName(u"driverTourStatList")

        self.verticalLayout_7.addWidget(self.driverTourStatList)

        self.verticalLayout_7.setStretch(1, 5)
        self.verticalLayout_7.setStretch(3, 5)

        self.horizontalLayout_8.addWidget(self.widget_13)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 7)

        self.horizontalLayout_6.addWidget(self.widget_12)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 5)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.tabWidget_2.addTab(self.driversStatsTab, "")
        self.leadersStatsTab = QWidget()
        self.leadersStatsTab.setObjectName(u"leadersStatsTab")
        self.horizontalLayout_11 = QHBoxLayout(self.leadersStatsTab)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_15 = QWidget(self.leadersStatsTab)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_9 = QVBoxLayout(self.widget_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_20 = QLabel(self.widget_15)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_9.addWidget(self.label_20)

        self.leadersBar = QHBoxLayout()
        self.leadersBar.setObjectName(u"leadersBar")

        self.verticalLayout_9.addLayout(self.leadersBar)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_21 = QLabel(self.widget_15)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.label_22 = QLabel(self.widget_15)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.leaderWithMostTourLbl = QLabel(self.widget_15)
        self.leaderWithMostTourLbl.setObjectName(u"leaderWithMostTourLbl")
        self.leaderWithMostTourLbl.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.leaderWithMostTourLbl)

        self.leastExpensiveLeaderLbl = QLabel(self.widget_15)
        self.leastExpensiveLeaderLbl.setObjectName(u"leastExpensiveLeaderLbl")
        self.leastExpensiveLeaderLbl.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.leastExpensiveLeaderLbl)


        self.verticalLayout_9.addLayout(self.formLayout_4)

        self.verticalLayout_9.setStretch(1, 9)
        self.verticalLayout_9.setStretch(2, 1)

        self.horizontalLayout_9.addWidget(self.widget_15)

        self.widget_17 = QWidget(self.leadersStatsTab)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.label_23 = QLabel(self.widget_17)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_10.addWidget(self.label_23)

        self.leaderStatsListWidget = QListWidget(self.widget_17)
        self.leaderStatsListWidget.setObjectName(u"leaderStatsListWidget")
        self.leaderStatsListWidget.setStyleSheet(u"QListWidget {\n"
"        font-size: 16px;\n"
"        color: rgb(18, 65, 141);\n"
"        background-color: white;\n"
"        border: 1px solid rgb(18, 65, 141);\n"
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

        self.verticalLayout_10.addWidget(self.leaderStatsListWidget)

        self.teamleaderslineEdit = QLineEdit(self.widget_17)
        self.teamleaderslineEdit.setObjectName(u"teamleaderslineEdit")
        self.teamleaderslineEdit.setStyleSheet(u"QLineEdit {\n"
"        font-size: 16px;\n"
"        color: rgb(18, 65, 141);\n"
"        background-color: white;\n"
"        border: 1px solid rgb(18, 65, 141);\n"
"        border-radius: 6px;\n"
"    }")

        self.verticalLayout_10.addWidget(self.teamleaderslineEdit)


        self.horizontalLayout_10.addLayout(self.verticalLayout_10)

        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_11 = QVBoxLayout(self.widget_18)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_24 = QLabel(self.widget_18)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_11.addWidget(self.label_24)

        self.leadersFavPie = QVBoxLayout()
        self.leadersFavPie.setObjectName(u"leadersFavPie")

        self.verticalLayout_11.addLayout(self.leadersFavPie)

        self.label_11 = QLabel(self.widget_18)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_11.addWidget(self.label_11)

        self.leaderTourStatList = QTableWidget(self.widget_18)
        if (self.leaderTourStatList.columnCount() < 3):
            self.leaderTourStatList.setColumnCount(3)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.leaderTourStatList.setHorizontalHeaderItem(0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.leaderTourStatList.setHorizontalHeaderItem(1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.leaderTourStatList.setHorizontalHeaderItem(2, __qtablewidgetitem61)
        self.leaderTourStatList.setObjectName(u"leaderTourStatList")

        self.verticalLayout_11.addWidget(self.leaderTourStatList)

        self.verticalLayout_11.setStretch(1, 5)
        self.verticalLayout_11.setStretch(3, 5)

        self.horizontalLayout_10.addWidget(self.widget_18)

        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 7)

        self.horizontalLayout_9.addWidget(self.widget_17)

        self.horizontalLayout_9.setStretch(0, 5)
        self.horizontalLayout_9.setStretch(1, 5)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)

        self.tabWidget_2.addTab(self.leadersStatsTab, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.statsPage)

        self.gridLayout_9.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)


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
        self.profitLabel.setText(QCoreApplication.translate("MainWindow", u"Profit:", None))
        self.totalCostLabel.setText(QCoreApplication.translate("MainWindow", u"Total Cost:", None))
        self.vehicleCostLabel.setText(QCoreApplication.translate("MainWindow", u"Vehicle Cost:", None))
        self.guideCostLabel.setText(QCoreApplication.translate("MainWindow", u" Guide Cost:", None))
        ___qtablewidgetitem11 = self.tourSummaryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Total People", None));
        ___qtablewidgetitem12 = self.tourSummaryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Total Cost", None));
        self.driverCostLabel.setText(QCoreApplication.translate("MainWindow", u"Driver Cost:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#12418d;\">Requests</span></p></body></html>", None))
        self.Driver_label.setText(QCoreApplication.translate("MainWindow", u"Select Driver", None))
        self.Vehicle_label.setText(QCoreApplication.translate("MainWindow", u"Select vehicle", None))
        self.Tour_Guide_label.setText(QCoreApplication.translate("MainWindow", u"Select Tour Guide", None))
        self.acceptTourButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.declineTourButton.setText(QCoreApplication.translate("MainWindow", u"Decline", None))
        self.hotelshare_label.setText(QCoreApplication.translate("MainWindow", u"Hotel Share:", None))
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
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tours By Transportation Type:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Profit / Destination:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Average People / Tour:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Most Profitable Tour:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tour With Most People:", None))
        self.avgPeoplePTLbl.setText("")
        self.mostProfTourLbl.setText("")
        self.tourWthMosPplLbl.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tourStatsTab), QCoreApplication.translate("MainWindow", u"Tours", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tours / Bus", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Average Cost:", None))
        self.avgBusCostLbl.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.vehiclesStatsTab), QCoreApplication.translate("MainWindow", u"Vehicles", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Tours / Driver", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Driver With Most km:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Cheapest Driver (By Day):", None))
        self.driverWithMostKmLbl.setText("")
        self.leastExpensiveDriverLbl.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Driver:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Favourite 3 Destinations:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tours Participated:", None))
        ___qtablewidgetitem56 = self.driverTourStatList.horizontalHeaderItem(0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Tour ID", None));
        ___qtablewidgetitem57 = self.driverTourStatList.horizontalHeaderItem(1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem58 = self.driverTourStatList.horizontalHeaderItem(2)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.driversStatsTab), QCoreApplication.translate("MainWindow", u"Drivers", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tours / Leader", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"T. Leader With Most Tours:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Cheapest T. Leader (By Day):", None))
        self.leaderWithMostTourLbl.setText("")
        self.leastExpensiveLeaderLbl.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Team Leader:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Favourite 3 Destinations:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tours Participated:", None))
        ___qtablewidgetitem59 = self.leaderTourStatList.horizontalHeaderItem(0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Tour ID", None));
        ___qtablewidgetitem60 = self.leaderTourStatList.horizontalHeaderItem(1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem61 = self.leaderTourStatList.horizontalHeaderItem(2)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.leadersStatsTab), QCoreApplication.translate("MainWindow", u"Team Leaders", None))
    # retranslateUi

