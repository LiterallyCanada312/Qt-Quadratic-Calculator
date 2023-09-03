import sys
import mathStuff

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QLineEdit)
from PyQt6.QtGui import (QDoubleValidator)

class mainPage:

    def __init__ (self):
        QWidget.__init__(self)

        aInput = QLineEdit()
        aInput.setValidator(QDoubleValidator())

        bInput = QLineEdit()
        bInput.setValidator(QDoubleValidator())

        cInput = QLineEdit()
        cInput.setValidator(QDoubleValidator())
        

        form = QVBoxLayout()
        form.addItem(aInput)
        form.addItem(bInput)
        form.addItem(cInput)

        self.setLayout(form)
        self.setWindowTitle("Homework Helper")

    @Slot()
    def quadraticPressed(self):
        mathStuff.doQuadratic()


if __name__ == 'main':
    app = QApplication(sys.argv)
    window = mainPage()
    window.show()
    sys.exit(app.exec())
