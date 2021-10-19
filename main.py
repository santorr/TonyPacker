import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Ma fenetre")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("appui bouton gauche")


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()

app.exec_()
