from PySide2 import QtCore, QtWidgets

from ui_facts import Ui_Dialog
from meanings import MeaningsDialog


class FactsDialog(QtWidgets.QDialog):
    factAdded = QtCore.Signal(dict)
    factDeleted = QtCore.Signal(str)
    meanChanged = QtCore.Signal(str, list)

    def __init__(self):
        super(FactsDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.facts = {}

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setFixedSize(700, 535)
        self.setWindowTitle("Работа с фактами")

        self.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.toolButton.clicked.connect(self.add_fact)

    def fill_tree(self, facts: dict):
        if facts:
            self.facts = facts

        for fact, data in facts.items():
            meanings = data['mean']
            self.push_fact_front_tree(fact, meanings)

    def push_fact_front_tree(self, parent: str, children: list):
        item_parent = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, [parent])

        item_children = [QtWidgets.QTreeWidgetItem(
            item_parent, [child]) for child in children]
        item_parent.addChildren(item_children)

        self.ui.treeWidget.addTopLevelItem(item_parent)

    def show_context_menu(self, point: QtCore.QPoint):
        menu = QtWidgets.QMenu()
        change_action = menu.addAction('Изменить значения')
        delete_action = menu.addAction('Удалить факт')

        if self.ui.treeWidget.hasFocus():
            if self.ui.treeWidget.invisibleRootItem().childCount():
                if self.ui.treeWidget.currentItem().childCount():
                    change_action.triggered.connect(self.change_meaning)
                    delete_action.triggered.connect(self.delete_fact)
                    menu.exec_(self.mapToGlobal(point))

    def add_fact(self):
        fact = self.ui.lineEdit.text().strip()

        window = MeaningsDialog(fact)
        window.exec_()

        meanings = window.get_meanings_list()
        requested = window.get_requested()
        if not meanings:
            QtWidgets.QMessageBox.critical(
                'Ошибка ввода!', 'Невозможно добавить факт без значений.')
            return

        if fact:
            self.factAdded.emit(
                {fact: {'mean': meanings, 'request': requested}})
            self.facts.update({fact: {'mean': meanings, 'request': requested}})
            self.push_fact_front_tree(fact, meanings)

    def delete_fact(self):
        cur_item = self.ui.treeWidget.currentItem()
        cur_item_child = [
            cur_item.child(i) for i in range(cur_item.childCount())]
        fact = cur_item.text(0)

        self.factDeleted.emit(fact)

        self.ui.treeWidget.invisibleRootItem().removeChild(cur_item)

    def change_meaning(self):
        cur_item = self.ui.treeWidget.currentItem()
        fact = cur_item.text(0)
        meanings = self.facts[fact]['mean']

        window = MeaningsDialog(fact)

        window.fill_list(meanings)
        window.block_requested()

        window.exec_()
        meanings = window.get_meanings_list()

        if not meanings:
            QtWidgets.QMessageBox.critical(
                self,
                'Ошибка ввода!',
                'Невозможно оставить факт без значений.\n' +
                f'Факт "{fact}" будет удалён из списка фактов.')
            self.delete_fact()
            return

        self.meanChanged.emit(fact, meanings)
        self.ui.treeWidget.invisibleRootItem().removeChild(cur_item)
        self.facts[fact]['mean'] = meanings
        self.push_fact_front_tree(fact, meanings)
