import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from src.views.main_window import MainWindow

if __name__ == "__main__":
    """ Run the application """
    app = QApplication(sys.argv)
    app.setApplicationName('Tony Packer')
    app.setApplicationVersion("0.0.1")
    """ Create the main window """
    window = MainWindow()
#     window.setWindowIcon(QIcon('images/logo.png'))
    window.setWindowFlags(Qt.WindowStaysOnTopHint)
    window.setWindowTitle(" ".join([app.applicationName(), app.applicationVersion()]))
    window.showNormal()
    window.setFixedSize(0, 0)
    window.show()
    app.exec_()
