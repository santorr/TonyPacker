from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5.QtWidgets import QSpinBox, QLineEdit, QPushButton, QSlider, QLabel, QFrame, QSizePolicy

from src.controllers.utility import absolute_path

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
        _spinup = absolute_path('images/spinup.png')
        _spinup_hover = absolute_path('images/spinup_hover.png')
        _spinup_pressed = absolute_path('images/spinup_pressed.png')

        _spindown = absolute_path('images/spindown.png')
        _spindown_hover = absolute_path('images/spindown_hover.png')
        _spindown_pressed = absolute_path('images/spindown_pressed.png')

        self.setStyleSheet(f"""
        QSpinBox {{ background: #181818; color: #{_font_color}; padding-right: 15px; font: {_font_size}pt '{_font_family}'; border-radius: 7px;}}
        QSpinBox::up-button {{ 
            subcontrol-origin: border; 
            subcontrol-position: right; 
            border-image: url({_spinup}); 
            width: 20px; 
            height: 20px;
        }}
        QSpinBox::up-button:hover {{
            border-image: url({_spinup_hover});
        }}
        QSpinBox::up-button:pressed {{
            border-image: url({_spinup_pressed});
        }}
        QSpinBox::down-button {{ 
            subcontrol-origin: border; 
            subcontrol-position: left;
            border-image: url({_spindown}); 
            width: 20px; 
            height: 20px;
        }}
        QSpinBox::down-button:hover {{
            border-image: url({_spindown_hover});
        }}
        QSpinBox::down-button:pressed {{
            border-image: url({_spindown_pressed});
        }}
        """)


class IntEntry(QLineEdit):
    def __init__(self, _color, _default_value=2048):
        QLineEdit.__init__(self)
        self.color = _color

        self.setText(str(_default_value))
        _int_validator = QIntValidator()
        self.setValidator(_int_validator)
        self.setAlignment(Qt.AlignHCenter)
        _sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(_sizePolicy)

        self.setup_style()

    def setup_style(self):
        self.setStyleSheet(f"""
        QLineEdit {{ 
            color: #{_font_color}; 
            font: {_font_size}pt '{_font_family}'; 
            font-weight: regular;
            background-color: #{self.color}; 
            border-radius: {_border_radius}px; 
            }}
        QLineEdit:disabled {{ 
            background: #505050; 
            }}""")

    def set_value(self, _value):
        self.setText(str(_value))

    def get_value(self):
        return int(self.text())


class Button(QPushButton):
    def __init__(self, _color_normal, _color_hover, _color_pressed, _color_disabled, _text="Button", _height=40):
        super(Button, self).__init__()
        self.color_normal = _color_normal
        self.color_hover = _color_hover
        self.color_pressed = _color_pressed
        self.color_disabled = _color_disabled
        self.height = _height
        self.setFocusPolicy(Qt.NoFocus)
        self.setText(_text)
        self.setup_style()

    def setup_style(self):
        self.setStyleSheet(f"""
        QPushButton {{ 
            background-color: #{self.color_normal}; 
            color: #{_font_color}; 
            border-radius: {_border_radius}px; 
            height: {self.height}px; 
            font: {_font_size}pt '{_font_family}'; 
            font-weight: regular;
            }}
        QPushButton:hover {{ 
            background: #{self.color_hover}; 
            }}
        QPushButton:pressed {{ 
            background: #{self.color_pressed}; 
            }}
        QPushButton:disabled {{ 
            background: #{self.color_disabled}; 
            }}""")


class ToggleButton(QPushButton):
    def __init__(self, _color_unchecked: str,  _color_checked: str, _default_value: bool = False,
                 _image_path: str = None):
        super(ToggleButton, self).__init__()
        self.color_unchecked = _color_unchecked
        self.color_checked = _color_checked

        self.setFocusPolicy(Qt.NoFocus)
        self.setCheckable(True)
        self.setChecked(_default_value)

        if _image_path is not None:
            # images\\toggle_resolution.png
            self.setIcon(QIcon(absolute_path(_image_path)))

        self.setup_style()

    def setup_style(self):
        self.setStyleSheet(f"""
        QPushButton {{ 
            background-color: #{self.color_unchecked}; 
            border-radius: {_border_radius}px;
            }}
        QPushButton:checked {{ 
            background: #{self.color_checked};
            }}""")


class VerticalSlider(QSlider):
    def __init__(self, _minimum=0, _maximum=100, _tick_interval=1):
        super(QSlider, self).__init__()
        self.setMinimum(_minimum)
        self.setMaximum(_maximum)
        self.setTickInterval(_tick_interval)
        self.setFocusPolicy(Qt.NoFocus)
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
        self.setStyleSheet(f"""
        color: #{_font_color}; font: {_font_size}pt '{_font_family}';
        """)


class HorizontalSeparator(QFrame):
    def __init__(self, _color):
        super(QFrame, self).__init__()
        self.color = _color

        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Raised)
        self.setLineWidth(0)

        self.setup_style()

    def setup_style(self):
        self.setStyleSheet(f"""
        background: #{self.color};
        """)
