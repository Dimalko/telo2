# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
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
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(417, 198)
        MainWindow.setMinimumSize(QSize(417, 198))
        MainWindow.setMaximumSize(QSize(417, 198))
        icon = QIcon()
        icon.addFile(u"hospital_clinic_pharmacy_icon_229983.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"font: 57 8pt \"Yu Gothic Medium\";\n"
"background-color: rgb(8, 123, 225);\n"
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
"QLabel{\n"
"color: rgb(243, 249, 254);\n"
"font-size: 24px;\n"
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
"QPushButton:hover{\n"
"background-color: rgb(47, 142, 228);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.deleteLbl = QLabel(self.centralwidget)
        self.deleteLbl.setObjectName(u"deleteLbl")
        self.deleteLbl.setMinimumSize(QSize(0, 20))
        self.deleteLbl.setMaximumSize(QSize(16777215, 25))
        self.deleteLbl.setStyleSheet(u"")

        self.gridLayout.addWidget(self.deleteLbl, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.deleteInput = QLineEdit(self.centralwidget)
        self.deleteInput.setObjectName(u"deleteInput")
        self.deleteInput.setStyleSheet(u"")

        self.gridLayout.addWidget(self.deleteInput, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deleteBtn = QPushButton(self.centralwidget)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setMinimumSize(QSize(0, 25))
        self.deleteBtn.setMaximumSize(QSize(150, 16777215))
        self.deleteBtn.setLayoutDirection(Qt.LeftToRight)
        self.deleteBtn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.deleteBtn)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0394\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03b7", None))
        self.deleteLbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/>.</p></body></html>", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

