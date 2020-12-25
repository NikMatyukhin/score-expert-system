from PySide2 import QtCore, QtWidgets

from ui_facts import Ui_Dialog


class FactsDialog(QtWidgets.QDialog):
    def __init__(self):
        super(FactsDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(700, 535)
        self.setWindowTitle("Работа с фактами")
