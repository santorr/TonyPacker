from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSlider, QSpinBox, QPushButton, QSizePolicy

from TonyPacker.models.enums import Channels
from TonyPacker.views.widgets.draggable_channel import DraggableImage
import numpy
from PIL import Image


class Channel(QWidget):
    def __init__(self, channel_type=None):
        super(Channel, self).__init__()
        self.channel_type = channel_type
        self.setup_ui()

        """ On stock les informations de l'image en full resolution """
        self.array_full_size = []
        """ On manipule l'array en partant du full resolution """
        self.array = []

        """ Create all connect """
        self.clear_button.clicked.connect(self.clear_texture)
        self.slider.valueChanged.connect(self.slider_changed)
        self.spinbox.valueChanged.connect(self.spinbox_changed)

    def setup_ui(self):
        """ Create all the setup for the channel ui """
        """ Grid  layout """
        grid = QGridLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)
        self.setLayout(grid)

        """ Label """
        self.label = QLabel(f"Channel ({self.channel_type.name[0]})")
        self.label.setAlignment(Qt.AlignCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.label.setSizePolicy(sizePolicy)

        """ Preview """
        self.preview = DraggableImage(self)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.preview.setSizePolicy(sizePolicy)

        """ Slider """
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setTickInterval(1)
        self.slider.setValue(150)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.slider.setSizePolicy(sizePolicy)

        """ Spinbox """
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(255)
        self.spinbox.setValue(150)

        """ clear_button """
        self.clear_button = QPushButton()
        self.clear_button.setText("Clear")
        self.clear_button.setEnabled(False)

        """ Pack all elements in the layout """
        grid.addWidget(self.label, 0, 0, 1, 2)
        grid.addWidget(self.preview, 1, 0)
        grid.addWidget(self.slider, 1, 1)
        grid.addWidget(self.spinbox, 2, 0, 1, 2)
        grid.addWidget(self.clear_button, 3, 0, 1, 2)

        """ Create all style sheet """
        font_color = "d8d8d8"
        font_family = "Noto Sans"

        self.label.setStyleSheet("""
        color: #%s; font: 8pt '%s';
        """ % (font_color, font_family))
        self.clear_button.setStyleSheet("""
        QPushButton { background-color: #4aa4fa; color: #%s; border-radius: 7px; height: 30px; font: 8pt '%s';}
        QPushButton:hover { background: #252525; }
        QPushButton:disabled { background: #505050; }""" % (font_color, font_family))
        self.slider.setStyleSheet("""
        QSlider::groove:vertical { width: 15px; background: #202020; border-radius: 7px; }
        QSlider::handle:vertical { background: #4aa4fa; width: 15px; height: 15px; border-radius: 7px;}
        QSlider::handle:vertical:disabled { background: #505050;}
        """)
        self.spinbox.setStyleSheet("""
        QSpinBox { background: #202020; color: #%s; padding-right: 15px; font: 8pt '%s';}
        QSpinBox::up-button { subcontrol-origin: border; subcontrol-position: top right }
        QSpinBox::up-arrow { width: 7px; height: 7px; }
        QSpinBox::down-button { subcontrol-origin: border; subcontrol-position: bottom right; }
        """ % (font_color, font_family))

    def clear_texture(self):
        self.slider.setEnabled(True)
        self.spinbox.setValue(True)
        self.clear_button.setEnabled(False)

    def slider_changed(self):
        self.spinbox.setValue(self.slider.value())

    def spinbox_changed(self):
        self.slider.setValue(self.spinbox.value())

    def import_image(self, image_path):
        self.slider.setEnabled(False)
        self.spinbox.setEnabled(False)
        self.clear_button.setEnabled(True)
        """ On extrait les information de l'image sous forme de tableau """
        self.array_full_size = self.image_to_array(self.open_image(image_path))

        self.modify_array_shape(self.array_full_size)

        # img = self.array_to_image(self.resize_array(self.array_full_size, 128))
        # img.save("C:/Users/santorr/Desktop/test.jpeg")

    def modify_array_shape(self, array):
        """
        Isolate the desired channel R, G, B, A
        It's possible to import multiple image types :
        - grayscale : shape(2556, 256)
        - RGB : shape(256, 256, 3)
        - RGBA : shape(256, 256, 4)
        """

        if self.channel_type == Channels.RED:
            result = self.isolate_channel(array, 0)
        elif self.channel_type == Channels.GREEN:
            result = self.isolate_channel(array, 1)
        elif self.channel_type == Channels.BLUE:
            result = self.isolate_channel(array, 2)
        else:
            result = self.isolate_channel(array, 3)

        print(result.shape)

    def isolate_channel(self, array, channel):
        """ Isolate the desired channel
        channel = 0 = RED
        channel = 1 = GREEN
        channel = 2 = BLUE
        channel = 3 = ALPHA
        """
        print(Channels(channel).name)
        if len(array.shape) > 2:
            try:
                return numpy.dsplit(array, array.shape[-1])[channel]
            except:
                return numpy.dsplit(array, array.shape[-1])[0]
        else:
            return array

    def open_image(self, image_path):
        """ Open and return an image from image_path """
        return Image.open(image_path)

    def image_to_array(self, image):
        """ Return an array converted from an image """
        return numpy.asarray(image)

    def array_to_image(self, array):
        """ Return an image converted from an array """
        return Image.fromarray(array)

    def resize_array(self, array, size):
        return numpy.resize(array, (size, size))

    def resize_image(self, image, size):
        return Image.fromarray(numpy.array(image.resize((size, size))))

    def set_preview(self):
        pass
