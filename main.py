"""
工具箱功能目录
"""

import os
import sys
import time
import webbrowser
# from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import main1, main2, main4, main5

"""全局变量"""
version_value = 0  # 验证是否联网变量
start_flag = False  # 是否能够运行程序标志
NAME = "4.4"  # 当前版本名称


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    """切换窗口函数"""

    # 切换自动化界面
    def log1(self):
        self.w1 = main1.MyWindow1()
        self.w1.ui.show()

    # 切换图片处理界面
    def log2(self):
        self.w2 = main2.MyWindow2()
        self.w2.ui.show()

    # 关于我们
    def tow3(self):
        url = "https://space.bilibili.com/2805045"
        webbrowser.open(url, new=2, autoraise=True)

    # 切换记忆搜索界面
    def log4(self):
        self.w4 = main4.MyWindow4()
        self.w4.ui.show()

    # 切换批量处理界面
    def log5(self):
        self.w5 = main5.MyWindow5()
        self.w5.ui.show()

    # 文字识别(OCR)界面
    # def log6(self):
    #     self.w6 = main6.MyWindow6()
    #     self.w6.ui.show()
    # def tow6(self):
    #     self.log_in(self.log6)

    # 定义一个打印函数(打印子线程中传回来的信息)
    def my_print(self, str_text):
        self.text_are.append(str_text)
        self.text_are.repaint()

    # 打开使用手册
    def instructions_action(self):
        # 通过读取绝对路径的方式打开
        file = os.path.abspath("data") + "/使用手册.docx"
        os.startfile(file)

    """主界面"""

    def sys_ui(self):
        global start_flag
        # 加载UI界面
        self.ui = uic.loadUi("./mini_main.ui")
        self.ui.setWindowTitle("自动化工具箱v{}".format(NAME))

        # 主界面按钮
        self.bt6 = self.ui.pushButton_6  # 打开操作手册
        self.bt6.clicked.connect(self.instructions_action)

        self.text_are = self.ui.textBrowser  # 信息显示区域

        """按钮功能"""
        # 打开自动化界面
        self.bt1 = self.ui.pushButton  # 自动化按钮
        self.bt1.clicked.connect(self.log1)
        self.bt1.clicked.connect(self.ui.close)
        # 打开图像处理界面
        self.bt2 = self.ui.pushButton_2  # 图像处理按钮
        self.bt2.clicked.connect(self.log2)
        self.bt2.clicked.connect(self.ui.close)
        # 打开捐赠通道界面
        self.bt3 = self.ui.pushButton_3  # 关于我们
        self.bt3.clicked.connect(self.tow3)
        # 打开记忆搜索界面
        self.bt4 = self.ui.pushButton_4  # 记忆搜索按钮
        self.bt4.clicked.connect(self.log4)
        self.bt4.clicked.connect(self.ui.close)
        # 打开批量处理界面
        self.bt5 = self.ui.pushButton_5  # 批量处理按钮
        self.bt5.clicked.connect(self.log5)
        self.bt5.clicked.connect(self.ui.close)
        # # 打开OCR识别界面
        # self.bt7 = self.ui.pushButton_7  # 批量处理按钮
        # self.bt7.clicked.connect(self.tow6)
        # self.bt7.clicked.connect(self.ui.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    sys.exit(app.exec_())
