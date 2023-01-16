from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSlider, QSpinBox, QPushButton, QSizePolicy
from TonyPacker.views.widgets.draggable_channel import DraggableImage
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
        img = QPixmap.fromImage(ImageQt(self.channel_data.get_image((200, 200))))
        self.preview.label.setPixmap(img)

    # def bgr_to_rgb(self, array: np.ndarray) -> np.ndarray:
    #     """ Return a RGB array from a BGR array """
    #     return cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
