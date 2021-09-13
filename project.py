from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# import ui
from delete_dialog import Ui_delete_dialog as Ui_Delete_Dialog
from edit_book import Ui_Dialog as Ui_Edit_Dialog
from mainwindow import Ui_MainWindow
from add_book import Ui_Dialog as Ui_Add_Dialog

import mu_functions as lib
from stylesheets import main_style_sheet


class Delete_Dialog(QDialog):
    def __init__(self, parent=None):
        super(Delete_Dialog, self).__init__(parent)
        self.ui = Ui_Delete_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class Edit_Dialog(QDialog):
    def __init__(self, parent=None):
        super(Edit_Dialog, self).__init__(parent)
        self.ui = Ui_Edit_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class Add_Dialog(QDialog):
    def __init__(self, parent=None):
        super(Add_Dialog, self).__init__(parent)
        self.ui = Ui_Add_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.pressed.connect(self.show_add_dialog)
        self.load_issued_tabel()
        self.load_unissued_tabel()
        self.load_all_books_tabel()
        self.edit_issued_3.clicked.connect(
            lambda: self.edit_book(self.issued_books_table_5))
        self.edit_unissued_3.clicked.connect(
            lambda: self.edit_book(self.issued_books_table_6))
        self.delete_issued_3.pressed.connect(
            lambda: self.delete_books(self.issued_books_table_5)
        )
        self.delete_unissued_3.pressed.connect(
            lambda: self.delete_books(self.issued_books_table_6)
        )
        self.refresh_issued_3.clicked.connect(self.load_issued_tabel)
        self.refresh_unissued_3.clicked.connect(self.load_unissued_tabel)
        self.refresh_books.clicked.connect(self.load_all_books_tabel)
        self.search_button.clicked.connect(self.search_book)
        self.setStyleSheet(main_style_sheet)
    def save_existing_book(self, ui):
        book = {
            'id': ui.id_input.text(),
            'name':	ui.name_input.text(),
            'author': ui.author_input.text(),
            'description':	ui.description_input.text(),
            'isbn': ui.isbn_input.text(),
            'page_count': ui.page_input.text(),
            'year': ui.year_input.text(),
            'issued': ui.radioButton.isChecked()
        }
        lib.update_book(book)

    def edit_book(self, table):
        selected_row = table.currentRow()
        print(selected_row)
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            book = lib.find_book(book_id)
            dialog = Edit_Dialog()
            dialog.ui.id_input.setText(str(book.id))
            dialog.ui.name_input.setText(book.name)
            dialog.ui.author_input.setText(book.author)
            dialog.ui.description_input.setText(book.desc)
            dialog.ui.isbn_input.setText(str(book.isbn))
            dialog.ui.page_input.setText(str(book.page_count))
            dialog.ui.year_input.setText(str(book.year))
            dialog.ui.radioButton.setChecked(book.issued)
            if book.issued == False:
                dialog.ui.radioButton_2.setChecked(True)

            dialog.ui.buttonBox.accepted.connect(
                lambda: self.save_existing_book(dialog.ui))
            dialog.exec()
            self.load_issued_tabel()
            self.load_unissued_tabel()

    def save_new_book(self, ui):
        print(ui.id_input.text())
        new_book = {
            'id': int(ui.id_input.text()),
            'name': ui.name_input.text(),
            'author': ui.author_input.text(),
            'description': ui.description_input.text(),
            'isbn': ui.isbn_input.text(),
            'page_count': int(ui.page_input.text()),
            'year': int(ui.year_input.text()),
            'issued': ui.radioButton.isChecked()
        }
        for attr in new_book:
            if new_book[attr] == None and str(new_book[attr]) == "":
                return False
        lib.add_book(new_book)
        self.load_issued_tabel()
        self.load_unissued_tabel()

    def delete_books(self, table):
        selected_row = table.currentRow()
        if selected_row != -1:
            book_id = int(table.item(selected_row, 0).text())
            dialog = Delete_Dialog()
            dialog.ui.buttonBox.accepted.connect(
                lambda: lib.delete_book(book_id)
            )
            dialog.exec()
            self.load_issued_tabel()
            self.load_unissued_tabel()

    def search_book(self):
        if self.search_input.text() != "":
            book = lib.find_book(int(self.search_input.text()))
            if book != None:
                self.search_table.setRowCount(1)
                book_dict = book.to_dict()
                for book_index, attr in enumerate(book_dict):
                    self.search_table.setItem(
                        0, book_index, QTableWidgetItem(str(book_dict[str(attr)])))
                    self.search_table.item(0, book_index).setFlags(
                        Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_issued_tabel(self):
        books = lib.get_issued_books()
        self.issued_books_table_5.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.issued_books_table_5.setItem(
                    index, book_index, QTableWidgetItem(str(book[str(attr)])))
            self.issued_books_table_5.item(index, book_index).setFlags(
                Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_unissued_tabel(self):
        books = lib.get_unissued_books()
        self.issued_books_table_6.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.issued_books_table_6.setItem(
                    index, book_index, QTableWidgetItem(str(book[str(attr)])))
            self.issued_books_table_6.item(index, book_index).setFlags(
                Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def load_all_books_tabel(self):
        books = lib.load_books()
        self.all_books.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                self.all_books.setItem(
                    index, book_index, QTableWidgetItem(str(book[str(attr)])))
            self.all_books.item(index, book_index).setFlags(
                Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def show_add_dialog(self):
        input_dlg = Add_Dialog()
        input_dlg.ui.buttonBox.accepted.connect(
            lambda: self.save_new_book(input_dlg.ui))

        input_dlg.exec()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
