import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from admin import AdminWindow
from agent import AgentWindow

"""
    Login window for system users.
    Allows Admin and Agent users to log in using username, password and role.
    """
class LoginWindow(QMainWindow):

    switch_admin = pyqtSignal()
    switch_agent = pyqtSignal()
    """
        Initializes the login window.
        Loads the UI, connects to the database and sets up interface elements.
        """   
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
    
    """
        Processes the user login procedure.
        Checks login credentials against the database and opens the appropriate window
        based on the user's role (Admin or Agent).
        """
    def login(self):
        #retreive entered inputs
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        role = self.roleInput.currentText()
        
        self.cursor.execute("SELECT username,password,role FROM Staff WHERE username=? AND password=? AND role=?", (username, password, role))
        result = self.cursor.fetchone()
        
        if result:
            if role == "Admin":
                self.switch_admin.emit()
                self.admin = AdminWindow()
                self.admin.show()
                self.hide()
            else:
                self.switch_agent.emit()
                self.agent = AgentWindow(username)
                self.agent.show()
                self.hide()
        else:
            self.invInpLbl.show()

        """
        Loads and displays the login image on the corresponding label.
        Uses the image file from the data/images folder.
        """
    def loginImg(self):
        pixmap = QPixmap("data//images//login_img.jpg")
        self.imgLabel.setPixmap(pixmap)

    """
    Main entry point of the application.
    Creates the PyQt5 application and displays the login window.
    """    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())