# -*- coding: utf-8 -*-

"""
Module implementing confirm_Dialog.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_confirm import Ui_confirm_Dialog


class confirm_Dialog(QDialog, Ui_confirm_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(confirm_Dialog, self).__init__(parent)

        self.setupUi(self)
    
    @pyqtSlot()
    def on_confirm_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        self.done(1)

    def reject(self):
        self.done(-1)
