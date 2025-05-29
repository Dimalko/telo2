import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QObject, pyqtSignal
"""
    Window for deleting records from the database.
    Provides a user interface to confirm and perform deletion actions,
    based on a provided SQL query and user input.
"""
class DeleteWindow(QMainWindow):
    finished = pyqtSignal()
    """
        Initializes the delete window.
        Loads the UI, connects to the database, enables foreign key constraints,
        and sets up the event handler for the delete button.
        
        :param query: SQL delete query to be executed
        :param labelText: Text to be displayed as a prompt label
        :param user: Optional flag to determine input type (str or int)
    """   
    def __init__(self, query=None, labelText=None, user=None):
        super().__init__()
        
        # Load the UI file
        loadUi('ui//delete.ui', self)
        
        #connect to db
        self.conn = sqlite3.connect("data//database.db")
        self.c = self.conn.cursor()
        #enable foreign keys
        self.c.execute("PRAGMA foreign_keys = ON;")
        
        #initializations
        self.user = user
        self.query = query
        self.deleteLbl.setText(labelText)
        
        #connect delete button to a function
        self.deleteBtn.clicked.connect(self.deleteAction)
    """
        Clears the input field of the delete form.
        Resets the field after a deletion attempt.
    """
    def input_clear(self):
        self.deleteInput.setText("")
    """
        Executes the deletion action based on user input.
        Converts input to the appropriate type depending on context (int or str),
        runs the SQL query with the input as parameter, commits the change to the database,
        hides the window, emits a finished signal, and clears the input field.
        Displays a warning message in case of invalid input.
    """  
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
        
        
