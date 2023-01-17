from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget, QLineEdit, QSizePolicy, QLabel


class SpinBox(QWidget):
    def __init__(self, _minimum_value=0, _maximum_value=255, _default_value=150):
        QWidget.__init__(self)
        self.minimum_value = _minimum_value
        self.maximum_value = _maximum_value
        self.value = _default_value

        self.setup_ui()

    def setup_ui(self):
        _layout = QHBoxLayout()
        _layout.setSpacing(0)
        self.setLayout(_layout)

        self.decrement_button = QPushButton()
        self.decrement_button.setText("-")

        self.increment_button = QPushButton()
        self.increment_button.setText("+")

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.set_value(self.value)

        self.decrement_button.clicked.connect(self.decrement)
        self.increment_button.clicked.connect(self.increment)

        _layout.addWidget(self.decrement_button)
        _layout.addWidget(self.label)
        _layout.addWidget(self.increment_button)

        self.set_style()

    def set_style(self):
        _font_size = 10
        _font_color = "f2f2f2"
        _font_family = "Noto Sans"
        _height = 25
        _top_border_radius = 3
        _bottom_border_radius = 3

        self.label.setStyleSheet("""
        color: #%s; font: %spt '%s'; background-color: black; border: 0; height: %spx;
        """ % (_font_color, _font_size, _font_family, _height))
        self.decrement_button.setStyleSheet("""
        QPushButton { background-color: #009bfc; color: #%s; height: %spx; width: 30px; font: %spt '%s'; border-top-left-radius :%spx; border-bottom-left-radius : %spx;}
        QPushButton:hover { background: #0079ca; }
        QPushButton:pressed { background: #0069bd; }
        QPushButton:disabled { background: #505050; }""" % (_font_color, _height, _font_size, _font_family, _top_border_radius, _bottom_border_radius))
        self.increment_button.setStyleSheet("""
        QPushButton { background-color: #009bfc; color: #%s; height: %spx; width: 30px; font: %spt '%s'; border-top-right-radius :%spx; border-bottom-right-radius : %spx;}
        QPushButton:hover { background: #0079ca; }
        QPushButton:pressed { background: #0069bd; }
        QPushButton:disabled { background: #505050; }""" % (_font_color, _height, _font_size, _font_family, _top_border_radius, _bottom_border_radius))

    def decrement(self):
        self.set_value(self.value - 1)

    def increment(self):
        self.set_value(self.value + 1)

    def set_value(self, value: int):
        if value < self.minimum_value:
            self.value = self.minimum_value
        elif value > self.maximum_value:
            self.value = self.maximum_value
        else:
            self.value = value

        self.label.setText(str(self.value))

    def get_value(self):
        return self.value
