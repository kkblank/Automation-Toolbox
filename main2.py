'''
图像变换界面
'''

import os
import sys
import cv2
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore

import main

'''定义全局变量，用于参数灵活传递'''
global suanfa_value  # 传递算法类型


class MyWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    # 定义一个打印函数
    def my_print(self, str_text):
        self.text_are.append(str_text)
        self.text_are.repaint()

    '''UI界面动作函数'''
    # 选择算法通道动作
    def suanfa_action(self, btn):
        global suanfa_value
        if btn.text() == '均衡':
            if btn.isChecked():
                suanfa_value['sf'] = '均衡'
        elif btn.text() == '质量':
            if btn.isChecked():
                suanfa_value['sf'] = '质量'
        else:
            if btn.isChecked():
                suanfa_value['sf'] = '快速'

    # 选择颜色通道的动作
    def color_action(self, btn):
        global suanfa_value
        if btn.text() == '彩色':
            if btn.isChecked():
                suanfa_value['ys'] = '彩色'
        if btn.text() == '黑白':
            if btn.isChecked():
                suanfa_value['ys'] = '黑白'

    # 点击图片文件夹动作
    def picture_action(self):
        self.open_picture = MyThread3()
        self.open_picture.start()

    # 点击重设图像按钮的动作
    def resize_picture_action(self):
        global suanfa_value
        # 读取xy坐标
        suanfa_value['x'] = self.picture_size_x.text()
        suanfa_value['y'] = self.picture_size_y.text()
        # 打开对话框,选择要转换的图片,并存储路径传递给子线程进行处理
        root = tk.Tk()
        root.withdraw()
        suanfa_value['path'] = filedialog.askopenfilename()
        # 开启图片处理子线程
        self.my_thread5 = MyThread5()
        self.my_thread5.start()
        self.my_thread5.textsignal.connect(self.my_print)

    '''UI显示界面'''
    def sys_ui(self):
        # 初始化全局变量
        global suanfa_value
        suanfa_value = {'sf': '均衡', 'path': '', 'x': '1080', 'y': '720', 'ys': '彩色'}

        self.ui = uic.loadUi('./mini_sys2.ui')
        self.ui.setWindowTitle('自动化工具箱v{}'.format(main.NAME))

        # 标题栏按钮
        self.mainWindow_bt = self.ui.pushButton_4  # 返回目录界面按钮
        self.mainWindow_bt.clicked.connect(self.tow)  # 打开目录界面
        self.mainWindow_bt.clicked.connect(self.ui.close)  # 关闭原来窗口

        # 文本显示窗口(显示打印信息)/没有槽函数
        self.text_are = self.ui.textBrowser
        self.text_are.setText('---欢迎使用图像处理功能---')

        # 图片文件夹2按钮/槽函数
        self.picture_bt = self.ui.pushButton
        self.picture_bt.clicked.connect(self.picture_action)
        # 重设图片大小按钮/槽函数
        self.resize_picture_bt = self.ui.pushButton_3
        self.resize_picture_bt.clicked.connect(self.resize_picture_action)
        # 读取图像分辨率区域/没有槽函数
        self.picture_size_x = self.ui.lineEdit_2  # x坐标
        self.picture_size_y = self.ui.lineEdit_3  # y坐标

        # 插值算法选择按钮
        self.select_bt = self.ui.radioButton  # 快速
        self.select_bt2 = self.ui.radioButton_2  # 均衡
        self.select_bt3 = self.ui.radioButton_3  # 质量
        # 图像色彩选择按钮
        self.select_bt4 = self.ui.radioButton_4  # 彩色
        self.select_bt5 = self.ui.radioButton_5  # 黑白

        # 给按钮进行分组
        self.color_group = QButtonGroup()  # 颜色组
        self.color_group.addButton(self.select_bt4)
        self.color_group.addButton(self.select_bt5)
        self.suanfa_group = QButtonGroup()  # 算法选择组
        self.suanfa_group.addButton(self.select_bt)
        self.suanfa_group.addButton(self.select_bt2)
        self.suanfa_group.addButton(self.select_bt3)
        # 设置默认选中均衡按钮
        self.select_bt2.setChecked(True)
        self.select_bt4.setChecked(True)
        # 给算法选择按钮绑定槽函数
        self.select_bt.toggled.connect(lambda: self.suanfa_action(self.select_bt))
        self.select_bt2.toggled.connect(lambda: self.suanfa_action(self.select_bt2))
        self.select_bt3.toggled.connect(lambda: self.suanfa_action(self.select_bt3))
        self.select_bt4.toggled.connect(lambda: self.color_action(self.select_bt4))
        self.select_bt5.toggled.connect(lambda: self.color_action(self.select_bt5))

    # 切换目录
    def tow(self):
        self.w1 = main.MyWindow()
        self.w1.ui.show()


# 打开图片文件夹2的子线程
class MyThread3(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        path = os.path.abspath('data') + '/picture2'
        os.startfile(path)


# 图像处理的子线程
class MyThread5(QThread):
    global suanfa_value
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        # 初始化一个算法查询字典
        color_dict = {'彩色':'1', '黑白':'0'}
        color = color_dict[suanfa_value['ys']]
        suanfa_dict = {'快速':'0', '均衡':'1', '质量':'2'}
        inter = suanfa_dict[suanfa_value['sf']]
        # 对新的图片名称进行处理
        picture_name = suanfa_value['path'].split('/')[-1].split('.')[0]
        picture_name2 = 'data/picture2/'+ picture_name + '-1' + '.png'
        # 判断是倍数还是像素
        npx = suanfa_value['x'].split('/')
        npy = suanfa_value['y'].split('/')
        try:  # 读取路径,放在try里面防止出现非法字符(中文)
            img = cv2.imread('{}'.format(suanfa_value['path']), int(color))
            # 判断是倍数还是像素
            if npx[-1] == 'n' and npy[-1] == 'n':
                img2 = cv2.resize(img, dsize=None, fx=float(npx[0]), fy=float(npy[0]), interpolation=int(inter))
            else:
                img2 = cv2.resize(img, (int(suanfa_value['x']),int(suanfa_value['y'])), interpolation=int(inter))
            cv2.imwrite(picture_name2, img2)
            self.message = '-转换成功,请打开图片文件夹2查看!-'
            self.textsignal.emit(self.message)
        except:
            self.message = '-读取失败，请确认图片格式是否为jpg/png等常见格式-'
            self.textsignal.emit(self.message)
            self.message = '-路径中是否出现中文或其他非法字符,请移动到全英文路径再试!-'
            self.textsignal.emit(self.message)
            self.message = '-请检查缩放倍数格式是否填写正确!-'
            self.textsignal.emit(self.message)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    w = MyWindow2()  # 实例化类
    w.ui.show()  # 展示窗口
    sys.exit(app.exec_())  # 保持窗口