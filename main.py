import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.select_data()
        self.connection = sqlite3.connect("coffee.sqlite")


    def select_data(self):
        self.connection = sqlite3.connect("coffee.sqlite")
        res = self.connection.cursor().execute('SELECT * from coffee').fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.connection.close()


class EditCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.create_btn.clicked.connect(self.create_coffee)
        self.edit_btn.clicked.connect(self.edit_coffee)

        self.connection = sqlite3.connect("coffee.sqlite")
        self.cur = self.connection.cursor()

        result = self.cur.execute('SELECT sale FROM coffee').fetchall()
        self.comboBox_1.addItems([str(item[0]) for item in result])

        result = self.cur.execute('SELECT zerna FROM coffee').fetchall()
        self.comboBox_2.addItems([str(item[0]) for item in result])

        result = self.cur.execute('SELECT description FROM coffee').fetchall()
        self.comboBox_3.addItems([str(item[0]) for item in result])

        result = self.cur.execute('SELECT objarka FROM coffee').fetchall()
        self.comboBox_4.addItems([str(item[0]) for item in result])

        result = self.cur.execute('SELECT sort FROM coffee').fetchall()
        self.comboBox_5.addItems([str(item[0]) for item in result])

        result = self.cur.execute('SELECT volume FROM coffee').fetchall()
        self.comboBox_6.addItems([str(item[0]) for item in result])

        result = self.cur.execute('SELECT id FROM coffee').fetchall()
        self.comboBox_7.addItems([str(item[0]) for item in result])

        self.connection.close()


    def create_coffee(self):
        self.connection = sqlite3.connect("coffee.sqlite")
        self.cur = self.connection.cursor()
        self.cur.execute('INSERT INTO coffee (sort, objarka, zerna, description, sale, volume) '
                         'VALUES (?, ?, ?, ?, ?, ?)',
                         (self.lineEdit_6.text(), self.lineEdit_4.text(), self.lineEdit_2.text(),
                          self.lineEdit_3.text(), self.lineEdit_1.text(), self.lineEdit_5.text()))
        self.connection.commit()
        self.connection.close()


    def edit_coffee(self):
        self.connection = sqlite3.connect("coffee.sqlite")
        self.cur = self.connection.cursor()
        self.cur.execute('UPDATE coffee SET sort = ?, objarka = ?, zerna = ?, description = ?, sale = ?, volume = ? '
                         'WHERE id = ?',
                         (self.lineEdit_66.text(), self.lineEdit_44.text(), self.lineEdit_22.text(),
                          self.lineEdit_33.text(), self.lineEdit_11.text(), self.lineEdit_55.text(), self.lineEdit_id.text()))
        self.connection.commit()
        self.connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()

    ex1 = EditCoffee()
    ex1.show()

    sys.exit(app.exec())