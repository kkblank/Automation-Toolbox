'''
记忆搜索界面
'''

import os
import pyperclip
import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore
import main

'''定义全局变量'''
inputWord = ""
DIC = {}  # 数字编号 int ：文件名 str


class MyWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    # 定义一个打印函数
    def my_print(self, str_text):
        self.text_are.append(str_text)
        self.text_are.repaint()

    # 点击记忆文件夹按钮动作
    def memory_action(self):
        self.open_memory = MyThread2()
        self.open_memory.start()

    # 点击确定按钮动作
    def ok_action(self):
        global inputWord
        inputWord = self.cmd_are.text()
        self.my_thread = MyThread()
        self.my_thread.start()
        self.my_thread.textsignal.connect(self.my_print)
        self.cmd_are.setText('')

    # 点击刷新动作
    def refresh_action(self):
        # 初始化刷新子线程
        self.out_are.setText('')
        self.text_are.setText('')
        self.my_thread3 = MyThread3()
        self.my_thread3.start()
        self.my_thread3.textsignal.connect(self.my_print)

    # 切换目录
    def tow(self):
        self.w1 = main.MyWindow()
        self.w1.ui.show()

    def sys_ui(self):
        self.ui = uic.loadUi('./mini_sys4.ui')
        self.ui.setWindowTitle('自动化工具箱v{}'.format(main.NAME))

        # 标题栏按钮
        self.mainWindow_bt = self.ui.pushButton_3
        self.mainWindow_bt.clicked.connect(self.tow)
        self.mainWindow_bt.clicked.connect(self.ui.close)

        # 记忆文件夹按钮/槽函数
        self.memory_bt = self.ui.pushButton
        self.memory_bt.clicked.connect(self.memory_action)
        # 文字显示区域
        self.text_are = self.ui.textBrowser
        # 粘贴测试区域
        self.out_are = self.ui.textEdit
        # 命令输入区域
        self.cmd_are = self.ui.lineEdit
        # 确定按钮/槽函数
        self.ok_bt = self.ui.pushButton_2
        self.ok_bt.clicked.connect(self.ok_action)
        # 刷新按钮/槽函数
        self.refresh_bt = self.ui.pushButton_4
        self.refresh_bt.clicked.connect(self.refresh_action)

        self.refresh_action()


# 主要执行子线程
class MyThread(QThread):
    # 设定一个传递文本信息的变量
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global DIC
        global inputWord
        try:
            int(inputWord)
        except:
            pass
        if inputWord.isdigit():
            # 纯数字，表示选定了
            inputNum = int(inputWord)
            if inputNum in DIC:
                self.getContentToClipboard(DIC[inputNum])
                self.message = '内容已经进入您的粘贴板!'
                self.textsignal.emit(self.message)
                self.message = '-------------------'
                self.textsignal.emit(self.message)
            else:
                self.message = '您输入的数字超出范围!'
                self.textsignal.emit(self.message)
                self.message = '-----------------'
                self.textsignal.emit(self.message)
        else:
            # 是正常的检索
            isFind = False
            for i, fileName in enumerate(os.listdir("data/memory")):
                if self.m1(inputWord.split(), fileName):
                    isFind = True
                    self.message = '{},{}'.format(str(i).zfill(4), fileName)
                    self.textsignal.emit(self.message)
                    self.message = '----------------'
                    self.textsignal.emit(self.message)
            if not isFind:
                self.message = '没有搜索到相关内容!'
                self.textsignal.emit(self.message)
                self.message = '----------------'
                self.textsignal.emit(self.message)

    def m1(self, arr, string) -> bool:
        """
        检测输入的关键词列表是否和 目标字符串匹配
        对于arr中的每一个小字符串，检测他们是否都是string的子串
        """
        return all(content in string for content in arr)

    def getContentToClipboard(self, fileName):
        """
        根据文件名，把文件名复制到粘贴板
        fileName: "xxx.txt"
        """
        with open(f"data/memory/{fileName}", encoding="utf-8") as f:
            content = f.read()
        pyperclip.copy(content)


# 记忆文件夹子线程
class MyThread2(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        path = os.path.abspath('data') + '/memory'
        os.startfile(path)


# 刷新按钮子线程
class MyThread3(QThread):
    # 设定一个传递文本信息的变量
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global DIC
        self.refreshDic()
        self.showList()
        self.message = '--------'
        self.textsignal.emit(self.message)
        self.message = '请输入搜索关键字，空格隔开，如果只输入数字表示选定'
        self.textsignal.emit(self.message)
        self.message = '-----------------'
        self.textsignal.emit(self.message)

    def refreshDic(self):
        """刷新操作，此操作影响全局变量dic"""
        # 初始化 dic
        global DIC
        DIC.clear()
        # enumerate,增加一个可迭代对象
        for i, fileName in enumerate(os.listdir("data/memory")):
            DIC[i] = fileName

    def showList(self):
        """展示列表"""
        for i, fileName in enumerate(os.listdir("data/memory")):
            self.message = '{},{}'.format(str(i).zfill(4), fileName)
            self.textsignal.emit(self.message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow4()
    w.ui.show()
    sys.exit(app.exec_())
