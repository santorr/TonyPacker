from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QFrame, QPushButton, QFileDialog
from TonyPacker.models.enums import Channels
from TonyPacker.views.widgets.channel import Channel
from TonyPacker.models.model_channel import ModelChannel


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # test = ModelChannel()
        # test.fill_data_with_image(_image_path=r"C:\Users\santorr\Documents\Megascans Library\Downloaded\surface\brick_rough_vgvmcgf\Thumbs\1k\vgvmcgf_1K_Albedo.jpg")
        # test.save_image()
        self.file_resolution = (512, 512)

        self.setup_ui()

    def setup_ui(self):
        """ main window ui """
        self.setStyleSheet("""background: #222222;""")
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
        self.r_channel = Channel(channel_type=Channels.RED, default_value=150)
        self.g_channel = Channel(channel_type=Channels.GREEN, default_value=150)
        self.b_channel = Channel(channel_type=Channels.BLUE, default_value=150)
        self.a_channel = Channel(channel_type=Channels.ALPHA, default_value=255)
        """ Create a separator """
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        """ Create an export button """
        export_button = QPushButton()
        export_button.setText("Export")
        export_button.clicked.connect(self.export_texture)
        """ Grid all components """
        self.grid.addWidget(self.r_channel, 0, 0)
        self.grid.addWidget(self.g_channel, 0, 1)
        self.grid.addWidget(self.b_channel, 0, 2)
        self.grid.addWidget(self.a_channel, 0, 3)
        self.grid.addWidget(separator, 4, 0)
        self.grid.addWidget(export_button, 5, 0)

        """ Create all style sheet """
        font_color = "d8d8d8"
        font_family = "Noto Sans"
        separator.setStyleSheet("""background: #4aa4fa;""")
        export_button.setStyleSheet("""
        QPushButton { background-color: #4aa4fa; color: #%s; border-radius: 7px; height: 30px; font: 8pt '%s';}
        QPushButton:hover { background: #252525; }
        QPushButton:disabled { background: #505050; }""" % (font_color, font_family))

    def export_texture(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
