from PySide2 import QtCore, QtWidgets

from ui_rules import Ui_Dialog


class RulesDialog(QtWidgets.QDialog):
    ruleAdded = QtCore.Signal(dict)
    ruleDeleted = QtCore.Signal(str)

    def __init__(self):
        super(RulesDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setFixedSize(700, 565)
        self.setWindowTitle("Работа с правилами")

        self.ui.comboBox.currentTextChanged.connect(self.domain_changed)
        self.ui.toolButton_2.clicked.connect(self.clear_form)
        self.ui.toolButton.clicked.connect(self.add_rule)

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

    def fill_combobox(self, domains: dict):
        self.ui.comboBox.clear()

        if domains:
            self.domains = domains
            self.ui.comboBox.addItems(domains.keys())

    def domain_changed(self, text):
        self.ui.comboBox_2.clear()

        if text:
            self.ui.comboBox_2.addItems(self.domains[text]['mean'])

    def clear_form(self):
        self.ui.lineEdit.clear()
        self.ui.comboBox.setCurrentIndex(0)

    def add_rule(self):
        situation = self.ui.lineEdit.text()

        if situation:
            domain = self.ui.comboBox.currentText()
            meaning = self.ui.comboBox_2.currentText()
            production = domain + ' = ' + meaning

            rule = {
                'situation': situation,
                'production': production,
            }

            self.ruleAdded.emit(rule)

            self.push_rule_front_table(situation, production)
