# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createTourDescription.ui'
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
        MainWindow.resize(459, 477)
        MainWindow.setMinimumSize(QSize(459, 477))
        MainWindow.setMaximumSize(QSize(459, 477))
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
"text-align: center;\n"
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelWidget = QWidget(self.centralwidget)
        self.labelWidget.setObjectName(u"labelWidget")
        self.labelWidget.setStyleSheet(u"background-color: rgb(18, 65, 141);")
        self.horizontalLayout_2 = QHBoxLayout(self.labelWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.labelWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(243, 249, 254);")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.labelWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tourDLabel = QLabel(self.widget)
        self.tourDLabel.setObjectName(u"tourDLabel")

        self.verticalLayout.addWidget(self.tourDLabel)

        self.tourIdDInput = QLineEdit(self.widget)
        self.tourIdDInput.setObjectName(u"tourIdDInput")
        self.tourIdDInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.tourIdDInput)

        self.startingPriceDLabel = QLabel(self.widget)
        self.startingPriceDLabel.setObjectName(u"startingPriceDLabel")

        self.verticalLayout.addWidget(self.startingPriceDLabel)

        self.startingPriceDInput = QLineEdit(self.widget)
        self.startingPriceDInput.setObjectName(u"startingPriceDInput")
        self.startingPriceDInput.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.startingPriceDInput)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.addImgDBtn = QPushButton(self.widget)
        self.addImgDBtn.setObjectName(u"addImgDBtn")
        self.addImgDBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.addImgDBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.saveDBtn = QPushButton(self.widget)
        self.saveDBtn.setObjectName(u"saveDBtn")
        self.saveDBtn.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveDBtn.sizePolicy().hasHeightForWidth())
        self.saveDBtn.setSizePolicy(sizePolicy)
        self.saveDBtn.setMinimumSize(QSize(0, 0))
        self.saveDBtn.setMaximumSize(QSize(200, 16777215))
        self.saveDBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveDBtn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.saveDBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalLayout.setStretch(0, 25)
        self.horizontalLayout.setStretch(1, 25)
        self.horizontalLayout.setStretch(2, 25)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tour Description", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Tour Description</span></p></body></html>", None))
        self.tourDLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Tour Id</span></p></body></html>", None))
        self.startingPriceDLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Starting Price</span></p></body></html>", None))
        self.addImgDBtn.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.saveDBtn.setText(QCoreApplication.translate("MainWindow", u"Save As..", None))
    # retranslateUi

