from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSlider, QSpinBox, QPushButton, QSizePolicy

from TonyPacker.models.enums import Channels
from TonyPacker.views.widgets.draggable_channel import DraggableImage
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
        self.label.setStyleSheet("""color: #ffffff;""")
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
        self.clear_button.setStyleSheet("""
        QPushButton { background-color: #202020; color: #ffffff; border-radius: 7px; height: 30px; }
        QPushButton:hover { background: #252525; }
        QPushButton:disabled { background: #505050; }""")
        self.slider.setStyleSheet("""
        QSlider::groove:vertical { width: 15px; background: #202020; border-radius: 7px; }
        QSlider::handle:vertical { background: #4aa4fa; width: 15px; height: 15px; border-radius: 7px;}
        """)
        self.spinbox.setStyleSheet("""
        QSpinBox { background: #202020; color: #ffffff; padding-right: 15px; }
        QSpinBox::up-button { subcontrol-origin: border; subcontrol-position: top right }
        QSpinBox::up-arrow { width: 7px; height: 7px; }
        QSpinBox::down-button { subcontrol-origin: border; subcontrol-position: bottom right; }
        """)

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
        if len(array.shape) > 2:
            if self.channel_type == Channels.RED:
                print("On doit garder le channel rouge")
            elif self.channel_type == Channels.GREEN:
                print("On doit garder le channel vert")
            elif self.channel_type == Channels.BLUE:
                print("On doit garder le channel bleu")
            elif self.channel_type == Channels.ALPHA:
                print("On doit garder le channel alpha")
        else:
            """ On doit garder le seul channel existant """
            print(array.shape)

    def open_image(self, image_path):
        return Image.open(image_path)

    def image_to_array(self, image):
        return numpy.asarray(image)

    def array_to_image(self, array):
        return Image.fromarray(array)

    def resize_array(self, array, size):
        return numpy.resize(array, (size, size))

    def resize_image(self, image, size):
        return Image.fromarray(numpy.array(image.resize((size, size))))

