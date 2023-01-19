from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QFrame, QPushButton, QFileDialog
from src.models.enums import Channels
from src.views.widgets.channel import Channel
from src.models.model_texture import ModelTexture


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.file_resolution = (2048, 2048)
        self.resolutions = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

        self.setup_ui()

    def setup_ui(self):
        _grid_spacing = 20
        _grid_margin = 20
        _r_channel_default_value = 150
        _g_channel_default_value = 150
        _b_channel_default_value = 150
        _a_channel_default_value = 255

        self.setStyleSheet("""background: #222222;""")
        _grid = QGridLayout()
        _grid.setAlignment(Qt.AlignLeft)
        _grid.setSpacing(_grid_spacing)
        _grid.setContentsMargins(_grid_margin, _grid_margin, _grid_margin, _grid_margin)
        self.setLayout(_grid)

        main_widget = QWidget()
        main_widget.setLayout(_grid)
        self.setCentralWidget(main_widget)

        self.r_channel = Channel(channel_type=Channels.RED, default_value=_r_channel_default_value)
        self.g_channel = Channel(channel_type=Channels.GREEN, default_value=_g_channel_default_value)
        self.b_channel = Channel(channel_type=Channels.BLUE, default_value=_b_channel_default_value)
        self.a_channel = Channel(channel_type=Channels.ALPHA, default_value=_a_channel_default_value)

        _separator = QFrame()
        _separator.setFrameShape(QFrame.HLine)
        _separator.setFrameShadow(QFrame.Raised)
        _separator.setLineWidth(0)

        _export_button = QPushButton()
        _export_button.setText("Export")
        _export_button.clicked.connect(self.export_texture)

        _grid.addWidget(self.r_channel, 0, 0)
        _grid.addWidget(self.g_channel, 0, 1)
        _grid.addWidget(self.b_channel, 0, 2)
        _grid.addWidget(self.a_channel, 0, 3)
        _grid.addWidget(_separator, 4, 0, 1, 4)
        _grid.addWidget(_export_button, 5, 0, 1, 4)

        """ Create all style sheet """
        _font_size = 10
        _font_color = "f2f2f2"
        _font_family = "Noto Sans"
        _border_radius = 3
        _separator.setStyleSheet("""background: #181818;""")
        _export_button.setStyleSheet("""
        QPushButton { background-color: #009bfc; color: #%s; border-radius: %spx; height: 40px; font: %spt '%s'; font-weight: regular;}
        QPushButton:hover { background: #0079ca; }
        QPushButton:pressed { background: #0069bd; }
        QPushButton:disabled { background: #505050; }""" % (_font_color, _border_radius, _font_size, _font_family))

    def export_texture(self):
        _file_path = QFileDialog.getSaveFileName(self, 'Save File', "", "JPG (*.jpg);; JPG (*.jpg);; JPEG (*.jpeg) ;;PNG (*.png)")
        _path = _file_path[0]
        _format = _file_path[1]
        if _path != '' and _format != '':
            _new_texture = ModelTexture(_channel_r=self.r_channel.channel_data.get_data(),
                                        _channel_g=self.g_channel.channel_data.get_data(),
                                        _channel_b=self.b_channel.channel_data.get_data(),
                                        _channel_a=self.a_channel.channel_data.get_data(),
                                        _format=_format,
                                        _resolution=self.file_resolution,
                                        _quality=95,
                                        _subsampling=0)
            _new_texture.save_image(_full_path=fr"{_path}")
