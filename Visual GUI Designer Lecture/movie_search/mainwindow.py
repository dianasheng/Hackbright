# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(668, 504)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.cmb_release_year = QtGui.QComboBox(self.centralWidget)
        self.cmb_release_year.setGeometry(QtCore.QRect(40, 63, 151, 26))
        self.cmb_release_year.setObjectName(_fromUtf8("cmb_release_year"))
        self.btn_ok_year = QtGui.QPushButton(self.centralWidget)
        self.btn_ok_year.setGeometry(QtCore.QRect(210, 60, 81, 32))
        self.btn_ok_year.setObjectName(_fromUtf8("btn_ok_year"))
        self.tbl_results = QtGui.QTableWidget(self.centralWidget)
        self.tbl_results.setGeometry(QtCore.QRect(30, 110, 611, 311))
        self.tbl_results.setObjectName(_fromUtf8("tbl_results"))
        self.tbl_results.setColumnCount(0)
        self.tbl_results.setRowCount(0)
        self.lbl_year = QtGui.QLabel(self.centralWidget)
        self.lbl_year.setGeometry(QtCore.QRect(40, 30, 211, 31))
        self.lbl_year.setObjectName(_fromUtf8("lbl_year"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 668, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_ok_year.setText(_translate("MainWindow", "OK", None))
        self.lbl_year.setText(_translate("MainWindow", "Please choose a release year.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

