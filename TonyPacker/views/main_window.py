from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget
from TonyPacker.models.enums import Channels
from TonyPacker.views.widgets.channel import Channel


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setup_ui()

    def setup_ui(self):
        """ main window ui """
        self.setStyleSheet("""background: #252525;""")
        """ Create a main grid layout """
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignLeft)
        self.grid.setSpacing(20)
        self.setLayout(self.grid)
        """ Create the main widget """
        main_widget = QWidget()
        main_widget.setLayout(self.grid)
        self.setCentralWidget(main_widget)
        """ Create all channels """
        self.r_channel = Channel(channel_type=Channels.RED)
        self.g_channel = Channel(channel_type=Channels.GREEN)
        self.b_channel = Channel(channel_type=Channels.BLUE)
        self.a_channel = Channel(channel_type=Channels.ALPHA)
        self.grid.addWidget(self.r_channel, 0, 0)
        self.grid.addWidget(self.g_channel, 1, 0)
        self.grid.addWidget(self.b_channel, 2, 0)
        self.grid.addWidget(self.a_channel, 3, 0)
