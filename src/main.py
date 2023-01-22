import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from src.views.main_window import MainWindow
from src.controllers.utility import absolute_path

if __name__ == "__main__":
    """ Run the application """
    app = QApplication(sys.argv)
    app.setApplicationName('Tony Packer')
    app.setApplicationVersion("1.0.1")

    window = MainWindow()
    window.setWindowIcon(QIcon(absolute_path('images\\logo.png')))
    window.setWindowFlags(Qt.WindowStaysOnTopHint)
    window.setWindowTitle(" ".join([app.applicationName(), app.applicationVersion()]))
    window.showNormal()
    window.setFixedSize(0, 0)

    window.show()
    app.exec_()
