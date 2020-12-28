# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rulesdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 565)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 680, 20))
        self.label.setMinimumSize(QSize(680, 20))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 640, 30))
        self.lineEdit.setMinimumSize(QSize(510, 30))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 70, 320, 30))
        self.comboBox.setMinimumSize(QSize(310, 30))
        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(660, 70, 30, 30))
        self.toolButton.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 110, 680, 420))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(680, 420))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(332)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 530, 680, 30))
        self.buttonBox.setMinimumSize(QSize(680, 30))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(340, 70, 310, 30))
        self.comboBox_2.setMinimumSize(QSize(310, 30))
        self.toolButton_2 = QToolButton(Dialog)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(660, 30, 30, 30))
        self.toolButton_2.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"repeat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0417\u0434\u0435\u0441\u044c \u043c\u043e\u0436\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u043e. \u0412\u043f\u0438\u0448\u0438\u0442\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u043e \u0438 \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438 \u043d\u0438\u0436\u0435.", None))
        self.toolButton.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u0430\u0432\u0438\u043b", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f", None));
    # retranslateUi

