#!/usr/bin/env python

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import urllib.request

class PyDownloader(QDialog) :
    def __init__(self) :
        super().__init__()
        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save = QLineEdit()
        self.prog = QProgressBar()
        self.dwl = QPushButton("Download")
        self.browse = QPushButton("Browse")

        self.url.setPlaceholderText("URL")
        self.save.setPlaceholderText("Save Location")
        self.prog.setValue(0)
        self.prog.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save)
        layout.addWidget(self.browse)
        layout.addWidget(self.prog)
        layout.addWidget(self.dwl)

        self.dwl.clicked.connect(self.download)
        self.browse.clicked.connect(self.browse_file)

        self.setWindowTitle("Py Downloader")
        self.setLayout(layout)
        self.setFocus()

    def download(self) :
        url = self.url.text()
        sav = self.save.text()
        try :
            urllib.request.urlretrieve(url, sav, self.report)
            QMessageBox.information(self, "Information", "The download is complete")
        except Exception as e:
            QMessageBox.warning(self, "Warning", "The download failed")

        finally :
            self.url.setText("")
            self.save.setText("")
            self.prog.setValue(0)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".", filter="All Files (*.*)")
        self.save.setText(QDir.toNativeSeparators(save_file[0]))

    def report(self, blocknum, blocksize, totalsize) :
        readsofar = blocknum*blocksize
        if totalsize > 0 :
            perc = readsofar*100/totalsize
            self.prog.setValue(int(perc))


app = QApplication(sys.argv)
d = PyDownloader()
d.show()
sys.exit(app.exec_())
