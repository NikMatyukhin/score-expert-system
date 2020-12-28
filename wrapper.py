from PySide2 import QtCore, QtWidgets, QtGui

from ui_wrapper import Ui_MainWindow
from service import KnowledgeBaseService
from rules import RulesDialog
from facts import FactsDialog


class ExpertSystemWrapper(QtWidgets.QMainWindow):
    def __init__(self):
        super(ExpertSystemWrapper, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(807, 594)
        self.setWindowTitle("Отправитель на экзамен")

        self.k_base = KnowledgeBaseService()

        self.ui.action.triggered.connect(self.open_rules_dialog)
        self.ui.action_4.triggered.connect(self.open_facts_dialog)
        self.ui.action_6.triggered.connect(self.load_base)
        self.ui.action_8.triggered.connect(self.save_base)

    def load_base(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        self.k_base.load(filepath)

        self.ui.treeWidget.model().removeRows(
            0, self.ui.tableWidget.rowCount())

        self.fill_requested_facts_table()

    def save_base(self):
        if self.k_base.filepath:
            self.k_base.save()
        else:
            filepath = QtWidgets.QFileDialog.getSaveFileName(self)[0]
            self.k_base.save(filepath=filepath)

    def fill_requested_facts_table(self):
        self.ui.tableWidget.model().removeRows(
            0, self.ui.tableWidget.rowCount())
        if self.k_base.facts:
            for fact in self.k_base.facts:
                if self.k_base.facts[fact]['request']:
                    self.ui.tableWidget.insertRow(0)
                    item_fact = QtWidgets.QTableWidgetItem(fact)
                    item_meaning = QtWidgets.QComboBox()
                    item_meaning.addItems(self.k_base.facts[fact]['mean'])
                    self.ui.tableWidget.setItem(0, 0, item_fact)
                    self.ui.tableWidget.setCellWidget(0, 1, item_meaning)
                    item_meaning.currentTextChanged.connect(self.logic_print)

    def open_facts_dialog(self):
        window = FactsDialog()

        window.factAdded.connect(self.k_base.add_fact)
        window.factDeleted.connect(self.k_base.delete_fact)

        window.fill_tree(self.k_base.facts)

        window.exec_()

        self.fill_requested_facts_table()

    def open_rules_dialog(self):
        window = RulesDialog()

        window.ruleAdded.connect(self.k_base.add_rule)
        window.ruleDeleted.connect(self.k_base.delete_rule)

        window.fill_table(self.k_base.rules)
        window.fill_combobox(self.k_base.facts)

        window.exec_()

    def logic_print(self, text):
        self.ui.treeWidget.invisibleRootItem().takeChildren()

        rules = self.k_base.rules[:]
        memory = self.given_facts()

        while (rule := self.accessible_situation(rules, memory)):
            rules.remove(rule)
            if_item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['ЕСЛИ'])
            used_facts = self.extract_facts(rule['situation'], memory.keys())

            for fact in used_facts:
                child_item = QtWidgets.QTreeWidgetItem(
                    if_item, [f'{fact} равен {memory[fact]}'])
                if_item.addChild(child_item)

            self.ui.treeWidget.addTopLevelItem(if_item)

            then_item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget, ['ТО'])

            conclusion, meaning = rule['production'].split(' = ')
            memory[conclusion] = meaning[1:-1]
            consequent_item = QtWidgets.QTreeWidgetItem(
                then_item, [f'{conclusion} становится {meaning[1:-1]}'])

            then_item.addChild(consequent_item)

            self.ui.treeWidget.addTopLevelItem(then_item)

    def given_facts(self):
        row_count = self.ui.tableWidget.rowCount()
        facts = {}
        for i in range(row_count):
            fact = self.ui.tableWidget.item(i, 0).text()
            meaning = self.ui.tableWidget.cellWidget(i, 1).currentText()[1:-1]
            facts[fact] = meaning
        return facts

    def accessible_situation(self, rules: list, memory: dict):
        for rule in rules:
            if eval(rule['situation'], {}, memory):
                return rule
        return str()

    def extract_facts(self, rule, facts):
        return [fact for fact in facts if fact in rule]

    def closeEvent(self, event: QtGui.QCloseEvent):
        if self.k_base.unsaved:
            yes = QtWidgets.QMessageBox.Yes
            no = QtWidgets.QMessageBox.No
            cancel = QtWidgets.QMessageBox.Cancel
            resBtn = QtWidgets.QMessageBox.question(
                self, "Отправитель на экзамен", "Сохранить базу перед выходом?",
                no | yes, yes)
            if resBtn == yes:
                self.save_base()
                event.ignore()
        event.accept()
