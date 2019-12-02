# -*- coding: utf-8 -*-

"""
Module implementing data_Disco.
"""
import time
import sys
import os
import json
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot, QStringListModel, QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, \
    QMessageBox, QGraphicsPixmapItem, QGraphicsScene, QTableWidgetItem
from confirm_Dialog import confirm_Dialog
from PyQt5 import QtGui, QtCore
from get_filename import load_path
from read_plot import action
from Data_preview import datapreview
from Ui_Data_Disco import Ui_Data_Disco
import csv
from xgb import classify_xgb
import tempfile


class data_Disco(QWidget, Ui_Data_Disco):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(data_Disco, self).__init__(parent)
        self.setupUi(self)

        self.cwd = os.getcwd()

        self.filename_list = []

        self.file_path = ''
#        self.png_path = ''
        self.csv_savepath = ''
        self.png_savepath = ''

        # 获取模型名字
        self.model_list, self.model_nums = load_path('classifier_model')
        self.Classifier_comboBox.addItems(self.model_list)

        # 获取结果信息
        self.table_item_model = QStandardItemModel(self)
        self.class_result_tableView.setModel(self.table_item_model)

        #
        self.model = QStandardItemModel(self)
        self.class_result_tableView.setModel(self.model)

        # 顶部三个按钮链接三个页面
        self.pushButton_top1.clicked.connect(self.on_pushButton_top1_clicked)
        self.pushButton_top2.clicked.connect(self.on_pushButton_top2_clicked)
        self.pushButton_top3.clicked.connect(self.on_pushButton_top3_clicked)

    # 第一页：数据预处理
    @pyqtSlot()
    def on_pushButton_top1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.stackedWidget.setCurrentIndex(0)

    # 第二页：分类
    @pyqtSlot()
    def on_pushButton_top2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.stackedWidget.setCurrentIndex(1)

    # 第三页：聚类
    @pyqtSlot()
    def on_pushButton_top3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.stackedWidget.setCurrentIndex(2)
    
    @pyqtSlot(int)
    def on_stackedWidget_currentChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        # raise NotImplementedError

    # 选择分类器，显示分类器名字等详情
    @pyqtSlot(str)
    def on_Classifier_comboBox_activated(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.page2_class_result = self.Classifier_comboBox.currentText()
        self.Classifier_lineEdit.setText(self.Classifier_comboBox.currentText())
        with open('json_model.json', 'r') as f:
            info = json.load(f)
            string = self.Classifier_comboBox.currentText().split('.')[0]
            info = info[string]

            i = 0
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(14)

            for key, value in info.items():
                accuracy1_item = QTableWidgetItem(value)
                accuracy1_item.setTextAlignment(QtCore.Qt.AlignCenter)
                accuracy1_item.setFlags(Qt.ItemIsEnabled)
                accuracy1_item.setFont(font)
                self.info_model.setItem(i, 0, accuracy1_item)
                i += 1

    # 第二页：待分类分类数据选取
    @pyqtSlot()
    def on_Datachoose_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 注: QFileDialog中getOpenFilename,getOpenFileNames，getSaveFilename 与getExistingDirectory
        # 不同，返回一个元组，第一个元素是文件路径名字，第二个是文件的类型filetype
        self.page2_data_path = QFileDialog.getOpenFileName(self, '选取文件',
                                                           self.cwd, "All Files (*);;Text Files (*.csv)")
        self.DataSource_lineEdit.setText(self.page2_data_path[0])

    # @pyqtSlot()
    # def on_Cross_Validation_radioButton_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     raise NotImplementedError

    # 第二页：启动按钮
    @pyqtSlot()
    def on_Start_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        classify_xgb(self.page2_data_path[0], self.page2_class_result)
        QMessageBox.information(self, '提示信息', 'Done!')
        self.results_list = []
        path = os.path.abspath('.')
        # if not os.listdir(path + '\\temp'):
        results, results_num = load_path(path + '\\temp')
        slm = QStringListModel()
        for result in results:
            t = time.localtime()
            result = result + ' '*60 + time.strftime("%Y-%m-%d %H:%M:%S", t)
            self.results_list.append(result)

        slm.setStringList(self.results_list)
        self.Result_listView.setModel(slm)

    # 第二页列表响应
    @pyqtSlot(QModelIndex)
    def on_Result_listView_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet

        path = os.path.abspath('.')
        result_index = index.row()
        result_path = self.results_list[int(result_index)]
        result_path = result_path.split()
        new_result_path = result_path[0]
        result_view_path = path + '\\temp\\' + new_result_path
        with open(result_view_path, 'r') as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    # 第一页：数据输出路径按钮
    @pyqtSlot()
    def on_csv_save_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.csv_savepath = QFileDialog.getExistingDirectory(self, '选取文件夹', self.cwd)
        self.csv_savepath_lineEdit.setText(self.csv_savepath)
        self.csv_path = '/'.join(self.csv_savepath.split("\\"))

    # 第一页：数据输入路径按钮
    @pyqtSlot()
    def on_data_processing_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.dir_files = QFileDialog.getExistingDirectory(self, '选取文件夹', self.cwd)
        self.sourcepath_lineEdit.setText(self.dir_files)
        self.file_path = '/'.join(self.dir_files.split("\\"))
        if self.dir_files != '':
            filenames, length = load_path(self.file_path)
            slm = QStringListModel()
            for filename in filenames:
                # 只读取fits文件
                if os.path.splitext(filename)[1] == '.fits':
                    self.filename_list.append(filename)

            # 为listView设置模型
            slm.setStringList(self.filename_list)
            self.listView.setModel(slm)
            self.file_info.setText("一共： " + str(length) + '个fits文件')

    # # 第一页：图像输出按钮
    # @pyqtSlot()
    # def on_png_save_pushButton_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     self.png_savepath = QFileDialog.getExistingDirectory(self, '选取文件夹', self.cwd)
    #     self.png_save_lineEdit.setText(self.png_savepath)
    #     self.png_path = '/'.join(self.png_savepath.split("\\"))

    # 第一页：启动按钮
    @pyqtSlot()
    def on_start_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 弹出对话框，确认所选路径无误
        confirm_info = confirm_Dialog()
        confirm_info.source_label.setText('从目录：' + self.dir_files + ' 选择了' + str(len(self.filename_list)) +
                                          '个fits文件')
        confirm_info.csv_save_label.setText('数据结果保存： ' + self.csv_path + '/result.csv')

        r = confirm_info.exec_()
        # 只有按下确定键，才可执行
        if r > 0:
            action(self.filename_list, self.file_path, self.csv_path)
            QMessageBox.information(self, '提示', 'Done!')

    # 第一页：列表响应
    @pyqtSlot(QModelIndex)
    def on_listView_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet

        # 数据预览的相关函数


        # 预览图像的路径
        with tempfile.TemporaryDirectory() as tmpdirname:

            png_index = index.row()

            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(18)

            max_value, min_value, mean_value, stdev = datapreview(self.filename_list[int(png_index)], self.file_path, tmpdirname)
            name_item = QTableWidgetItem(str(self.filename_list[int(png_index)]))
            name_item.setTextAlignment(QtCore.Qt.AlignCenter)
            name_item.setFont(font)
            self.info_data.setItem(0, 0, name_item)

            max_item = QTableWidgetItem(str(max_value))
            max_item.setTextAlignment(QtCore.Qt.AlignCenter)
            max_item.setFont(font)
            self.info_data.setItem(1, 0, max_item)

            min_item = QTableWidgetItem(str(min_value))
            min_item.setTextAlignment(QtCore.Qt.AlignCenter)
            min_item.setFont(font)
            self.info_data.setItem(2, 0, min_item)

            mean_item = QTableWidgetItem(str(mean_value))
            mean_item.setTextAlignment(QtCore.Qt.AlignCenter)
            mean_item.setFont(font)
            self.info_data.setItem(3, 0, mean_item)

            stdev_item = QTableWidgetItem(str(stdev))
            stdev_item.setTextAlignment(QtCore.Qt.AlignCenter)
            stdev_item.setFont(font)
            self.info_data.setItem(4, 0, stdev_item)

            # output_action(self.filename_list[int(png_index)], self.file_path, tmpdirname)
            png_view_path = tmpdirname + '\\' + self.filename_list[int(png_index)] + '.png'
            # 将预览图显示到图床fits_graphicsView上
            self.fits_graphicsView.scene = QGraphicsScene()
            self.image = QPixmap()
            self.image.load(png_view_path)
            png_item = QGraphicsPixmapItem(self.image)
            self.fits_graphicsView.scene.addItem(png_item)
            self.fits_graphicsView.setScene(self.fits_graphicsView.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    data_disco = data_Disco()
    data_disco.show()
    sys.exit(app.exec_())
