from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication,
                             QHBoxLayout, QVBoxLayout, QFormLayout )
from PyQt5.QtGui import QPixmap

icons = {
    "Folder": "icons/folder.png",
    "File": "icons/file.png"
}

class FileWidget(QWidget):
    def __init__(self, text, filetype):
        super().__init__()

        self.text = text
        self.type = filetype
        self.icon = QLabel(self)
        self.fileName = QLabel(self)

        self.icon.setMaximumSize(QtCore.QSize(15, 15))
        self.fileName.setMaximumSize((QtCore.QSize(10000,15)))
        self.setLayout(QFormLayout())
        self.layout().setWidget(0, QtWidgets.QFormLayout.LabelRole, self.icon)
        self.layout().setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fileName)

        self.set_icon()
        # self.icon.setPixmap(QtGui.QPixmap("folder.png"))
        # self.icon.setScaledContents(True)

        self.fileName.setText(text)

    def get_text(self):
        return self.text

    def set_icon(self):
        img = icons.get(self.type, "icons/file.png")
        self.icon.setPixmap(QtGui.QPixmap(img))
        self.icon.setScaledContents(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = FileWidget("Sample Folder", "Folder")
    Form.show()
    sys.exit(app.exec_())
