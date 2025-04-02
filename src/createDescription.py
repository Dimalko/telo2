import sys
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic import loadUi



class CreateTourDescriptionWindow(QMainWindow):
    finished = pyqtSignal()
    
    
    def __init__(self,):
        super().__init__()

        loadUi('ui/createTourDescription.ui', self)

        self.connection = sqlite3.connect("data//database.db")
        self.cursor = self.connection.cursor()

        self.saveDBtn.clicked.connect(self.saveDescription)
        self.addImgDBtn.clicked.connect(self.getImage)

        self.imagePath = ""


    def input_clear(self):
        self.tourIdDInput.setText("")
        self.startingPriceDInput.setText("")


    def saveDescription(self):
        try:
            tourDescId = self.tourIdDInput.text()
            price = self.startingPriceDInput.text()
            
            self.cursor.execute("SELECT start_date, end_date, destination FROM Tours WHERE id = ?", (tourDescId,))
            result = self.cursor.fetchone()
            
            if not result:
                QMessageBox.warning(self, "Error", "Tour ID not found")
                return
            
            s_date, e_date, location = result
            
            background_image = f"file:///{self.image_path.replace('\\', '/')}"
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Tour Description</title>
                <style>
                    html, body{{
                        height: 100%;
                        margin: 0 auto;
                        font-family: 'Brush Script MT', cursive;
                    }}
                    .main-container{{
                        height: 100%;
                        background-image: url('{background_image}');
                        background-size: cover;
                        background-position: center;
                        background-color: rgb(0, 174, 255);
                        color: white;
                        text-align: center;
                        text-shadow: 0px 0px 5px aqua;
                    }}
                    .title{{
                        font-size: 72px;
                        background-color: rgba(0,0,0,0.2);
                        padding: 20px;
                    }}
                    .information{{
                        display: flex;
                        justify-content: space-around;
                        width: 100%;
                        font-size: 42px;
                        position: fixed;
                        bottom: 20%;
                    }}
                    .dates, .price{{
                        padding: 20px;
                        border-radius: 10px;
                        background-color: rgba(0,0,0,0.2);
                    }}
                </style>
            </head>
            <body>
                <div class="main-container">
                    <div class="title">{location} !!!</div>
                    <div class="information">
                        <div class="dates">
                            <div>Starting date:</div>
                            <div>{s_date}</div>
                            <div>End date:</div>
                            <div>{e_date}</div>
                        </div>
                        <div class="price">{price}€</div>
                    </div>
                </div>
            </body>
            </html>
            """
            
            save_path, _ = QFileDialog.getSaveFileName(self, "Save HTML File", "", "HTML Files (*.html);;All Files (*)")
            
            if save_path:
                with open(save_path, "w", encoding="utf-8") as file:
                    file.write(html_content)
                QMessageBox.information(self, "Success", "HTML file saved successfully")
                self.finished.emit()
                self.input_clear()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Could not create description")
            self.input_clear()
            self.connection.rollback()
        finally:
            self.connection.close()
            self.finished.emit()
            self.close()    
    
    def getImage(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        
        if file_path:
            self.image_path = file_path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateTourDescriptionWindow()
    window.show()
    sys.exit(app.exec_())
