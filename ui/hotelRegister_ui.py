# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hotelRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 775)
        MainWindow.setMinimumSize(QSize(531, 300))
        MainWindow.setMaximumSize(QSize(531, 775))
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
"    width: 12px;  /* Thickness of the scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(18, 65, 141);\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"    border-radius: 6px; /* Rounded edges */\n"
"}\n"
"\n"
"QScrollBa"
                        "r::handle:vertical:hover {\n"
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
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 529, 773))
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

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.verticalLayout.addWidget(self.passwordLabel)

        self.hotelNameInput = QLineEdit(self.widget)
        self.hotelNameInput.setObjectName(u"hotelNameInput")
        self.hotelNameInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.hotelNameInput)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.hotelCityInput = QLineEdit(self.widget)
        self.hotelCityInput.setObjectName(u"hotelCityInput")

        self.verticalLayout.addWidget(self.hotelCityInput)

        self.FirstNameLabel = QLabel(self.widget)
        self.FirstNameLabel.setObjectName(u"FirstNameLabel")

        self.verticalLayout.addWidget(self.FirstNameLabel)

        self.hotelAddressInput = QLineEdit(self.widget)
        self.hotelAddressInput.setObjectName(u"hotelAddressInput")
        self.hotelAddressInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.hotelAddressInput)

        self.LastNameLabel = QLabel(self.widget)
        self.LastNameLabel.setObjectName(u"LastNameLabel")

        self.verticalLayout.addWidget(self.LastNameLabel)

        self.hotelPriceInput = QLineEdit(self.widget)
        self.hotelPriceInput.setObjectName(u"hotelPriceInput")
        self.hotelPriceInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.hotelPriceInput)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_Hotel_button = QPushButton(self.widget)
        self.add_Hotel_button.setObjectName(u"add_Hotel_button")
        self.add_Hotel_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Hotel_button.sizePolicy().hasHeightForWidth())
        self.add_Hotel_button.setSizePolicy(sizePolicy)
        self.add_Hotel_button.setMinimumSize(QSize(200, 25))
        self.add_Hotel_button.setMaximumSize(QSize(200, 16777215))
        self.add_Hotel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_Hotel_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.add_Hotel_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Travel Agents", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Hotel register</span></p></body></html>", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">City</span></p></body></html>", None))
        self.FirstNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Address</span></p></body></html>", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Price Per Person</span></p></body></html>", None))
        self.add_Hotel_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

