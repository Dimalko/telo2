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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 812)
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 30, 581, 711))
        self.widget.setStyleSheet(u"QWidget{\n"
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
        self.LastNameLabel = QLabel(self.widget)
        self.LastNameLabel.setObjectName(u"LastNameLabel")
        self.LastNameLabel.setGeometry(QRect(100, 330, 399, 82))
        self.Work_HoursInput = QLineEdit(self.widget)
        self.Work_HoursInput.setObjectName(u"Work_HoursInput")
        self.Work_HoursInput.setGeometry(QRect(100, 531, 399, 18))
        self.Work_HoursInput.setStyleSheet(u"\n"
"    border: 1px solid #cccccc; /* Border color and width */\n"
"    border-radius: 5px; /* Border radius */")
        self.FirstNameLabel = QLabel(self.widget)
        self.FirstNameLabel.setObjectName(u"FirstNameLabel")
        self.FirstNameLabel.setGeometry(QRect(100, 217, 399, 83))
        self.LastNameInput = QLineEdit(self.widget)
        self.LastNameInput.setObjectName(u"LastNameInput")
        self.LastNameInput.setGeometry(QRect(100, 418, 399, 18))
        self.LastNameInput.setStyleSheet(u"\n"
"    border: 1px solid #cccccc; /* Border color and width */\n"
"    border-radius: 5px; /* Border radius */")
        self.Work_HoursLabel = QLabel(self.widget)
        self.Work_HoursLabel.setObjectName(u"Work_HoursLabel")
        self.Work_HoursLabel.setGeometry(QRect(100, 442, 399, 83))
        self.SalaryLabel = QLabel(self.widget)
        self.SalaryLabel.setObjectName(u"SalaryLabel")
        self.SalaryLabel.setGeometry(QRect(100, 555, 399, 82))
        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(100, 105, 399, 82))
        self.usernameInput = QLineEdit(self.widget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(100, 81, 399, 18))
        self.usernameInput.setStyleSheet(u"\n"
"    border: 1px solid #cccccc; /* Border color and width */\n"
"    border-radius: 5px; /* Border radius */")
        self.SalaryInput = QLineEdit(self.widget)
        self.SalaryInput.setObjectName(u"SalaryInput")
        self.SalaryInput.setGeometry(QRect(100, 643, 399, 18))
        self.SalaryInput.setStyleSheet(u"\n"
"    border: 1px solid #cccccc; /* Border color and width */\n"
"    border-radius: 5px; /* Border radius */")
        self.FirstNameInput = QLineEdit(self.widget)
        self.FirstNameInput.setObjectName(u"FirstNameInput")
        self.FirstNameInput.setGeometry(QRect(100, 306, 399, 18))
        self.FirstNameInput.setStyleSheet(u"\n"
"    border: 1px solid #cccccc; /* Border color and width */\n"
"    border-radius: 5px; /* Border radius */")
        self.usernameLabel = QLabel(self.widget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(100, -8, 399, 83))
        self.passwordInput = QLineEdit(self.widget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(100, 193, 399, 18))
        self.passwordInput.setStyleSheet(u"\n"
"    border: 1px solid #cccccc; /* Border color and width */\n"
"    border-radius: 5px; /* Border radius */")
        self.add_Travel_Agent_button = QPushButton(self.centralwidget)
        self.add_Travel_Agent_button.setObjectName(u"add_Travel_Agent_button")
        self.add_Travel_Agent_button.setEnabled(True)
        self.add_Travel_Agent_button.setGeometry(QRect(360, 750, 101, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Travel_Agent_button.sizePolicy().hasHeightForWidth())
        self.add_Travel_Agent_button.setSizePolicy(sizePolicy)
        self.add_Travel_Agent_button.setMinimumSize(QSize(0, 25))
        self.add_Travel_Agent_button.setCursor(QCursor(Qt.PointingHandCursor))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Travel Agents", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.FirstNameLabel.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.Work_HoursLabel.setText(QCoreApplication.translate("MainWindow", u"Work Hours", None))
        self.SalaryLabel.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.add_Travel_Agent_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

