from PyQt5.QtWidgets import QMainWindow

from TonyPacker.views.main_window_convert import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
