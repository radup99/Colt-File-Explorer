from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from mainwindow import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow("D:")
    win.setWindowTitle("Colt File Manager")
    win.show_file_list()
    win.show()
    sys.exit(app.exec_())
