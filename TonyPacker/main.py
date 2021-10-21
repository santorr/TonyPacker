import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("appui bouton gauche")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Tony Paker")
    window.showMaximized()
    window.show()
    app.exec_()
