'''
作者界面
'''

import sys
import webbrowser

import cv2
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore

# import main


class MyWindow3(QMainWindow):

    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    ''' ui界面按钮动作函数'''
    # 选择捐赠通道动作
    def select_action(self, btn):
        pass
        # if btn.text() == '支付宝红包':
        #     if btn.isChecked():
        #         self.img_are.setPixmap(QPixmap('hb.png'))
        # elif btn.text() == '支付宝':
        #     if btn.isChecked():
        #         self.img_are.setPixmap(QPixmap('zfb.jpg'))
        # elif btn.text() == '微信':
        #     if btn.isChecked():
        #         self.img_are.setPixmap(QPixmap('wx.jpg'))

    # 打开作者主页动作
    def main_web_action(self):
        url = 'https://space.bilibili.com/2805045'
        webbrowser.open(url, new=2, autoraise=True)

    ''' ui显示界面'''
    def sys_ui(self):
        self.ui = uic.loadUi('./mini_sys3.ui')
        self.ui.setWindowTitle('自动化工具箱v{}'.format(main.NAME))

        # 标题栏按钮
        self.mainWindow_bt = self.ui.pushButton_4  # 返回目录界面按钮
        self.mainWindow_bt.clicked.connect(self.tow)  # 打开目录界面
        self.mainWindow_bt.clicked.connect(self.ui.close)  # 关闭原来窗口

        # 作者主页按钮
        self.main_web_bt = self.ui.pushButton
        self.main_web_bt.clicked.connect(self.main_web_action)

        # 捐赠图片显示区域(显示捐赠收款码)/没有槽函数
        self.img_are = self.ui.label_3
        # self.img_are.setPixmap(QPixmap('hb.png'))
        # 捐赠方式选择按钮
        self.select_bt = self.ui.radioButton  # 关闭
        self.select_bt2 = self.ui.radioButton_2  # 支付宝
        self.select_bt3 = self.ui.radioButton_3  # 微信
        # 设置默认选中按钮
        self.select_bt.setChecked(True)
        # 给捐赠选择按钮绑定槽函数
        self.select_bt.toggled.connect(lambda: self.select_action(self.select_bt))
        self.select_bt2.toggled.connect(lambda: self.select_action(self.select_bt2))
        self.select_bt3.toggled.connect(lambda: self.select_action(self.select_bt3))

    # 切换目录
    def tow(self):
        self.w1 = main.MyWindow()
        self.w1.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow3()
    w.ui.show()
    sys.exit(app.exec_())