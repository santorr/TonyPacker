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
    """ Run the application """
    app = QApplication(sys.argv)
    app.setApplicationName('Tony Parker')
    app.setApplicationVersion("0.0.1")
    """ Create the main window """
    window = MainWindow()
    window.setWindowTitle(" ".join([app.applicationName(), app.applicationVersion()]))
    window.showMaximized()
    window.show()
    app.exec_()
