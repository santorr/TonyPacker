from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSlider, QSpinBox, QPushButton, QSizePolicy


class Channel(QWidget):
    def __init__(self, channel_type=0):
        super(Channel, self).__init__()
        self.channel_type = channel_type
        self.data = []

        self.setup_ui()

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
        self.preview = QLabel()
        self.preview.setPixmap(QPixmap("resources/template.jpg"))
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

    def clear_texture(self):
        self.slider.setEnabled(True)
        self.spinbox.setValue(True)
        self.clear_button.setEnabled(False)

    def slider_changed(self):
        self.spinbox.setValue(self.slider.value())

    def spinbox_changed(self):
        self.slider.setValue(self.spinbox.value())

    def import_texture(self):
        self.slider.setEnabled(False)
        self.spinbox.setEnabled(False)
        self.clear_button.setEnabled(True)
