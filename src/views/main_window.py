import pathlib

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QFileDialog
from pathlib import Path

from src.controllers.formats import Formats
from src.controllers.resolution_controller import ResolutionController
from src.models.enums import Channels
from src.views.widgets.channel import Channel
from src.models.model_texture import ModelTexture
from src.controllers.custom_widgets import Button, HorizontalSeparator


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.r_channel = Channel(_channel_type=Channels.RED, _default_value=150)
        self.g_channel = Channel(_channel_type=Channels.GREEN, _default_value=150)
        self.b_channel = Channel(_channel_type=Channels.BLUE, _default_value=150)
        self.a_channel = Channel(_channel_type=Channels.ALPHA, _default_value=255)
        self.separator = HorizontalSeparator(_color='181818')
        self.resolution_controller = ResolutionController(_default_resolution=(1024, 1024))
        self.export_button = Button(_text="Export", _color_normal='009bfc', _color_hover='0079ca',
                                    _color_pressed='0069bd', _color_disabled='505050')
        self.export_button.clicked.connect(self.export_texture)

        self.setup_ui()

    def setup_ui(self):
        _grid_spacing = 20
        _grid_margin = 20

        self.setStyleSheet("""background: #222222;""")
        _grid = QGridLayout()
        _grid.setAlignment(Qt.AlignLeft)
        _grid.setSpacing(_grid_spacing)
        _grid.setContentsMargins(_grid_margin, _grid_margin, _grid_margin, _grid_margin)
        self.setLayout(_grid)

        main_widget = QWidget()
        main_widget.setLayout(_grid)
        self.setCentralWidget(main_widget)

        _grid.addWidget(self.r_channel, 0, 0)
        _grid.addWidget(self.g_channel, 0, 1)
        _grid.addWidget(self.b_channel, 0, 2)
        _grid.addWidget(self.a_channel, 0, 3)
        _grid.addWidget(self.separator, 4, 0, 1, 4)
        _grid.addWidget(self.resolution_controller, 5, 0, 1, 2)
        _grid.addWidget(self.export_button, 5, 2, 1, 2)

    def export_texture(self):
        _file_path = QFileDialog.getSaveFileName(self, 'Save File', "", Formats().get_export_formats())
        _path = Path(_file_path[0])
        _format = Formats().get_format(_format_extension=_path.suffix)

        if _path != '' and _format != '':
            _new_texture = ModelTexture(_channel_r=self.r_channel.channel_data.get_data(),
                                        _channel_g=self.g_channel.channel_data.get_data(),
                                        _channel_b=self.b_channel.channel_data.get_data(),
                                        _channel_a=self.a_channel.channel_data.get_data(),
                                        _format=_format,
                                        _resolution=self.resolution_controller.get_resolution(),
                                        _quality=95,
                                        _subsampling=0)
            _new_texture.save_image(_full_path=fr"{_path}")
