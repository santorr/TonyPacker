from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSlider, QSpinBox, QPushButton, QSizePolicy
from TonyPacker.views.widgets.draggable_channel import DraggableImage
from TonyPacker.views.widgets.spin_box import SpinBox
from TonyPacker.models.model_channel import ModelChannel


class Channel(QWidget):
    def __init__(self, channel_type=None, default_value=255):
        super(Channel, self).__init__()
        """ Init variables """
        self.channel_type = channel_type
        self.default_value = default_value
        """ Create channel data """
        self.channel_data = ModelChannel()
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

        # self.label = QLabel(f"Channel ({self.channel_type.name[0]})")
        self.label = QLabel(self.channel_type.name[0])
        self.label.setAlignment(Qt.AlignCenter)
        _sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.label.setSizePolicy(_sizePolicy)
        self.label.setContentsMargins(0, 0, 0, 10)

        self.preview = DraggableImage(self)
        _sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.preview.setSizePolicy(_sizePolicy)

        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setTickInterval(1)
        _sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.slider.setSizePolicy(_sizePolicy)

        self.spinbox = SpinBox()

        self.clear_button = QPushButton()
        self.clear_button.setText("Clear")
        self.clear_button.setEnabled(False)

        _grid.addWidget(self.label, 0, 0, 1, 2)
        _grid.addWidget(self.preview, 1, 0)
        _grid.addWidget(self.slider, 1, 1)
        _grid.addWidget(self.spinbox, 2, 0, 1, 2)
        _grid.addWidget(self.clear_button, 3, 0, 1, 2)

        self.setup_style()

    def setup_style(self):
        """ Create all style sheet """
        _font_size = 10
        _font_color = "f2f2f2"
        _font_family = "Noto Sans"
        _border_radius = 3

        self.label.setStyleSheet("""
        color: #%s; font: %spt '%s';
        """ % (_font_color, _font_size, _font_family))
        self.clear_button.setStyleSheet("""
        QPushButton { background-color: #fc2100; color: #%s; border-radius: %spx; height: 30px; font: %spt '%s';}
        QPushButton:hover { background: #ca1e00; }
        QPushButton:pressed { background: #bd2400; }
        QPushButton:disabled { background: #505050; }""" % (_font_color, _border_radius, _font_size, _font_family))
        self.slider.setStyleSheet("""
        QSlider::groove:vertical { width: 15px; background: #181818; border-radius: 7px; }
        QSlider::handle:vertical { background: #009bfc; width: 15px; height: 15px; border-radius: 7px;}
        QSlider::handle:vertical:disabled { background: #505050;}
        """)

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
        self.set_preview_image()

    def set_channel_with_image(self, image_path):
        self.slider.setEnabled(False)
        self.spinbox.setEnabled(False)
        self.clear_button.setEnabled(True)

        self.channel_data.fill_data_with_image(image_path)
        self.set_preview_image()

    def set_preview_image(self):
        """ Set the preview image """
        _preview_size = self.preview.resolution
        img = QPixmap.fromImage(ImageQt(self.channel_data.get_image()))

        self.preview.label.setPixmap(img.scaled(_preview_size, _preview_size, Qt.KeepAspectRatio))
