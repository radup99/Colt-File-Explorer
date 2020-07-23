from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import os

from browser_ui import Ui_MainWindow
from PathObject import PathObject
from file_list import get_files_folders


class MainWindow(QMainWindow):
    def __init__(self, path_text):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.path = PathObject(path_text)
        self.files = []
        self.folders = []

        self.ui.setupUi(self)
        self.connect()
        self.show_file_list()

    def connect(self):
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.pathBar.returnPressed.connect(self.update_path)
        self.ui.fileTable.doubleClicked.connect(self.open_folder)

    def update_path(self):
        path_text = self.ui.pathBar.text()
        if os.path.isdir(path_text):
            self.path.pathtext = path_text
            self.show_file_list()
        else:
            self.path_error_popup()
            self.ui.pathBar.setText(str(self.path))

    def path_error_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid path!")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def show_file_list(self):
        self.files, self.folders = get_files_folders(self.path)

        self.ui.pathBar.setText(str(self.path))
        self.ui.fileTable.setRowCount(0)

        for dir in self.folders:
            row = self.ui.fileTable.rowCount()
            self.ui.fileTable.insertRow(row)
            self.ui.fileTable.setItem(row, 0, QtWidgets.QTableWidgetItem(dir.name))
            self.ui.fileTable.setItem(row, 1, QtWidgets.QTableWidgetItem("Folder"))

        for f in self.files:
            row = self.ui.fileTable.rowCount()
            self.ui.fileTable.insertRow(row)
            self.ui.fileTable.setItem(row, 0, QtWidgets.QTableWidgetItem(f.name))
            self.ui.fileTable.setItem(row, 1, QtWidgets.QTableWidgetItem(f.type))
            self.ui.fileTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(f.size)))

    def open_folder(self, item):
        dir = item.data()
        self.path.add(dir)
        self.show_file_list()

    def back(self):
        self.path.back()
        self.show_file_list()

    def path_error_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid path!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    '''
    def show_file_list(self):
        files, folders = get_files_folders(self.path)

        for dir in folders:
            print(dir.name)

        for f in files:
            print(f.name, f.type, f.size)
    '''