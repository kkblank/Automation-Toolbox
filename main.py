'''
工具箱功能目录
'''
import json
import os
import sys
import time
import webbrowser
import numpy as np
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore
import main1,main2,main4,main5

'''全局变量'''
version_value = 0  # 验证是否联网变量
start_flag = False  # 是否能够运行程序标志
NAME = '4.3'  # 当前版本名称


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    '''切换窗口函数'''
    # 登录验证函数
    def log_in(self, func):
        global start_flag
        if start_flag is True:
            func()
        else:
            self.my_print('验证失败,程序即将在5秒后退出,请进行联网验证!')
            time.sleep(5)

    # 切换自动化界面
    def log1(self):
        self.w1 = main1.MyWindow1()
        self.w1.ui.show()
    def tow1(self):
        self.log_in(self.log1)

    # 切换图片处理界面
    def log2(self):
        self.w2 = main2.MyWindow2()
        self.w2.ui.show()
    def tow2(self):
        self.log_in(self.log2)

    # 关于我们
    def tow3(self):
        url = 'https://space.bilibili.com/2805045'
        webbrowser.open(url, new=2, autoraise=True)

    # 切换记忆搜索界面
    def log4(self):
        self.w4 = main4.MyWindow4()
        self.w4.ui.show()
    def tow4(self):
        self.log_in(self.log4)

    # 切换批量处理界面
    def log5(self):
        self.w5 = main5.MyWindow5()
        self.w5.ui.show()
    def tow5(self):
        self.log_in(self.log5)

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

    # 版本信息动作
    def version_action(self):
        self.text_are.setText('软件免费，感谢支持!')
        self.text_are.append('-正在请求联网验证-')
        self.text_are.append('-每日仅验证1次-')
        self.text_are.repaint()
        # 实例化联网认证信息，并且开启子线程
        self.my_thread4 = MyThread4()
        self.my_thread4.start()
        # 链接子线程传回的信号与主线程打印函数绑定
        self.my_thread4.textsignal.connect(self.my_print)

    # 打开使用手册
    def instructions_action(self):
        # 通过读取绝对路径的方式打开
        file = os.path.abspath('data') + '/使用手册.docx'
        os.startfile(file)

    '''主界面'''
    def sys_ui(self):
        global start_flag
        # 加载UI界面
        self.ui = uic.loadUi('./mini_main.ui')
        self.ui.setWindowTitle('自动化工具箱v{}'.format(NAME))

        # 主界面按钮
        self.bt6 = self.ui.pushButton_6  # 打开操作手册
        self.bt6.clicked.connect(self.instructions_action)

        self.text_are = self.ui.textBrowser  # 信息显示区域

        '''按钮功能'''
        # 打开自动化界面
        self.bt1 = self.ui.pushButton  # 自动化按钮
        self.bt1.clicked.connect(self.tow1)
        self.bt1.clicked.connect(self.ui.close)
        # 打开图像处理界面
        self.bt2 = self.ui.pushButton_2  # 图像处理按钮
        self.bt2.clicked.connect(self.tow2)
        self.bt2.clicked.connect(self.ui.close)
        # 打开捐赠通道界面
        self.bt3 = self.ui.pushButton_3  # 关于我们
        self.bt3.clicked.connect(self.tow3)
        # 打开记忆搜索界面
        self.bt4 = self.ui.pushButton_4  # 记忆搜索按钮
        self.bt4.clicked.connect(self.tow4)
        self.bt4.clicked.connect(self.ui.close)
        # 打开批量处理界面
        self.bt5 = self.ui.pushButton_5  # 批量处理按钮
        self.bt5.clicked.connect(self.tow5)
        self.bt5.clicked.connect(self.ui.close)
        # # 打开OCR识别界面
        # self.bt7 = self.ui.pushButton_7  # 批量处理按钮
        # self.bt7.clicked.connect(self.tow6)
        # self.bt7.clicked.connect(self.ui.close)

        self.version_action()  # 自动联网校正


# 请求网络验证的子线程
class MyThread4(QThread):
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global version_value
        # 设置一天只联网校正1次的逻辑，避免超过最大限制次数
        # 如果不存在配置文件，则进行1次联网校正
        f2 = os.path.exists('now_time.npy')
        if not f2:
            self.log_in()
        else:
            # 如果存在配置文件，则读取配置信息
            now_time = np.load('now_time.npy')
            now_data = time.localtime()
            now_data = np.array([now_data.tm_year, now_data.tm_mon, now_data.tm_mday])
            # 如果可以匹配则直接打印本地数据
            if np.all(now_time == now_data):
                tf = open("myDictionary.json", "r")
                data = json.load(tf)
                self.message = data['title']
                self.textsignal.emit(self.message)
                self.message = data['talk']
                self.textsignal.emit(self.message)
                version_value = data['version']
                tf.close()
            else:  # 时间戳不匹配则联网验证
                self.log_in()
        self.panduan_action()

    # 请求服务器响应的函数
    def log_in(self):
        global version_value
        try:
            # 请求服务器地址
            r = requests.post(
                url='https://f6949055554740a0b3384073fbe22f79.apig.cn-east-3.huaweicloudapis.com/log_test')
            # 拿到服务器的返回值，并转化成字典形式，并保存在本地
            tf = open("myDictionary.json", "w")
            json.dump(r.json(), tf)
            tf.close()
            # 保存本地时间戳
            t = time.localtime()
            t2 = np.array([t.tm_year, t.tm_mon, t.tm_mday])
            np.save('now_time', t2)
            # 传输打印信息
            self.message = r.json()['title']
            self.textsignal.emit(self.message)
            self.message = r.json()['talk']
            self.textsignal.emit(self.message)
            version_value = r.json()['version']
        except:  # 验证失败打印超时信息
            self.message = '联网验证超时，请检查网络!'
            self.textsignal.emit(self.message)

    # 判断函数(判断是否进行联网验证)
    def panduan_action(self):
        global start_flag
        if version_value == NAME:
            start_flag = True
            self.message = '-验证通过,欢迎使用-'
            self.textsignal.emit(self.message)
        elif version_value == 0:
            self.message = '请求超时，请先检查网络后重启软件.'
            self.textsignal.emit(self.message)
        else:
            self.message = '发现新版本为{}，请更新软件！'.format(version_value)
            self.textsignal.emit(self.message)
            self.message = '------------'
            self.textsignal.emit(self.message)
            self.message = '123网盘更新链接：https://www.123pan.com/s/R43eVv-5GdKd.html'
            self.textsignal.emit(self.message)
            self.message = '------------'
            self.textsignal.emit(self.message)
            self.message = '若您已更新最新版本，请忽略该提示。版本信息会在明日自动匹配。'
            self.textsignal.emit(self.message)
            # 不强制更新/此处设置为False则启用强制更新
            start_flag = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    sys.exit(app.exec_())