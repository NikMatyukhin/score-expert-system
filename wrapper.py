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
        self.k_base = None

        self.ui.action_4.triggered.connect(self.open_facts_dialog)

        self.ui.action.triggered.connect(self.open_rules_dialog)

        self.ui.action_6.triggered.connect(self.load_base)
        self.ui.action_8.triggered.connect(self.save_base)

    def load_base(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        self.k_base = KnowledgeBaseService(filepath)
        self.k_base.load()

        domains_number = len(self.k_base.domains)

        for domain in self.k_base.domains:
            if self.k_base.domains[domain]['request']:
                self.ui.tableWidget.insertRow(0)
                item_domain = QtWidgets.QTableWidgetItem(domain)
                self.ui.tableWidget.setItem(0, 0, item_domain)

    def save_base(self):
        filepath = QtWidgets.QFileDialog.getSaveFileName(self)[0]

    def open_facts_dialog(self):
        window = FactsDialog()
        window.exec_()

    def open_rules_dialog(self):
        window = RulesDialog()

        window.ruleAdded.connect(self.k_base.add_rule)
        window.ruleDeleted.connect(self.k_base.delete_rule)

        window.fill_table(self.k_base.rules)
        window.fill_combobox(self.k_base.domains)

        window.exec_()
