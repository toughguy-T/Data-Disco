# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Data_Disco.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Data_Disco(object):
    def setupUi(self, Data_Disco):
        Data_Disco.setObjectName("Data_Disco")
        Data_Disco.resize(1588, 1500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(Data_Disco.sizePolicy().hasHeightForWidth())
        Data_Disco.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Data_Disco)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_top1 = QtWidgets.QPushButton(Data_Disco)
        self.pushButton_top1.setMaximumSize(QtCore.QSize(616, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_top1.setFont(font)
        self.pushButton_top1.setObjectName("pushButton_top1")
        self.horizontalLayout.addWidget(self.pushButton_top1)
        self.pushButton_top2 = QtWidgets.QPushButton(Data_Disco)
        self.pushButton_top2.setMaximumSize(QtCore.QSize(615, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_top2.setFont(font)
        self.pushButton_top2.setObjectName("pushButton_top2")
        self.horizontalLayout.addWidget(self.pushButton_top2)
        self.pushButton_top3 = QtWidgets.QPushButton(Data_Disco)
        self.pushButton_top3.setMaximumSize(QtCore.QSize(616, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_top3.setFont(font)
        self.pushButton_top3.setObjectName("pushButton_top3")
        self.horizontalLayout.addWidget(self.pushButton_top3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Data_Disco)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.stackedWidget = QtWidgets.QStackedWidget(Data_Disco)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_dataproceesing = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_dataproceesing.sizePolicy().hasHeightForWidth())
        self.page_dataproceesing.setSizePolicy(sizePolicy)
        self.page_dataproceesing.setObjectName("page_dataproceesing")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_dataproceesing)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.page_dataproceesing)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setMaximumSize(QtCore.QSize(521, 16777215))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.data_processing_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_processing_pushButton.sizePolicy().hasHeightForWidth())
        self.data_processing_pushButton.setSizePolicy(sizePolicy)
        self.data_processing_pushButton.setMaximumSize(QtCore.QSize(98, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.data_processing_pushButton.setFont(font)
        self.data_processing_pushButton.setObjectName("data_processing_pushButton")
        self.gridLayout.addWidget(self.data_processing_pushButton, 0, 0, 1, 1)
        self.csv_save_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csv_save_pushButton.sizePolicy().hasHeightForWidth())
        self.csv_save_pushButton.setSizePolicy(sizePolicy)
        self.csv_save_pushButton.setMaximumSize(QtCore.QSize(98, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.csv_save_pushButton.setFont(font)
        self.csv_save_pushButton.setObjectName("csv_save_pushButton")
        self.gridLayout.addWidget(self.csv_save_pushButton, 1, 0, 1, 1)
        self.sourcepath_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourcepath_lineEdit.sizePolicy().hasHeightForWidth())
        self.sourcepath_lineEdit.setSizePolicy(sizePolicy)
        self.sourcepath_lineEdit.setMaximumSize(QtCore.QSize(413, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.sourcepath_lineEdit.setFont(font)
        self.sourcepath_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sourcepath_lineEdit.setObjectName("sourcepath_lineEdit")
        self.gridLayout.addWidget(self.sourcepath_lineEdit, 0, 1, 1, 1)
        self.csv_savepath_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csv_savepath_lineEdit.sizePolicy().hasHeightForWidth())
        self.csv_savepath_lineEdit.setSizePolicy(sizePolicy)
        self.csv_savepath_lineEdit.setMaximumSize(QtCore.QSize(413, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.csv_savepath_lineEdit.setFont(font)
        self.csv_savepath_lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.csv_savepath_lineEdit.setObjectName("csv_savepath_lineEdit")
        self.gridLayout.addWidget(self.csv_savepath_lineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(256, 16777215))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.start_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy)
        self.start_pushButton.setMaximumSize(QtCore.QSize(255, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout_2.addWidget(self.start_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(517, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.file_info = QtWidgets.QLabel(self.layoutWidget)
        self.file_info.setMaximumSize(QtCore.QSize(517, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.file_info.setFont(font)
        self.file_info.setText("")
        self.file_info.setObjectName("file_info")
        self.verticalLayout_3.addWidget(self.file_info)
        self.listView = QtWidgets.QListView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMaximumSize(QtCore.QSize(517, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.info_data = QtWidgets.QTableWidget(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_data.sizePolicy().hasHeightForWidth())
        self.info_data.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info_data.setFont(font)
        self.info_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_data.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.info_data.setLineWidth(1)
        self.info_data.setMidLineWidth(0)
        self.info_data.setObjectName("info_data")
        self.info_data.setColumnCount(1)
        self.info_data.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_data.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_data.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_data.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_data.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_data.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.info_data.setHorizontalHeaderItem(0, item)
        self.info_data.horizontalHeader().setDefaultSectionSize(500)
        self.info_data.horizontalHeader().setMinimumSectionSize(500)
        self.info_data.horizontalHeader().setStretchLastSection(True)
        self.info_data.verticalHeader().setDefaultSectionSize(32)
        self.info_data.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.info_data)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.fits_graphicsView = QtWidgets.QGraphicsView(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fits_graphicsView.sizePolicy().hasHeightForWidth())
        self.fits_graphicsView.setSizePolicy(sizePolicy)
        self.fits_graphicsView.setObjectName("fits_graphicsView")
        self.verticalLayout_2.addWidget(self.fits_graphicsView)
        self.verticalLayout_5.addWidget(self.splitter)
        self.stackedWidget.addWidget(self.page_dataproceesing)
        self.page_classifier = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_classifier.sizePolicy().hasHeightForWidth())
        self.page_classifier.setSizePolicy(sizePolicy)
        self.page_classifier.setObjectName("page_classifier")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_classifier)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Classifier_comboBox = QtWidgets.QComboBox(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Classifier_comboBox.sizePolicy().hasHeightForWidth())
        self.Classifier_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Classifier_comboBox.setFont(font)
        self.Classifier_comboBox.setObjectName("Classifier_comboBox")
        self.gridLayout_2.addWidget(self.Classifier_comboBox, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.Classifier_lineEdit = QtWidgets.QLineEdit(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Classifier_lineEdit.sizePolicy().hasHeightForWidth())
        self.Classifier_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Classifier_lineEdit.setFont(font)
        self.Classifier_lineEdit.setObjectName("Classifier_lineEdit")
        self.gridLayout_2.addWidget(self.Classifier_lineEdit, 0, 2, 1, 1)
        self.Datachoose_pushButton = QtWidgets.QPushButton(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Datachoose_pushButton.sizePolicy().hasHeightForWidth())
        self.Datachoose_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.Datachoose_pushButton.setFont(font)
        self.Datachoose_pushButton.setObjectName("Datachoose_pushButton")
        self.gridLayout_2.addWidget(self.Datachoose_pushButton, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 1)
        self.DataSource_lineEdit = QtWidgets.QLineEdit(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataSource_lineEdit.sizePolicy().hasHeightForWidth())
        self.DataSource_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.DataSource_lineEdit.setFont(font)
        self.DataSource_lineEdit.setObjectName("DataSource_lineEdit")
        self.gridLayout_2.addWidget(self.DataSource_lineEdit, 1, 2, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        self.line_2 = QtWidgets.QFrame(self.page_classifier)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.info_model = QtWidgets.QTableWidget(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_model.sizePolicy().hasHeightForWidth())
        self.info_model.setSizePolicy(sizePolicy)
        self.info_model.setObjectName("info_model")
        self.info_model.setColumnCount(1)
        self.info_model.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_model.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_model.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_model.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_model.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.info_model.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_model.setHorizontalHeaderItem(0, item)
        self.info_model.horizontalHeader().setDefaultSectionSize(500)
        self.info_model.horizontalHeader().setMinimumSectionSize(500)
        self.info_model.horizontalHeader().setStretchLastSection(True)
        self.info_model.verticalHeader().setDefaultSectionSize(31)
        self.info_model.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_8.addWidget(self.info_model)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.Start_pushButton = QtWidgets.QPushButton(self.page_classifier)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.Start_pushButton.setFont(font)
        self.Start_pushButton.setObjectName("Start_pushButton")
        self.horizontalLayout_6.addWidget(self.Start_pushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.line_4 = QtWidgets.QFrame(self.page_classifier)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_8.addWidget(self.line_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.page_classifier)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.Result_listView = QtWidgets.QListView(self.page_classifier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Result_listView.sizePolicy().hasHeightForWidth())
        self.Result_listView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Result_listView.setFont(font)
        self.Result_listView.setObjectName("Result_listView")
        self.verticalLayout_6.addWidget(self.Result_listView)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.line_3 = QtWidgets.QFrame(self.page_classifier)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.page_classifier)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.class_result_tableView = QtWidgets.QTableView(self.page_classifier)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.class_result_tableView.setFont(font)
        self.class_result_tableView.setObjectName("class_result_tableView")
        self.class_result_tableView.horizontalHeader().setDefaultSectionSize(400)
        self.class_result_tableView.horizontalHeader().setMinimumSectionSize(400)
        self.class_result_tableView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_7.addWidget(self.class_result_tableView)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_16.addLayout(self.horizontalLayout_3)
        self.line_5 = QtWidgets.QFrame(self.page_classifier)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_16.addWidget(self.line_5)
        self.stackedWidget.addWidget(self.page_classifier)
        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.retranslateUi(Data_Disco)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Data_Disco)

    def retranslateUi(self, Data_Disco):
        _translate = QtCore.QCoreApplication.translate
        Data_Disco.setWindowTitle(_translate("Data_Disco", "Data-Disco"))
        self.pushButton_top1.setText(_translate("Data_Disco", "数据预处理"))
        self.pushButton_top2.setText(_translate("Data_Disco", "分类"))
        self.pushButton_top3.setText(_translate("Data_Disco", "聚类"))
        self.data_processing_pushButton.setText(_translate("Data_Disco", "选取文件夹"))
        self.csv_save_pushButton.setText(_translate("Data_Disco", "数据存储路径"))
        self.start_pushButton.setText(_translate("Data_Disco", "start"))
        self.label.setText(_translate("Data_Disco", "已选择的文件："))
        self.label_2.setText(_translate("Data_Disco", "数据总览"))
        item = self.info_data.verticalHeaderItem(0)
        item.setText(_translate("Data_Disco", "                                                 Name                                                 "))
        item = self.info_data.verticalHeaderItem(1)
        item.setText(_translate("Data_Disco", "                                                 Max                                                 "))
        item = self.info_data.verticalHeaderItem(2)
        item.setText(_translate("Data_Disco", "                                                 Min                                                 "))
        item = self.info_data.verticalHeaderItem(3)
        item.setText(_translate("Data_Disco", "                                                 Mean                                                 "))
        item = self.info_data.verticalHeaderItem(4)
        item.setText(_translate("Data_Disco", "                                                 Stdev                                                 "))
        self.label_3.setText(_translate("Data_Disco", "图像预览"))
        self.label_9.setText(_translate("Data_Disco", "选择分类器"))
        self.Datachoose_pushButton.setText(_translate("Data_Disco", "选择数据"))
        self.label_10.setText(_translate("Data_Disco", "分类数据"))
        item = self.info_model.verticalHeaderItem(0)
        item.setText(_translate("Data_Disco", "                         Accuracy(Train)                         "))
        item = self.info_model.verticalHeaderItem(1)
        item.setText(_translate("Data_Disco", "                         Accuracy(Test)                         "))
        item = self.info_model.verticalHeaderItem(2)
        item.setText(_translate("Data_Disco", "                         Features                         "))
        item = self.info_model.verticalHeaderItem(3)
        item.setText(_translate("Data_Disco", "                         Data(Train)                         "))
        item = self.info_model.verticalHeaderItem(4)
        item.setText(_translate("Data_Disco", "                         Data(Test)                         "))
        self.Start_pushButton.setText(_translate("Data_Disco", "Start"))
        self.label_8.setText(_translate("Data_Disco", "Result-List"))
        self.label_4.setText(_translate("Data_Disco", "输出"))