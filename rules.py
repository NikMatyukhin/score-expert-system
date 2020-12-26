from PySide2 import QtCore, QtWidgets

from ui_rules import Ui_Dialog


class RulesDialog(QtWidgets.QDialog):
    ruleAdded = QtCore.Signal(dict)
    ruleDeleted = QtCore.Signal(dict)

    def __init__(self):
        super(RulesDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.setFixedSize(700, 565)
        self.setWindowTitle("Работа с правилами")

        self.ui.comboBox.currentTextChanged.connect(self.fact_changed)
        self.ui.toolButton_2.clicked.connect(self.clear_form)
        self.ui.toolButton.clicked.connect(self.add_rule)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def fill_table(self, rules: list):
        for rule in rules:
            situation, production = rule['situation'], rule['production']

            self.push_rule_front_table(situation, production)

    def push_rule_front_table(self, situation, production):
        item_situation = QtWidgets.QTableWidgetItem(situation)
        item_production = QtWidgets.QTableWidgetItem(production)

        self.ui.tableWidget.insertRow(0)
        self.ui.tableWidget.setItem(0, 0, item_situation)
        self.ui.tableWidget.setItem(0, 1, item_production)

    def fill_combobox(self, facts: dict):
        self.ui.comboBox.clear()

        if facts:
            self.facts = facts
            self.ui.comboBox.addItems(facts.keys())

    def fact_changed(self, text):
        self.ui.comboBox_2.clear()

        if text:
            self.ui.comboBox_2.addItems(self.facts[text]['mean'])

    def clear_form(self):
        self.ui.lineEdit.clear()
        self.ui.comboBox.setCurrentIndex(0)

    def show_context_menu(self, point: QtCore.QPoint):
        menu = QtWidgets.QMenu()
        delete_action = menu.addAction('Удалить правило')

        if self.ui.tableWidget.hasFocus():
            delete_action.triggered.connect(self.delete_rule)
            menu.exec_(self.mapToGlobal(point))

    def add_rule(self):
        situation = self.ui.lineEdit.text().strip()

        if situation:
            fact = self.ui.comboBox.currentText().strip()
            meaning = self.ui.comboBox_2.currentText().strip()
            production = fact + ' = ' + meaning

            rule = {
                'situation': situation,
                'production': production,
            }

            self.ruleAdded.emit(rule)

            self.push_rule_front_table(situation, production)

    def delete_rule(self):
        row = self.ui.tableWidget.currentRow()

        situation = self.ui.tableWidget.item(row, 0).text()
        production = self.ui.tableWidget.item(row, 1).text()

        rule = {
            'situation': situation,
            'production': production,
        }

        self.ruleDeleted.emit(rule)

        self.ui.tableWidget.removeRow(row)
