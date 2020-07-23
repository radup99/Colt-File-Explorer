# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setMaximumSize(QtCore.QSize(30, 20))
        self.backBtn.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.fwdBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fwdBtn.sizePolicy().hasHeightForWidth())
        self.fwdBtn.setSizePolicy(sizePolicy)
        self.fwdBtn.setMaximumSize(QtCore.QSize(30, 20))
        self.fwdBtn.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.fwdBtn.setObjectName("fwdBtn")
        self.horizontalLayout.addWidget(self.fwdBtn)
        self.pathBar = QtWidgets.QLineEdit(self.centralwidget)
        self.pathBar.setObjectName("pathBar")
        self.horizontalLayout.addWidget(self.pathBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fileTable = QtWidgets.QTableWidget(self.centralwidget)
        self.fileTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fileTable.setShowGrid(False)
        self.fileTable.setWordWrap(False)
        self.fileTable.setObjectName("fileTable")
        self.fileTable.setColumnCount(3)
        self.fileTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(2, item)
        self.fileTable.horizontalHeader().setMinimumSectionSize(20)
        self.fileTable.verticalHeader().setVisible(False)
        self.fileTable.verticalHeader().setDefaultSectionSize(23)
        self.verticalLayout.addWidget(self.fileTable)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backBtn.setText(_translate("MainWindow", "<"))
        self.fwdBtn.setText(_translate("MainWindow", ">"))
        item = self.fileTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.fileTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.fileTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
