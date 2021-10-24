from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout


class DraggableImage(QWidget):
    def __init__(self, channel):
        QWidget.__init__(self)
        self.channel = channel

        self.setAcceptDrops(True)
        size = 150
        self.setFixedSize(QSize(size, size))
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
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.channel.import_image(file_path)
            event.accept()
        else:
            event.ignore()

    def create_label(self, text):
        label = QLabel()
        label.setText(text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
                QLabel{border: 1px dashed #aaa; color: #aaa}
                """)
        return label
