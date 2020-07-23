from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from decimal import *
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
        self.file_count = 0
        self.dir_count = 0

        self.ui.setupUi(self)
        self.connect()
        self.show_file_list()

    def connect(self):
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.pathBar.returnPressed.connect(self.update_path)
        self.ui.fileTable.doubleClicked.connect(self.open_item)

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
        self.update_counts()

        self.ui.pathBar.setText(str(self.path))
        self.ui.fileTable.setRowCount(0)

        for dir in self.folders:
            row = self.ui.fileTable.rowCount()
            self.ui.fileTable.insertRow(row)
            self.ui.fileTable.setItem(row, 0, QtWidgets.QTableWidgetItem(dir.name))
            self.ui.fileTable.setItem(row, 1, QtWidgets.QTableWidgetItem("Folder"))

        for f in self.files:
            row = self.ui.fileTable.rowCount()
            size = self.format_size(f.size)
            self.ui.fileTable.insertRow(row)
            self.ui.fileTable.setItem(row, 0, QtWidgets.QTableWidgetItem(f.name))
            self.ui.fileTable.setItem(row, 1, QtWidgets.QTableWidgetItem(f.type))
            self.ui.fileTable.setItem(row, 2, QtWidgets.QTableWidgetItem(size))

    def format_size(self, size):
        if size < 999:
            return f"{size} B"
        if size < 999999:
            num = Decimal(size / 1000)
            return f"{round(num, 2)} KB"
        if size < 999999999:
            num = Decimal(size / 1000000)
            return f"{round(num, 2)} MB"
        if size < 999999999999:
            num = Decimal(size / 1000000000)
            return f"{round(num, 2)} GB"
        return str(size)

    def update_counts(self):
        self.file_count = len(self.files)
        self.dir_count = len(self.folders)

    def open_item(self, item):
        if item.column() != 0:
            return
        name = item.data()
        # self.path.add(name)
        # self.show_file_list()
        if item.row() < self.dir_count:
            self.open_folder(name)
        else:
            self.open_file(name)

    def open_folder(self, dir):
        self.path.add(dir)
        self.show_file_list()

    def open_file(self, file):
        path = PathObject(str(self.path))
        path.add(file)
        os.startfile(str(path))

    def back(self):
        self.path.back()
        self.show_file_list()

    def path_error_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid path!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()