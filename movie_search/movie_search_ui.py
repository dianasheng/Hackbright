import mainwindow
import movie_data_manager
from PyQt4 import QtGui
import sys


class MovieSearch(QtGui.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(MovieSearch, self).__init__()  # allows us to access methods and variables from mainwindow.py
        self.setupUi(self)
        self.setWindowTitle("Movie Search")
        self.movie_data_list = movie_data_manager.load_movie_data()
        self.year_list = movie_data_manager.get_release_year_list()
        self.initialize_widgets()

    def initialize_widgets(self):
        #fill combobox with years
        for year in self.year_list:
            self.cmb_release_year.addItem(year)

        #connect the button
        self.btn_ok_year.clicked.connect(lambda: self.fill_table_results(self.cmb_release_year.currentText()))

    def fill_table_results(self, year):
        movie_list = movie_data_manager.get_movie_info_by_year(year)
        self.tbl_results.setColumnCount(5)
        self.tbl_results.setRowCount(50)

        row = 0
        col = 0
        for info in movie_list:
            item = QtGui.QTableWidgetItem(info.title)

            self.tbl_results.setItem(row, col, QtGui.QTableWidgetItem(info.title))
            self.tbl_results.setItem(row, col+1, QtGui.QTableWidgetItem(info.director))
            self.tbl_results.setItem(row, col+2, QtGui.QTableWidgetItem(info.actor_1))
            self.tbl_results.setItem(row, col+3, QtGui.QTableWidgetItem(info.actor_2))
            self.tbl_results.setItem(row, col+4, QtGui.QTableWidgetItem(info.location))
            row += 1
            col = 0


def main():
    app = QtGui.QApplication(sys.argv)
    window = MovieSearch()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
    