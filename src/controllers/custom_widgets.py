from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSpinBox, QLineEdit, QPushButton, QSlider, QLabel

_font_size = 10
_font_color = "f2f2f2"
_font_family = "Noto Sans"
_border_radius = 3


class SpinBox(QSpinBox):
    def __init__(self, _minimum_value=0, _maximum_value=255, _default_value=150):
        QSpinBox.__init__(self)
        self.setMinimum(_minimum_value)
        self.setMaximum(_maximum_value)
        self.setValue(_default_value)

        self.setAlignment(Qt.AlignHCenter)
        self.lineEdit().setReadOnly(False)

        self.setup_style()

    def setup_style(self):
        _font_size = 10
        _font_color = "f2f2f2"
        _font_family = "Noto Sans"

        self.setStyleSheet("""
        QSpinBox { background: #181818; color: #%s; padding-right: 15px; font: %spt '%s'; border-radius: 7px;}
        QSpinBox::up-button { 
            subcontrol-origin: border; 
            subcontrol-position: right; 
            border-image: url(images/spinup.png); 
            width: 20px; 
            height: 20px;
        }
        QSpinBox::up-button:hover {
            border-image: url(images/spinup_hover.png);
        }
        QSpinBox::up-button:pressed {
            border-image: url(images/spinup_pressed.png);
        }
        QSpinBox::down-button { 
            subcontrol-origin: border; 
            subcontrol-position: left;
            border-image: url(images/spindown.png); 
            width: 20px; 
            height: 20px;
        }
        QSpinBox::down-button:hover {
            border-image: url(images/spindown_hover.png);
        }
        QSpinBox::down-button:pressed {
            border-image: url(images/spindown_pressed.png);
        }
        """ % (_font_color, _font_size, _font_family))


class LineEdit(QLineEdit):
    def __init__(self):
        QLineEdit.__init__(self)

    def setup_style(self):
        pass


class Button(QPushButton):
    def __init__(self, _color_normal, _color_hover, _color_pressed, _color_disabled, _text="Button", _height=40):
        super(Button, self).__init__()
        self.color_normal = _color_normal
        self.color_hover = _color_hover
        self.color_pressed = _color_pressed
        self.color_disabled = _color_disabled
        self.height = _height

        self.setText(_text)
        self.setup_style()

    def setup_style(self):
        self.setStyleSheet("""
        QPushButton { 
            background-color: #%s; 
            color: #%s; 
            border-radius: %spx; 
            height: %spx; 
            font: %spt '%s'; 
            font-weight: regular;
            }
        QPushButton:hover { 
            background: #%s; 
            }
        QPushButton:pressed { 
            background: #%s; 
            }
        QPushButton:disabled { 
            background: #%s; 
            }""" % (
            self.color_normal,
            _font_color,
            _border_radius,
            self.height,
            _font_size,
            _font_family,
            self.color_hover,
            self.color_pressed,
            self.color_disabled))


class VerticalSlider(QSlider):
    def __init__(self, _minimum=0, _maximum=100, _tick_interval=1):
        super(QSlider, self).__init__()
        self.setMinimum(_minimum)
        self.setMaximum(_maximum)
        self.setTickInterval(_tick_interval)

        self.setup_style()

    def setup_style(self):
        self.setStyleSheet("""
        QSlider::groove:vertical { width: 15px; background: #181818; border-radius: 7px; }
        QSlider::handle:vertical { background: #009bfc; width: 15px; height: 15px; border-radius: 7px;}
        QSlider::handle:vertical:disabled { background: #505050;}
        """)


class Label(QLabel):
    def __init__(self, _text=""):
        super(QLabel, self).__init__()
        self.setText(_text)

        self.setup_style()

    def setup_style(self):
        self.setStyleSheet("""
        color: #%s; font: %spt '%s';
        """ % (_font_color, _font_size, _font_family))