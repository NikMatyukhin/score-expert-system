from PySide2 import QtCore, QtWidgets

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

        self.memory = []
        self.k_base = KnowledgeBaseService()

        self.ui.action_4.triggered.connect(self.open_facts_dialog)

        self.ui.action.triggered.connect(self.open_rules_dialog)

        self.ui.action_6.triggered.connect(self.load_base)
        self.ui.action_8.triggered.connect(self.save_base)

    def load_base(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        self.k_base.load(filepath)

        self.ui.tableWidget.clear()
        self.ui.treeWidget.clear()

        for fact in self.k_base.facts:
            if self.k_base.facts[fact]['request']:
                self.ui.tableWidget.insertRow(0)
                item_fact = QtWidgets.QTableWidgetItem(fact)
                self.ui.tableWidget.setItem(0, 0, item_fact)

    def save_base(self):
        if self.k_base.filepath:
            self.k_base.save()
        else:
            filepath = QtWidgets.QFileDialog.getSaveFileName(self)[0]
            self.k_base.save(filepath=filepath)

    def open_facts_dialog(self):
        window = FactsDialog()

        window.factAdded.connect(self.k_base.add_fact)
        window.factDeleted.connect(self.k_base.delete_fact)

        window.fill_tree(self.k_base.facts)

        window.exec_()

    def open_rules_dialog(self):
        window = RulesDialog()

        window.ruleAdded.connect(self.k_base.add_rule)
        window.ruleDeleted.connect(self.k_base.delete_rule)

        window.fill_table(self.k_base.rules)
        window.fill_combobox(self.k_base.facts)

        window.exec_()
