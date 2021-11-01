import numpy as np
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSlider, QSpinBox, QPushButton, QSizePolicy
import cv2
from TonyPacker.views.widgets.draggable_channel import DraggableImage
from PIL import Image


class Channel(QWidget):
    """
    Cette classe permet de gerer un channel de texture. Il est possible d'y importer une texture ou
    de creer une texture avec une valeur de 0 a 255.
    Dans le cas ou on importe une texture :
    - Drag and drop une image dans le channel
    - Lecture de l'image en format BGR
    - Conversion de l'image en format RGB
    - Isolement du bon channel (R, G ou B selon le channel dans lequel on a glisse la texture)
    - Creation de la miniature pour visualiser ce qui en ressortira
    Dans le cas ou on cree une texture :
    - Creer un array avec la valeur du slider
    - Creation de la miniature pour visualiser ce qui en ressortira
    """
    def __init__(self, channel_type=None, default_value=255):
        super(Channel, self).__init__()
        self.channel_type = channel_type
        self.default_value = default_value
        self.desired_resolution = None
        self.array_full_size = []

        self.setup_ui()
        """ Create all connect """
        self.clear_button.clicked.connect(self.clear_texture)
        self.spinbox.valueChanged.connect(self.spinbox_changed)
        self.slider.valueChanged.connect(self.slider_changed)

        self.slider.setValue(self.default_value)

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
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.slider.setSizePolicy(sizePolicy)

        """ Spinbox """
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(255)

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
        self.spinbox.setEnabled(True)
        self.clear_button.setEnabled(False)
        self.create_empty_array()

    def slider_changed(self):
        self.spinbox.setValue(self.slider.value())
        self.create_empty_array()

    def spinbox_changed(self):
        self.slider.setValue(self.spinbox.value())

    def import_image(self, image_path):
        self.slider.setEnabled(False)
        self.spinbox.setEnabled(False)
        self.clear_button.setEnabled(True)

        """ Open image with cv2 with format BGR, no alpha """
        self.array_full_size = self.open_image(image_path)
        """ Convert BGR to RGB """
        self.array_full_size = self.bgr_to_rgb(self.array_full_size)
        """ Isolate the desired channel, else keep the channel 0 """
        try:
            self.array_full_size = self.array_full_size[:, :, self.channel_type.value]
        except:
            self.array_full_size = self.array_full_size[:, :, 0]

        self.desired_resolution = min(self.array_full_size.shape[0], self.array_full_size.shape[1])
        self.set_preview_image()

    def create_empty_array(self):
        self.array_full_size = np.ones((4, 4), 'uint8') * self.slider.value()
        self.desired_resolution = 2048
        self.set_preview_image()

    def set_preview_image(self):
        print(self.desired_resolution)
        """ Set the preview image """
        preview_img = self.resize_array(array=self.array_full_size, size=self.preview.resolution)
        img = QPixmap.fromImage(ImageQt(Image.fromarray(preview_img)))
        self.preview.label.setPixmap(img)

    def open_image(self, image_path: str) -> np.ndarray:
        """ Open and return a BGR array from image_path """
        return cv2.imread(image_path, cv2.IMREAD_COLOR)

    def bgr_to_rgb(self, array: np.ndarray) -> np.ndarray:
        """ Return a RGB array from a BGR array """
        return cv2.cvtColor(array, cv2.COLOR_BGR2RGB)

    def resize_array(self, array: np.ndarray, size: int) -> np.ndarray:
        """ Resize an array with a specific resolution """
        return cv2.resize(array, dsize=(size, size), interpolation=cv2.INTER_AREA)
