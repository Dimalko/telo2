# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeamLeadersRegister.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 889)
        MainWindow.setMinimumSize(QSize(800, 889))
        MainWindow.setMaximumSize(QSize(800, 889))
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(110, 20, 454, 794))
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

        self.SkillsLabel = QLabel(self.widget)
        self.SkillsLabel.setObjectName(u"SkillsLabel")
        self.SkillsLabel.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.SkillsLabel)

        self.SkillsInput = QLineEdit(self.widget)
        self.SkillsInput.setObjectName(u"SkillsInput")
        self.SkillsInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.SkillsInput)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_Team_Leader_button = QPushButton(self.widget)
        self.add_Team_Leader_button.setObjectName(u"add_Team_Leader_button")
        self.add_Team_Leader_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Team_Leader_button.sizePolicy().hasHeightForWidth())
        self.add_Team_Leader_button.setSizePolicy(sizePolicy)
        self.add_Team_Leader_button.setMinimumSize(QSize(200, 25))
        self.add_Team_Leader_button.setMaximumSize(QSize(200, 16777215))
        self.add_Team_Leader_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_Team_Leader_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.add_Team_Leader_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Team Leaders", None))
        self.IdLabel.setText(QCoreApplication.translate("MainWindow", u"Identification number", None))
        self.FirstNameLabel.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.PaymentLabel.setText(QCoreApplication.translate("MainWindow", u"Payment", None))
        self.SkillsLabel.setText(QCoreApplication.translate("MainWindow", u"Skills", None))
        self.add_Team_Leader_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

