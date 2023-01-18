from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSpinBox


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
