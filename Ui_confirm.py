# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_confirm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirm_Dialog(object):
    def setupUi(self, confirm_Dialog):
        confirm_Dialog.setObjectName("confirm_Dialog")
        confirm_Dialog.resize(663, 396)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(confirm_Dialog.sizePolicy().hasHeightForWidth())
        confirm_Dialog.setSizePolicy(sizePolicy)
        confirm_Dialog.setMinimumSize(QtCore.QSize(663, 396))
        confirm_Dialog.setMaximumSize(QtCore.QSize(663, 396))
        self.verticalLayout = QtWidgets.QVBoxLayout(confirm_Dialog)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.source_label = QtWidgets.QLabel(confirm_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.source_label.setFont(font)
        self.source_label.setObjectName("source_label")
        self.verticalLayout.addWidget(self.source_label)
        self.csv_save_label = QtWidgets.QLabel(confirm_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.csv_save_label.setFont(font)
        self.csv_save_label.setObjectName("png_save_label")
        self.verticalLayout.addWidget(self.csv_save_label)
        self.confirm_buttonBox = QtWidgets.QDialogButtonBox(confirm_Dialog)
        self.confirm_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.confirm_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.confirm_buttonBox.setObjectName("confirm_buttonBox")
        self.verticalLayout.addWidget(self.confirm_buttonBox)

        self.retranslateUi(confirm_Dialog)
        self.confirm_buttonBox.accepted.connect(confirm_Dialog.accept)
        self.confirm_buttonBox.rejected.connect(confirm_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(confirm_Dialog)

    def retranslateUi(self, confirm_Dialog):
        _translate = QtCore.QCoreApplication.translate
        confirm_Dialog.setWindowTitle(_translate("confirm_Dialog", "Confirm"))
        self.source_label.setText(_translate("confirm_Dialog", "TextLabel"))
        self.csv_save_label.setText(_translate("confirm_Dialog", "TextLabel"))
