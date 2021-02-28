#!/usr/bin/env python

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class HelloWorld(QDialog) :
    def __init__(self) :
        super().__init__()
        #layout = QVBoxLayout()
        #layout = QHBoxLayout()
        layout = QGridLayout()
        self.label = QLabel("Hello World")
        line_edit = QLineEdit()
        button = QPushButton("Close")
        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.changeText)

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setWindowTitle("Hello Qt World")
        self.setLayout(layout)

    def changeText(self, txt) :
        #self.label.setText(txt)
        print (f"User typed {txt}")


app = QApplication(sys.argv)
d = HelloWorld()
d.show()
sys.exit(app.exec_())
