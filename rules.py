from PySide2 import QtCore, QtWidgets

from ui_rules import Ui_Dialog


class RulesDialog(QtWidgets.QDialog):
    def __init__(self):
        super(RulesDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(700, 565)
        self.setWindowTitle("Работа с правилами")

    def fill_table(self, rules: list):
        for rule in rules:
            situation, production = rule['situation'], rule['production']
            item_situation = QtWidgets.QTableWidgetItem(situation)
            item_production = QtWidgets.QTableWidgetItem(production)

            self.ui.tableWidget.insertRow(0)
            self.ui.tableWidget.setItem(0, 0, item_situation)
            self.ui.tableWidget.setItem(0, 1, item_production)

    def fill_combobox(self, domains: list):
        self.ui.comboBox.clear()
        self.ui.comboBox.insertItems(0, domains)
