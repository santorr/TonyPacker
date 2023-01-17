import sys
from PyQt5.QtWidgets import QApplication
from TonyPacker.views.main_window import MainWindow

if __name__ == "__main__":
    """ Run the application """
    app = QApplication(sys.argv)
    app.setApplicationName('Tony Packer')
    app.setApplicationVersion("0.0.1")
    """ Create the main window """
    window = MainWindow()
    window.setWindowTitle(" ".join([app.applicationName(), app.applicationVersion()]))
    window.showNormal()
    window.setFixedSize(0, 0)
    window.show()
    app.exec_()
