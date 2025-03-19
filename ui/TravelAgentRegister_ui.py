# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TravelAgentRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(564, 812)
        MainWindow.setMinimumSize(QSize(564, 812))
        MainWindow.setMaximumSize(QSize(564, 812))
        MainWindow.setStyleSheet(u"QWidget{\n"
"background-color: rgb(8, 123, 225);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:rgb(243, 249, 254);\n"
"font-size:16px;\n"
"padding-bottom: 0px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(18, 65, 141);\n"
"border: none; \n"
"border-radius: 4px; \n"
"padding: 8px;\n"
"color:rgb(243, 249, 254);\n"
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLabel = QLabel(self.widget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.verticalLayout.addWidget(self.usernameLabel)

        self.usernameInput = QLineEdit(self.widget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.usernameInput)

        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.verticalLayout.addWidget(self.passwordLabel)

        self.passwordInput = QLineEdit(self.widget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.passwordInput)

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

        self.Work_HoursLabel = QLabel(self.widget)
        self.Work_HoursLabel.setObjectName(u"Work_HoursLabel")
        self.Work_HoursLabel.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.Work_HoursLabel)

        self.Work_HoursInput = QLineEdit(self.widget)
        self.Work_HoursInput.setObjectName(u"Work_HoursInput")
        self.Work_HoursInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.Work_HoursInput)

        self.SalaryLabel = QLabel(self.widget)
        self.SalaryLabel.setObjectName(u"SalaryLabel")

        self.verticalLayout.addWidget(self.SalaryLabel)

        self.SalaryInput = QLineEdit(self.widget)
        self.SalaryInput.setObjectName(u"SalaryInput")
        self.SalaryInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.SalaryInput)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_Travel_Agent_button = QPushButton(self.widget)
        self.add_Travel_Agent_button.setObjectName(u"add_Travel_Agent_button")
        self.add_Travel_Agent_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Travel_Agent_button.sizePolicy().hasHeightForWidth())
        self.add_Travel_Agent_button.setSizePolicy(sizePolicy)
        self.add_Travel_Agent_button.setMinimumSize(QSize(200, 25))
        self.add_Travel_Agent_button.setMaximumSize(QSize(200, 16777215))
        self.add_Travel_Agent_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_Travel_Agent_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.add_Travel_Agent_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Travel Agents", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.FirstNameLabel.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.Work_HoursLabel.setText(QCoreApplication.translate("MainWindow", u"Work Hours", None))
        self.SalaryLabel.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.add_Travel_Agent_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

