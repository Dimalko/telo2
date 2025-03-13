from PySide6.QtGui import QPixmap

def set_image(label, image_path):
    """Sets an image on a QLabel."""
    pixmap = QPixmap(image_path)
    label.setPixmap(pixmap)
    label.setScaledContents(True)  # Allow resizing to fit the label
