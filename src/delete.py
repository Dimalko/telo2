import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QObject, pyqtSignal

class DeleteWindow(QMainWindow):
    finished = pyqtSignal()
    
    def __init__(self, query=None, labelText=None, user=None):
        super().__init__()
        
        # Load the UI file
        loadUi('ui//delete.ui', self)
        
        #connect to db
        self.conn = sqlite3.connect("data//database.db")
        self.c = self.conn.cursor()
        
        #initializations
        self.user = user
        self.query = query
        self.deleteLbl.setText(labelText)
        
        #connect delete button to a function
        self.deleteBtn.clicked.connect(self.deleteAction)
    
    def input_clear(self):
        self.deleteInput.setText("")
       
    def deleteAction(self):
        try:
            #
            if self.user == None:
                deleteInputText = int(self.deleteInput.text())
            else:
                deleteInputText = self.deleteInput.text()
            #
            
            self.c.execute(self.query, (deleteInputText,))
            
            self.conn.commit()
            
            self.hide()
            self.finished.emit()
            
            self.input_clear()
        except ValueError:
            QMessageBox.warning(self, "Warning","Wrong input.")
        
        
