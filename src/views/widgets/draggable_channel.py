from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QGridLayout
from pathlib import Path
from src.controllers.custom_widgets import Label
from src.controllers.formats import Formats


class DraggableImage(QWidget):
    def __init__(self, channel):
        QWidget.__init__(self)
        self.channel = channel

        self.setAcceptDrops(True)
        self.resolution = 150
        self.setFixedSize(QSize(self.resolution, self.resolution))
        self.grid = QGridLayout()
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(0)
        self.setLayout(self.grid)

        self.label = self.create_label("Drag image here")
        self.grid.addWidget(self.label, 0, 0)

    def dragEnterEvent(self, event):
        """ Set the on drag event """
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        """ Set the on move event """
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """ Set the drop event """
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = Path(event.mimeData().urls()[0].toLocalFile())
            file_extension = file_path.suffix.lower()
            if file_extension in Formats().get_extension_list():
                self.channel.set_channel_with_image(file_path)
                event.accept()
            else:
                print(f"You can't import {file_extension} format.")
                event.ignore()
        else:
            event.ignore()

    @staticmethod
    def create_label(text):
        label = Label(_text=text)
        label.setAlignment(Qt.AlignCenter)
        return label
