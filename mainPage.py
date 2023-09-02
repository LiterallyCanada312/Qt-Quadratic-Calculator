import sys
import mathStuff

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)

class mainPage:

    def __init__ (self):
        QWidget.__init__(self)


    @Slot()
    def quadraticPressed(self):
        mathStuff.doQuadratic()


    