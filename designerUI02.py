# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designerUI02.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1043, 764)
        self.test_bt = QtWidgets.QPushButton(Form)
        self.test_bt.setGeometry(QtCore.QRect(550, 660, 81, 61))
        self.test_bt.setObjectName("test_bt")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 20, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(460, 80, 121, 20))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(800, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.datawidget = MplWidget(Form)
        self.datawidget.setGeometry(QtCore.QRect(70, 150, 531, 491))
        self.datawidget.setObjectName("datawidget")
        self.costwidget = mplwidget2(Form)
        self.costwidget.setGeometry(QtCore.QRect(650, 270, 341, 281))
        self.costwidget.setObjectName("costwidget")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 660, 141, 59))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filenamelabel = QtWidgets.QLabel(self.layoutWidget)
        self.filenamelabel.setObjectName("filenamelabel")
        self.verticalLayout.addWidget(self.filenamelabel)
        self.openbt = QtWidgets.QPushButton(self.layoutWidget)
        self.openbt.setObjectName("openbt")
        self.verticalLayout.addWidget(self.openbt)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(180, 670, 127, 47))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.learninglabel = QtWidgets.QLabel(self.layoutWidget1)
        self.learninglabel.setObjectName("learninglabel")
        self.verticalLayout_2.addWidget(self.learninglabel)
        self.learninginput = QtWidgets.QLineEdit(self.layoutWidget1)
        self.learninginput.setObjectName("learninginput")
        self.verticalLayout_2.addWidget(self.learninginput)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(320, 670, 127, 47))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.iterationlabel = QtWidgets.QLabel(self.layoutWidget2)
        self.iterationlabel.setObjectName("iterationlabel")
        self.verticalLayout_3.addWidget(self.iterationlabel)
        self.iterationinput = QtWidgets.QLineEdit(self.layoutWidget2)
        self.iterationinput.setObjectName("iterationinput")
        self.verticalLayout_3.addWidget(self.iterationinput)
        self.train_bt = QtWidgets.QPushButton(Form)
        self.train_bt.setGeometry(QtCore.QRect(460, 660, 81, 61))
        self.train_bt.setObjectName("train_bt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.test_bt.setText(_translate("Form", "test"))
        self.label_3.setText(_translate("Form", "Neural Networks HW1"))
        self.label_5.setText(_translate("Form", "104103025 許嘉茵"))
        self.label_7.setText(_translate("Form", "cost"))
        self.filenamelabel.setText(_translate("Form", "filename"))
        self.openbt.setText(_translate("Form", "Open file"))
        self.learninglabel.setText(_translate("Form", "learning rate"))
        self.iterationlabel.setText(_translate("Form", "iteration times"))
        self.train_bt.setText(_translate("Form", "train"))

from mplwidget import MplWidget
from mplwidget2 import mplwidget2
