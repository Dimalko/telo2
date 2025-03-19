import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from admin import AdminWindow
#from supplier import SupplierWindow


class LoginWindow(QMainWindow):
    
    switch_admin = pyqtSignal()
    #switch_supplier = Signal()
    
    def __init__(self):
        super().__init__()    
        
        # Load the UI file
        loadUi('ui//login.ui', self)

        #load images
        self.loginImg()
        
        #connect db file
        self.connection = sqlite3.connect("data/database.db")
        self.cursor = self.connection.cursor()      
        
        #connect login btn to a function
        self.loginBtn.clicked.connect(self.login)
        
        #hide the invalid input message
        self.invInpLbl.hide()
    
    
    def login(self):
        #retreive entered inputs
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        role = self.roleInput.currentText()
        print(role)
        
        self.cursor.execute("SELECT username,password,role FROM Staff WHERE username=? AND password=? AND role=?", (username, password, role))
        result = self.cursor.fetchone()
        
        if result:
            print("connect success")
            if role == "Admin":
                self.switch_admin.emit()
                self.admin = AdminWindow()
                self.admin.show()
                self.hide()
        #     else:
        #         self.switch_supplier.emit()
        #         self.supplier = SupplierWindow(username)
        #         self.supplier.show()
        #         self.hide()
        # else:
        #     self.invInpLbl.show()
        #     print("invalid input")


    def loginImg(self):
        pixmap = QPixmap("data//images//login_img.jpg")
        self.imgLabel.setPixmap(pixmap)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())