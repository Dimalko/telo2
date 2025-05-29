# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DriversRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
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
        self.IdLabel = QLabel(self.widget)
        self.IdLabel.setObjectName(u"IdLabel")

        self.verticalLayout.addWidget(self.IdLabel)

        self.IdInput = QLineEdit(self.widget)
        self.IdInput.setObjectName(u"IdInput")
        self.IdInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.IdInput)

        self.FirstNameLabel = QLabel(self.widget)
        self.FirstNameLabel.setObjectName(u"FirstNameLabel")

        self.verticalLayout.addWidget(self.FirstNameLabel)

        self.FirstNameInput = QLineEdit(self.widget)
        self.FirstNameInput.setObjectName(u"FirstNameInput")
        self.FirstNameInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.FirstNameInput)

        self.LastNameLabel = QLabel(self.widget)
        self.LastNameLabel.setObjectName(u"LastNameLabel")

        self.verticalLayout.addWidget(self.LastNameLabel)

        self.LastNameInput = QLineEdit(self.widget)
        self.LastNameInput.setObjectName(u"LastNameInput")
        self.LastNameInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.LastNameInput)

        self.PaymentLabel = QLabel(self.widget)
        self.PaymentLabel.setObjectName(u"PaymentLabel")

        self.verticalLayout.addWidget(self.PaymentLabel)

        self.PaymentInput = QLineEdit(self.widget)
        self.PaymentInput.setObjectName(u"PaymentInput")
        self.PaymentInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.PaymentInput)

        self.TypeLabel = QLabel(self.widget)
        self.TypeLabel.setObjectName(u"TypeLabel")
        self.TypeLabel.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.TypeLabel)

        self.TypeComboBox = QComboBox(self.widget)
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.setObjectName(u"TypeComboBox")
        self.TypeComboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid; \n"
"border-radius: 6px; \n"
"border-color:rgb(18, 65, 141);\n"
"padding: 8px;\n"
"color: rgb(18, 65, 141);\n"
"font-size:14px;")

        self.verticalLayout.addWidget(self.TypeComboBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_Driver_button = QPushButton(self.widget)
        self.add_Driver_button.setObjectName(u"add_Driver_button")
        self.add_Driver_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Driver_button.sizePolicy().hasHeightForWidth())
        self.add_Driver_button.setSizePolicy(sizePolicy)
        self.add_Driver_button.setMinimumSize(QSize(200, 25))
        self.add_Driver_button.setMaximumSize(QSize(200, 16777215))
        self.add_Driver_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_Driver_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.add_Driver_button)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Drivers Register", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Register</span></p></body></html>", None))
        self.IdLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Identification Number</span></p></body></html>", None))
        self.FirstNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">First Name</span></p></body></html>", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Last name</span></p></body></html>", None))
        self.PaymentLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Payment</span></p></body></html>", None))
        self.TypeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Type</p></body></html>", None))
        self.TypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Permanent", None))
        self.TypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Freelancer", None))

        self.add_Driver_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

