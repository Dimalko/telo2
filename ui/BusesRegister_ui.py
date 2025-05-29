# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BusesRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 775)
        MainWindow.setMinimumSize(QSize(531, 300))
        MainWindow.setMaximumSize(QSize(531, 16777215))
        MainWindow.setStyleSheet(u"QWidget{\n"
"background-color: rgb(243, 249, 254);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color: rgb(18, 65, 141);\n"
"font-size:16px;\n"
"padding-bottom: 0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid; \n"
"border-radius: 6px; \n"
"border-color:rgb(18, 65, 141);\n"
"padding: 8px;\n"
"color: rgb(18, 65, 141);\n"
"font-size:14px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid; \n"
"	border-radius: 6px; \n"
"	border-color:rgb(18, 65, 141);\n"
"	padding: 8px;\n"
"	color: rgb(18, 65, 141);\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 16px;\n"
"padding: 5px;\n"
"background-color: rgb(18, 65, 141);\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(230, 222, 255);  /* Background color of the scrollbar track */\n"
"    width: 12px;  /* Thickness of the s"
                        "crollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(18, 65, 141);\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"    border-radius: 6px; /* Rounded edges */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #74b9ff; /* Lighter color when hovered */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; /* Removes the small arrow buttons */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* Keeps empty space color same */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 517, 784))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelWidget = QWidget(self.scrollAreaWidgetContents)
        self.labelWidget.setObjectName(u"labelWidget")
        self.labelWidget.setStyleSheet(u"background-color: rgb(18, 65, 141);")
        self.horizontalLayout_2 = QHBoxLayout(self.labelWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.labelWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(243, 249, 254);")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.labelWidget)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.PlateNumberLabel = QLabel(self.widget_2)
        self.PlateNumberLabel.setObjectName(u"PlateNumberLabel")

        self.verticalLayout_4.addWidget(self.PlateNumberLabel)

        self.PlateNumberInput = QLineEdit(self.widget_2)
        self.PlateNumberInput.setObjectName(u"PlateNumberInput")
        self.PlateNumberInput.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.PlateNumberInput)

        self.ModelLabel = QLabel(self.widget_2)
        self.ModelLabel.setObjectName(u"ModelLabel")

        self.verticalLayout_4.addWidget(self.ModelLabel)

        self.ModelInput = QLineEdit(self.widget_2)
        self.ModelInput.setObjectName(u"ModelInput")
        self.ModelInput.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.ModelInput)

        self.YearLabel = QLabel(self.widget_2)
        self.YearLabel.setObjectName(u"YearLabel")

        self.verticalLayout_4.addWidget(self.YearLabel)

        self.YearInput = QLineEdit(self.widget_2)
        self.YearInput.setObjectName(u"YearInput")
        self.YearInput.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.YearInput)

        self.MileageLabel = QLabel(self.widget_2)
        self.MileageLabel.setObjectName(u"MileageLabel")

        self.verticalLayout_4.addWidget(self.MileageLabel)

        self.MileageInput = QLineEdit(self.widget_2)
        self.MileageInput.setObjectName(u"MileageInput")
        self.MileageInput.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.MileageInput)

        self.CompanyLabel = QLabel(self.widget_2)
        self.CompanyLabel.setObjectName(u"CompanyLabel")
        self.CompanyLabel.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.CompanyLabel)

        self.CompanyComboBox = QComboBox(self.widget_2)
        self.CompanyComboBox.addItem("")
        self.CompanyComboBox.addItem("")
        self.CompanyComboBox.setObjectName(u"CompanyComboBox")
        self.CompanyComboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid; \n"
"border-radius: 6px; \n"
"border-color:rgb(18, 65, 141);\n"
"padding: 8px;\n"
"color: rgb(18, 65, 141);\n"
"font-size:14px;")

        self.verticalLayout_4.addWidget(self.CompanyComboBox)

        self.Rental_CostLabel = QLabel(self.widget_2)
        self.Rental_CostLabel.setObjectName(u"Rental_CostLabel")

        self.verticalLayout_4.addWidget(self.Rental_CostLabel)

        self.Rental_CostInput = QLineEdit(self.widget_2)
        self.Rental_CostInput.setObjectName(u"Rental_CostInput")
        self.Rental_CostInput.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.Rental_CostInput)

        self.ConsumptionLabel = QLabel(self.widget_2)
        self.ConsumptionLabel.setObjectName(u"ConsumptionLabel")
        self.ConsumptionLabel.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.ConsumptionLabel)

        self.ConsumptionInput = QLineEdit(self.widget_2)
        self.ConsumptionInput.setObjectName(u"ConsumptionInput")
        self.ConsumptionInput.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.ConsumptionInput)

        self.SeatsLabel = QLabel(self.widget_2)
        self.SeatsLabel.setObjectName(u"SeatsLabel")

        self.verticalLayout_4.addWidget(self.SeatsLabel)

        self.SeatsInput = QLineEdit(self.widget_2)
        self.SeatsInput.setObjectName(u"SeatsInput")
        self.SeatsInput.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.SeatsInput)

        self.Contract_DateLabel = QLabel(self.widget_2)
        self.Contract_DateLabel.setObjectName(u"Contract_DateLabel")

        self.verticalLayout_4.addWidget(self.Contract_DateLabel)

        self.Contract_Date_dateEdit = QDateEdit(self.widget_2)
        self.Contract_Date_dateEdit.setObjectName(u"Contract_Date_dateEdit")
        self.Contract_Date_dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid; \n"
"border-radius: 6px; \n"
"border-color:rgb(18, 65, 141);\n"
"padding: 8px;\n"
"color: rgb(18, 65, 141);\n"
"font-size:14px;")

        self.verticalLayout_4.addWidget(self.Contract_Date_dateEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_Buses_button = QPushButton(self.widget_2)
        self.add_Buses_button.setObjectName(u"add_Buses_button")
        self.add_Buses_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Buses_button.sizePolicy().hasHeightForWidth())
        self.add_Buses_button.setSizePolicy(sizePolicy)
        self.add_Buses_button.setMinimumSize(QSize(200, 25))
        self.add_Buses_button.setMaximumSize(QSize(200, 16777215))
        self.add_Buses_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_Buses_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.add_Buses_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Buses Register", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Bus Register</span></p></body></html>", None))
        self.PlateNumberLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Plate Number</p></body></html>", None))
        self.ModelLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Model</span></p></body></html>", None))
        self.YearLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Year</span></p></body></html>", None))
        self.MileageLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Mileage</span></p></body></html>", None))
        self.CompanyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Company</p></body></html>", None))
        self.CompanyComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Owned", None))
        self.CompanyComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Rental", None))

        self.Rental_CostLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Rental Cost</p></body></html>", None))
        self.ConsumptionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Consumption</p></body></html>", None))
        self.SeatsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Seats</span></p></body></html>", None))
        self.Contract_DateLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Contract Date</span></p></body></html>", None))
        self.add_Buses_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

