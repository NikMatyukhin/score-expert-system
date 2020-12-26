from PySide2 import QtCore, QtWidgets

from ui_meanings import Ui_Dialog


class MeaningsDialog(QtWidgets.QDialog):
    def __init__(self, fact):
        super(MeaningsDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.setFixedSize(371, 480)
        self.setWindowTitle(f"Работа со значениями \"{fact}\"")

        self.ui.pushButton.clicked.connect(self.add_meaning)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def block_requested(self):
        self.ui.checkBox.setEnabled(False)

    def fill_list(self, meanings: list):
        for meaning in meanings:
            self.push_meaning_front_list(meaning)

    def push_meaning_front_list(self, meaning):
        item_meaning = QtWidgets.QListWidgetItem(meaning)
        self.ui.listWidget.addItem(item_meaning)

    def show_context_menu(self, point: QtCore.QPoint):
        menu = QtWidgets.QMenu()
        delete_action = menu.addAction('Удалить значение')

        if self.ui.listWidget.hasFocus():
            delete_action.triggered.connect(self.delete_meaning)
            menu.exec_(self.mapToGlobal(point))

    def add_meaning(self):
        meaning = self.ui.lineEdit.text().strip()

        if meaning:
            self.push_meaning_front_list(meaning)

    def delete_meaning(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def get_meanings_list(self):
        row_count = self.ui.listWidget.count()
        if row_count:
            meanings = [
                self.ui.listWidget.item(i).text() for i in range(row_count)]
            return meanings

    def get_requested(self):
        return self.ui.checkBox.isChecked()
