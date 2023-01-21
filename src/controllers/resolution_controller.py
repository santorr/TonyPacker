from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy

from src.controllers.custom_widgets import IntEntry, ToggleButton


class ResolutionController(QWidget):
    def __init__(self, _default_resolution):
        QWidget.__init__(self)
        self.aspect_ratio = 0.0
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        _vertical_layout = QHBoxLayout()
        self.setLayout(_vertical_layout)
        self.resolution_x_entry = IntEntry(_color='181818', _default_value=_default_resolution[0])
        self.resolution_y_entry = IntEntry(_color='181818', _default_value=_default_resolution[1])
        self.lock_aspect_ratio_button = ToggleButton(_color_unchecked='181818', _color_checked='505050',
                                                     _default_value=True, _image_path="images/toggle_resolution.png")

        _vertical_layout.addWidget(self.resolution_x_entry)
        _vertical_layout.addWidget(self.lock_aspect_ratio_button)
        _vertical_layout.addWidget(self.resolution_y_entry)

        self.lock_aspect_ratio_button.clicked.connect(self.set_lock_aspect_ratio)
        self.resolution_x_entry.editingFinished.connect(self.value_changed)

        self.set_lock_aspect_ratio()

    def set_lock_aspect_ratio(self):
        if self.lock_aspect_ratio_button.isChecked():
            self.resolution_y_entry.setEnabled(False)
            self.cal_ratio()
            print(f"Lock aspect ratio : {self.aspect_ratio}")
        else:
            self.resolution_y_entry.setEnabled(True)
            print("Unlock aspect ratio")

    def cal_ratio(self):
        self.aspect_ratio = self.get_resolution_y() / self.get_resolution_x()

    def value_changed(self):
        if self.lock_aspect_ratio_button.isChecked():
            self.resolution_y_entry.set_value(int(self.resolution_x_entry.get_value() * self.aspect_ratio))
        else:
            self.cal_ratio()

    def get_resolution_x(self):
        return self.resolution_x_entry.get_value()

    def get_resolution_y(self):
        return self.resolution_y_entry.get_value()

    def get_resolution(self):
        return self.get_resolution_x, self.get_resolution_y
