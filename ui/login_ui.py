# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"QWidget{\n"
"font: 57 8pt \"Yu Gothic Medium\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(8, 123, 225);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(243, 249, 254);\n"
"font-size: 24px;")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel{\n"
"color:rgb(243, 249, 254);\n"
"font-size:16px;\n"
"padding-bottom: 0px;\n"
"}")
        self.label.setScaledContents(False)

        self.verticalLayout.addWidget(self.label)

        self.usernameInput = QLineEdit(self.widget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setStyleSheet(u"background-color: rgb(18, 65, 141);\n"
"border: none; \n"
"border-radius: 4px; \n"
"padding: 8px;\n"
"color:rgb(243, 249, 254);\n"
"font-size:14px;")

        self.verticalLayout.addWidget(self.usernameInput)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_5)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"color:rgb(243, 249, 254);\n"
"font-size:16px;\n"
"padding:0px;")
        self.label_2.setMargin(0)
        self.label_2.setIndent(-1)

        self.verticalLayout.addWidget(self.label_2)

        self.passwordInput = QLineEdit(self.widget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setStyleSheet(u"background-color: rgb(18, 65, 141);\n"
"border: none; \n"
"border-radius: 4px; \n"
"padding: 8px;\n"
"color:rgb(243, 249, 254);\n"
"font-size:14px;")
        self.passwordInput.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordInput)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.roleInput = QComboBox(self.widget)
        self.roleInput.addItem("")
        self.roleInput.addItem("")
        self.roleInput.setObjectName(u"roleInput")
        self.roleInput.setStyleSheet(u"background-color: rgb(18, 65, 141);\n"
"border: none; \n"
"border-radius: 4px; \n"
"padding: 8px;\n"
"color:rgb(243, 249, 254);\n"
"font-size: 14px;")

        self.verticalLayout.addWidget(self.roleInput)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.loginBtn = QPushButton(self.widget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(200, 0))
        self.loginBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.loginBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.invInpLbl = QLabel(self.widget)
        self.invInpLbl.setObjectName(u"invInpLbl")
        self.invInpLbl.setStyleSheet(u"color:rgb(243, 249, 254);\n"
"font-size:14px;\n"
"padding:0px;")

        self.verticalLayout.addWidget(self.invInpLbl)

        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imgLabel = QLabel(self.widget_2)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imgLabel.sizePolicy().hasHeightForWidth())
        self.imgLabel.setSizePolicy(sizePolicy2)
        self.imgLabel.setMinimumSize(QSize(0, 0))
        self.imgLabel.setSizeIncrement(QSize(4, 4))
        self.imgLabel.setPixmap(QPixmap(u"Adobe_Express_-_file.jpg"))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setAlignment(Qt.AlignCenter)
        self.imgLabel.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.imgLabel)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Welcome</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_5.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.roleInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.roleInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Travel_Agent", None))

        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.invInpLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">\u26a0\ufe0f Invalid username os password</span></p></body></html>", None))
        self.imgLabel.setText("")
    # retranslateUi

