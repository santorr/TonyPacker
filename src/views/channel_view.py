from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy
from src.controllers.draggable_channel import DraggableImage
from src.models.channel import Channel
from src.controllers.custom_widgets import SpinBox, Button, VerticalSlider, Label


class ChannelView(QWidget):
    def __init__(self, _channel_type=None, _default_value=255):
        super(ChannelView, self).__init__()
        """ Init variables """
        self.channel_type = _channel_type
        self.default_value = _default_value
        """ Create channel data """
        self.channel_data = Channel()
        """ Create Ui """
        self.setup_ui()
        """ Create all connect """
        self.clear_button.clicked.connect(self.clear_texture)
        self.spinbox.valueChanged.connect(self.on_spinbox_changed)
        self.slider.valueChanged.connect(self.on_slider_changed)
        """ Set slider value """
        self.slider.setValue(self.default_value)

    def setup_ui(self):
        """ Create all the setup for the channel ui """
        _grid = QGridLayout()
        _grid.setContentsMargins(0, 0, 0, 0)
        _grid.setSpacing(0)
        self.setLayout(_grid)

        self.channel_name = Label(_text=self.channel_type.name[0])
        self.channel_resolution = Label(_text="2 x 2")

        self.channel_name.setAlignment(Qt.AlignCenter)
        self.channel_resolution.setAlignment(Qt.AlignCenter)
        _sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.channel_resolution.setSizePolicy(_sizePolicy)
        self.channel_name.setSizePolicy(_sizePolicy)
        self.channel_name.setContentsMargins(0, 0, 0, 10)

        self.preview = DraggableImage(self)
        _sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.preview.setSizePolicy(_sizePolicy)

        self.slider = VerticalSlider(_minimum=0, _maximum=255, _tick_interval=1)
        _sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.slider.setSizePolicy(_sizePolicy)

        self.spinbox = SpinBox()

        self.clear_button = Button(_text="Clear", _color_normal='fc2100', _color_hover='ca1e00', _color_pressed='bd2400', _color_disabled='505050', _height=30)
        self.clear_button.setEnabled(False)

        _grid.addWidget(self.channel_name, 0, 0, 1, 2)
        _grid.addWidget(self.channel_resolution, 1, 0, 1, 2)
        _grid.addWidget(self.preview, 2, 0)
        _grid.addWidget(self.slider, 2, 1)
        _grid.addWidget(self.spinbox, 3, 0, 1, 2)
        _grid.addWidget(self.clear_button, 4, 0, 1, 2)

    def clear_texture(self):
        self.slider.setEnabled(True)
        self.spinbox.setEnabled(True)
        self.clear_button.setEnabled(False)
        self.set_channel_with_slider()

    def on_slider_changed(self):
        self.spinbox.setValue(self.slider.value())
        self.set_channel_with_slider()

    def on_spinbox_changed(self):
        self.slider.setValue(self.spinbox.value())

    def set_channel_with_slider(self):
        self.channel_data.fill_data_with_uniform_value(self.slider.value())
        self.set_preview_channel()

    def set_channel_with_image(self, image_path):
        self.slider.setEnabled(False)
        self.spinbox.setEnabled(False)
        self.clear_button.setEnabled(True)

        self.channel_data.fill_data_with_image(image_path)
        self.set_preview_channel()

    def set_preview_channel(self):
        """ Set the preview image """
        self.channel_resolution.setText(f"{self.channel_data.get_data_size()[0]} x {self.channel_data.get_data_size()[1]}")
        _preview_size = self.preview.resolution
        img = QPixmap.fromImage(ImageQt(self.channel_data.get_image()))
        self.preview.label.setPixmap(img.scaled(_preview_size, _preview_size, Qt.KeepAspectRatio))
