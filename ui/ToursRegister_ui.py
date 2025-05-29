# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToursRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 775)
        MainWindow.setMinimumSize(QSize(531, 300))
        MainWindow.setMaximumSize(QSize(531, 775))
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/app_icon_blue_32x32.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 531, 775))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelWidget = QWidget(self.scrollAreaWidgetContents)
        self.labelWidget.setObjectName(u"labelWidget")
        self.labelWidget.setStyleSheet(u"background-color: rgb(18, 65, 141);")
        self.horizontalLayout_2 = QHBoxLayout(self.labelWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.destinationLabel = QLabel(self.widget)
        self.destinationLabel.setObjectName(u"destinationLabel")

        self.verticalLayout.addWidget(self.destinationLabel)

        self.destinationInput = QLineEdit(self.widget)
        self.destinationInput.setObjectName(u"destinationInput")
        self.destinationInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.destinationInput)

        self.start_dateLabel = QLabel(self.widget)
        self.start_dateLabel.setObjectName(u"start_dateLabel")

        self.verticalLayout.addWidget(self.start_dateLabel)

        self.start_dateEdit = QDateEdit(self.widget)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid; \n"
"border-radius: 6px; \n"
"border-color:rgb(18, 65, 141);\n"
"padding: 8px;\n"
"color: rgb(18, 65, 141);\n"
"font-size:14px;")
        self.start_dateEdit.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.start_dateEdit.setFrame(True)
        self.start_dateEdit.setReadOnly(False)
        self.start_dateEdit.setCurrentSection(QDateTimeEdit.DaySection)

        self.verticalLayout.addWidget(self.start_dateEdit)

        self.end_dateLabel = QLabel(self.widget)
        self.end_dateLabel.setObjectName(u"end_dateLabel")

        self.verticalLayout.addWidget(self.end_dateLabel)

        self.end_dateEdit = QDateEdit(self.widget)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        self.end_dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid; \n"
"border-radius: 6px; \n"
"border-color:rgb(18, 65, 141);\n"
"padding: 8px;\n"
"color: rgb(18, 65, 141);\n"
"font-size:14px;")
        self.end_dateEdit.setLocale(QLocale(QLocale.English, QLocale.Germany))

        self.verticalLayout.addWidget(self.end_dateEdit)

        self.descriptionLabel = QLabel(self.widget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.descriptionInput = QLineEdit(self.widget)
        self.descriptionInput.setObjectName(u"descriptionInput")
        self.descriptionInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.descriptionInput)

        self.kmLabel = QLabel(self.widget)
        self.kmLabel.setObjectName(u"kmLabel")

        self.verticalLayout.addWidget(self.kmLabel)

        self.kmInput = QLineEdit(self.widget)
        self.kmInput.setObjectName(u"kmInput")
        self.kmInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.kmInput)

        self.transportationLabel = QLabel(self.widget)
        self.transportationLabel.setObjectName(u"transportationLabel")

        self.verticalLayout.addWidget(self.transportationLabel)

        self.transportationInput = QComboBox(self.widget)
        self.transportationInput.addItem("")
        self.transportationInput.addItem("")
        self.transportationInput.addItem("")
        self.transportationInput.setObjectName(u"transportationInput")

        self.verticalLayout.addWidget(self.transportationInput)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.activitiesInput = QLineEdit(self.widget)
        self.activitiesInput.setObjectName(u"activitiesInput")

        self.verticalLayout.addWidget(self.activitiesInput)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.hotelContainer = QGridLayout()
        self.hotelContainer.setObjectName(u"hotelContainer")

        self.verticalLayout.addLayout(self.hotelContainer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_Tour_button = QPushButton(self.widget)
        self.add_Tour_button.setObjectName(u"add_Tour_button")
        self.add_Tour_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Tour_button.sizePolicy().hasHeightForWidth())
        self.add_Tour_button.setSizePolicy(sizePolicy)
        self.add_Tour_button.setMinimumSize(QSize(200, 25))
        self.add_Tour_button.setMaximumSize(QSize(200, 16777215))
        self.add_Tour_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_Tour_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.add_Tour_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tours Register", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Tour Register</span></p></body></html>", None))
        self.destinationLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Destination</span></p></body></html>", None))
        self.start_dateLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Start Date</span></p></body></html>", None))
        self.start_dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.end_dateLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">End Date</span></p></body></html>", None))
        self.end_dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Description</span></p></body></html>", None))
        self.kmLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Km</span></p></body></html>", None))
        self.transportationLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Transportation</p></body></html>", None))
        self.transportationInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Bus", None))
        self.transportationInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Ship", None))
        self.transportationInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Airplain", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Activities</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Hotels</span></p></body></html>", None))
        self.add_Tour_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

