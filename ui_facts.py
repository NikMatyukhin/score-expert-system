# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'factsdialog.ui'
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
        Dialog.resize(700, 535)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 680, 20))
        self.label.setMinimumSize(QSize(680, 20))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 640, 30))
        self.lineEdit.setMinimumSize(QSize(640, 30))
        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(660, 30, 30, 30))
        self.toolButton.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.treeWidget = QTreeWidget(Dialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 70, 680, 431))
        self.treeWidget.setMinimumSize(QSize(680, 430))
        self.treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(15)
        self.treeWidget.setAnimated(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 500, 680, 31))
        self.buttonBox.setMinimumSize(QSize(680, 30))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0417\u0434\u0435\u0441\u044c \u043c\u043e\u0436\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0444\u0430\u043a\u0442 \u0438 \u0435\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f. \u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u0444\u0430\u043a\u0442 \u0438 \u0434\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u0435\u043c\u0443 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u043d\u0438\u0436\u0435.", None))
        self.toolButton.setText("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u043a\u0442\u043e\u0432", None));
    # retranslateUi

