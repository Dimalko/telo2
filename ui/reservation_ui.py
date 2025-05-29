# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(874, 710)
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
"}\n"
"QListWidget {\n"
"    background-color: white;\n"
"    border: 2px solid rgb(18, 65, 141);\n"
"    border-radius: 6px;\n"
"    alternate-background-color: #f0f0f0;\n"
"    padding: 2px;\n"
"    font-size: 14px;\n"
"    color: rgb(18, 65, 141);\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QListWidget::item:selec"
                        "ted {\n"
"    background-color: rgb(18, 65, 141);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"QTableWidget {\n"
"border:none;\n"
"background-color: white; \n"
"alternate-background-color: #f0f0f0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(18, 65, 141);            \n"
"	color: rgb(243, 249, 254);\n"
"    font: 57 8pt \"Yu Gothic Medium\";\n"
"    padding: 5px;\n"
"    border: 1px solid rgb(24, 89, 193); \n"
"}\n"
"\n"
"#QTableWidget QTableCornerButton::section {\n"
"    background-color: #74b9ff; /* Top-left corner color */\n"
"    border: 1px solid #0984e3;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #dfe6e9;  /* Background color of the scrollbar track */\n"
"    height: 12px;  /* Thickness of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0984e3; /* Color of the scrollbar handle (slider) */\n"
"    min-width: 20px; /* Minimum width of the"
                        " handle */\n"
"    border-radius: 6px; /* Rounded edges */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #74b9ff; /* Lighter color when hovered */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none; /* Removes the small arrow buttons */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none; /* Keeps empty space color same */\n"
"}\n"
"\n"
"QListWidget{\n"
"	border: 1px solid rgb(161, 161, 161);	\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid rgb(18, 65, 141);	\n"
"	border-radius: 9px;\n"
"}\n"
"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QWidget{\n"
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
"}\n"
"QListWidget {\n"
"    background-color: white;\n"
"    border: 2px solid rgb(18, 65, 141);\n"
"    border-radius: 6px;\n"
"    alternate-background-color: #f0f0f0;\n"
"    padding: 2px;\n"
"    font-size: 14px;\n"
"    color: rgb(18, 65, 141);\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QListWidget::item:selec"
                        "ted {\n"
"    background-color: rgb(18, 65, 141);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTabBar{\n"
"border:none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"        background: rgb(220, 228, 231);\n"
"        \n"
"       \n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"        background: #087be1;\n"
"        color: white; \n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"        background: #2f8ee4;\n"
"		color: white; \n"
"}\n"
"")
        self.reservationTab = QWidget()
        self.reservationTab.setObjectName(u"reservationTab")
        self.reservationTab.setStyleSheet(u"QWidget{\n"
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
"}\n"
"QListWidget {\n"
"    background-color: white;\n"
"    border: 2px solid rgb(18, 65, 141);\n"
"    border-radius: 6px;\n"
"    alternate-background-color: #f0f0f0;\n"
"    padding: 2px;\n"
"    font-size: 14px;\n"
"    color: rgb(18, 65, 141);\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QListWidget::item:selec"
                        "ted {\n"
"    background-color: rgb(18, 65, 141);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.reservationTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Tourslabel = QLabel(self.reservationTab)
        self.Tourslabel.setObjectName(u"Tourslabel")

        self.verticalLayout_2.addWidget(self.Tourslabel)

        self.Tour_listWidget = QListWidget(self.reservationTab)
        self.Tour_listWidget.setObjectName(u"Tour_listWidget")

        self.verticalLayout_2.addWidget(self.Tour_listWidget)

        self.TourslineEdit = QLineEdit(self.reservationTab)
        self.TourslineEdit.setObjectName(u"TourslineEdit")

        self.verticalLayout_2.addWidget(self.TourslineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Clientlabel = QLabel(self.reservationTab)
        self.Clientlabel.setObjectName(u"Clientlabel")

        self.verticalLayout.addWidget(self.Clientlabel)

        self.Client_listWidget = QListWidget(self.reservationTab)
        self.Client_listWidget.setObjectName(u"Client_listWidget")
        self.Client_listWidget.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.Client_listWidget)

        self.ClientlineEdit = QLineEdit(self.reservationTab)
        self.ClientlineEdit.setObjectName(u"ClientlineEdit")

        self.verticalLayout.addWidget(self.ClientlineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.reservationTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.peopleSpinBox = QSpinBox(self.reservationTab)
        self.peopleSpinBox.setObjectName(u"peopleSpinBox")
        self.peopleSpinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.peopleSpinBox)

        self.label_4 = QLabel(self.reservationTab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.Hotels_comboBox = QComboBox(self.reservationTab)
        self.Hotels_comboBox.setObjectName(u"Hotels_comboBox")
        self.Hotels_comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.Hotels_comboBox)

        self.label_5 = QLabel(self.reservationTab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.paymentComboBox = QComboBox(self.reservationTab)
        self.paymentComboBox.addItem("")
        self.paymentComboBox.addItem("")
        self.paymentComboBox.setObjectName(u"paymentComboBox")
        self.paymentComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.paymentComboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.add_reservation_pushButton = QPushButton(self.reservationTab)
        self.add_reservation_pushButton.setObjectName(u"add_reservation_pushButton")

        self.verticalLayout_6.addWidget(self.add_reservation_pushButton)

        self.tabWidget.addTab(self.reservationTab, "")
        self.clientsTab = QWidget()
        self.clientsTab.setObjectName(u"clientsTab")
        self.horizontalLayout = QHBoxLayout(self.clientsTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget = QWidget(self.clientsTab)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.FirstNameInput = QLineEdit(self.widget)
        self.FirstNameInput.setObjectName(u"FirstNameInput")
        self.FirstNameInput.setStyleSheet(u"")

        self.gridLayout.addWidget(self.FirstNameInput, 4, 0, 1, 1)

        self.PhoneNumberLabel = QLabel(self.widget)
        self.PhoneNumberLabel.setObjectName(u"PhoneNumberLabel")

        self.gridLayout.addWidget(self.PhoneNumberLabel, 1, 0, 1, 1)

        self.EmailInput = QLineEdit(self.widget)
        self.EmailInput.setObjectName(u"EmailInput")
        self.EmailInput.setStyleSheet(u"")

        self.gridLayout.addWidget(self.EmailInput, 8, 0, 1, 1)

        self.LastNameInput = QLineEdit(self.widget)
        self.LastNameInput.setObjectName(u"LastNameInput")
        self.LastNameInput.setStyleSheet(u"")

        self.gridLayout.addWidget(self.LastNameInput, 6, 0, 1, 1)

        self.PhoneNumberInput = QLineEdit(self.widget)
        self.PhoneNumberInput.setObjectName(u"PhoneNumberInput")
        self.PhoneNumberInput.setStyleSheet(u"")

        self.gridLayout.addWidget(self.PhoneNumberInput, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.LastNameLabel = QLabel(self.widget)
        self.LastNameLabel.setObjectName(u"LastNameLabel")

        self.gridLayout.addWidget(self.LastNameLabel, 5, 0, 1, 1)

        self.labelWidget = QWidget(self.widget)
        self.labelWidget.setObjectName(u"labelWidget")
        self.labelWidget.setStyleSheet(u"background-color: rgb(18, 65, 141);")
        self.horizontalLayout_3 = QHBoxLayout(self.labelWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.client_label = QLabel(self.labelWidget)
        self.client_label.setObjectName(u"client_label")
        self.client_label.setStyleSheet(u"color: rgb(243, 249, 254);")

        self.horizontalLayout_3.addWidget(self.client_label)


        self.gridLayout.addWidget(self.labelWidget, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.add_Client_button = QPushButton(self.widget)
        self.add_Client_button.setObjectName(u"add_Client_button")
        self.add_Client_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_Client_button.sizePolicy().hasHeightForWidth())
        self.add_Client_button.setSizePolicy(sizePolicy)
        self.add_Client_button.setMinimumSize(QSize(200, 25))
        self.add_Client_button.setMaximumSize(QSize(200, 16777215))
        self.add_Client_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_Client_button.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.add_Client_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_4, 10, 0, 1, 1)

        self.FirstNameLabel = QLabel(self.widget)
        self.FirstNameLabel.setObjectName(u"FirstNameLabel")

        self.gridLayout.addWidget(self.FirstNameLabel, 3, 0, 1, 1)

        self.EmailLabel = QLabel(self.widget)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setStyleSheet(u"")

        self.gridLayout.addWidget(self.EmailLabel, 7, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.tabWidget.addTab(self.clientsTab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"QWidget{\n"
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
"}\n"
"QListWidget {\n"
"    background-color: white;\n"
"    border: 2px solid rgb(18, 65, 141);\n"
"    border-radius: 6px;\n"
"    alternate-background-color: #f0f0f0;\n"
"    padding: 2px;\n"
"    font-size: 14px;\n"
"    color: rgb(18, 65, 141);\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QListWidget::item:selec"
                        "ted {\n"
"    background-color: rgb(18, 65, 141);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.verticalLayout1 = QVBoxLayout(self.tab_3)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.group_selection_layout = QHBoxLayout()
        self.group_selection_layout.setObjectName(u"group_selection_layout")
        self.group_label = QLabel(self.tab_3)
        self.group_label.setObjectName(u"group_label")
        self.group_label.setStyleSheet(u"QLabel {\n"
"    color: #12418d;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"	background-color:rgb(170, 217, 231);\n"
"}\n"
"")

        self.group_selection_layout.addWidget(self.group_label)

        self.groupComboBox = QComboBox(self.tab_3)
        self.groupComboBox.setObjectName(u"groupComboBox")
        self.groupComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.group_selection_layout.addWidget(self.groupComboBox)


        self.verticalLayout1.addLayout(self.group_selection_layout)

        self.groupPaymentsTable = QTableWidget(self.tab_3)
        if (self.groupPaymentsTable.columnCount() < 5):
            self.groupPaymentsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.groupPaymentsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.groupPaymentsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.groupPaymentsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.groupPaymentsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.groupPaymentsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.groupPaymentsTable.setObjectName(u"groupPaymentsTable")
        self.groupPaymentsTable.setStyleSheet(u"QWidget{\n"
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
"}\n"
"\n"
"")

        self.verticalLayout1.addWidget(self.groupPaymentsTable)

        self.paymentFormLayout = QFormLayout()
        self.paymentFormLayout.setObjectName(u"paymentFormLayout")
        self.labelDate = QLabel(self.tab_3)
        self.labelDate.setObjectName(u"labelDate")

        self.paymentFormLayout.setWidget(0, QFormLayout.LabelRole, self.labelDate)

        self.paymentDateEdit = QDateEdit(self.tab_3)
        self.paymentDateEdit.setObjectName(u"paymentDateEdit")
        self.paymentDateEdit.setStyleSheet(u"QDateEdit {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}")
        self.paymentDateEdit.setCalendarPopup(True)

        self.paymentFormLayout.setWidget(0, QFormLayout.FieldRole, self.paymentDateEdit)

        self.labelType = QLabel(self.tab_3)
        self.labelType.setObjectName(u"labelType")

        self.paymentFormLayout.setWidget(1, QFormLayout.LabelRole, self.labelType)

        self.paymentTypeComboBox = QComboBox(self.tab_3)
        self.paymentTypeComboBox.addItem("")
        self.paymentTypeComboBox.addItem("")
        self.paymentTypeComboBox.addItem("")
        self.paymentTypeComboBox.setObjectName(u"paymentTypeComboBox")
        self.paymentTypeComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")

        self.paymentFormLayout.setWidget(1, QFormLayout.FieldRole, self.paymentTypeComboBox)

        self.labelAmount = QLabel(self.tab_3)
        self.labelAmount.setObjectName(u"labelAmount")

        self.paymentFormLayout.setWidget(2, QFormLayout.LabelRole, self.labelAmount)

        self.paymentAmountSpinBox = QDoubleSpinBox(self.tab_3)
        self.paymentAmountSpinBox.setObjectName(u"paymentAmountSpinBox")
        self.paymentAmountSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: white;\n"
"    border: 2px solid #12418d;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #12418d;\n"
"}\n"
"\n"
"QDoubleSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #12418d;\n"
"}\n"
"\n"
"\n"
"")
        self.paymentAmountSpinBox.setDecimals(2)
        self.paymentAmountSpinBox.setMaximum(10000.000000000000000)

        self.paymentFormLayout.setWidget(2, QFormLayout.FieldRole, self.paymentAmountSpinBox)


        self.verticalLayout1.addLayout(self.paymentFormLayout)

        self.horizontalPaymentButtons = QHBoxLayout()
        self.horizontalPaymentButtons.setObjectName(u"horizontalPaymentButtons")
        self.addPaymentButton = QPushButton(self.tab_3)
        self.addPaymentButton.setObjectName(u"addPaymentButton")
        self.addPaymentButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalPaymentButtons.addWidget(self.addPaymentButton)

        self.deletePaymentButton = QPushButton(self.tab_3)
        self.deletePaymentButton.setObjectName(u"deletePaymentButton")

        self.horizontalPaymentButtons.addWidget(self.deletePaymentButton)

        self.editPaymentButton = QPushButton(self.tab_3)
        self.editPaymentButton.setObjectName(u"editPaymentButton")
        self.editPaymentButton.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 0px;\n"
"font-size: 14px;\n"
"padding: 5px;\n"
"background-color:rgb(234, 129, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(240, 168, 0);\n"
"}")

        self.horizontalPaymentButtons.addWidget(self.editPaymentButton)


        self.verticalLayout1.addLayout(self.horizontalPaymentButtons)

        self.paymentStatusLabel = QLabel(self.tab_3)
        self.paymentStatusLabel.setObjectName(u"paymentStatusLabel")
        self.paymentStatusLabel.setStyleSheet(u"font-weight: bold; \n"
"padding-top: 10px;\n"
"background-color:rgb(170, 217, 231);;\n"
"border-radius: 7px;")

        self.verticalLayout1.addWidget(self.paymentStatusLabel)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reservation Window", None))
        self.Tourslabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Tours</p></body></html>", None))
        self.Clientlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">client</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"number of people", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"hotel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"payment type", None))
        self.paymentComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"card", None))
        self.paymentComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"cash", None))

        self.add_reservation_pushButton.setText(QCoreApplication.translate("MainWindow", u"Make Reservation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reservationTab), QCoreApplication.translate("MainWindow", u"Reservation", None))
        self.PhoneNumberLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Phone Number</span></p></body></html>", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Last name</span></p></body></html>", None))
        self.client_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Clients Register</span></p></body></html>", None))
        self.add_Client_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.FirstNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">First Name</span></p></body></html>", None))
        self.EmailLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Email</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clientsTab), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.group_label.setText(QCoreApplication.translate("MainWindow", u"Choose Reservation/ Group:", None))
        ___qtablewidgetitem = self.groupPaymentsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.groupPaymentsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"group_id", None));
        ___qtablewidgetitem2 = self.groupPaymentsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"amount", None));
        ___qtablewidgetitem3 = self.groupPaymentsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"payment_date", None));
        ___qtablewidgetitem4 = self.groupPaymentsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"type", None));
        self.labelDate.setText(QCoreApplication.translate("MainWindow", u"Date of Payment", None))
        self.labelType.setText(QCoreApplication.translate("MainWindow", u"Type of Payment", None))
        self.paymentTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Prepayment", None))
        self.paymentTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0399nstallment", None))
        self.paymentTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Final Payment", None))

        self.labelAmount.setText(QCoreApplication.translate("MainWindow", u"Amount Payed", None))
        self.paymentAmountSpinBox.setPrefix(QCoreApplication.translate("MainWindow", u"\u20ac ", None))
        self.addPaymentButton.setText(QCoreApplication.translate("MainWindow", u"Add Payment", None))
        self.deletePaymentButton.setText(QCoreApplication.translate("MainWindow", u"Delete Payment", None))
        self.editPaymentButton.setText(QCoreApplication.translate("MainWindow", u"Edit Payment", None))
        self.paymentStatusLabel.setText(QCoreApplication.translate("MainWindow", u"\u039a\u03b1\u03c4\u03b1\u03b2\u03bb\u03b7\u03b8\u03ad\u03bd: 0 / 0 \u20ac | \u039a\u03b1\u03c4\u03ac\u03c3\u03c4\u03b1\u03c3\u03b7: Unpaid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Group Payments", None))
    # retranslateUi

