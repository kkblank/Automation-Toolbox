'''
自动化界面
'''

import sys, os
import time
import pyperclip
import xlrd
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore
import pyautogui as pg
import main

'''定义全局变量，用于部分情况下的灵活传参'''
key_num = 0  # 传递循环次数
version_value = 0  # 传递最新版本号
stop_flag = 1  # 全局的停止标志/1开始,0结束
step_flag = 0  # 单步调试指令行数
picture_file_name = 0  # 记录当前读取的是哪个图片文件夹
picture_check_speed = 1  # 图片检测的时间间隔
confidence = 75  # 图片检测的置信度


# 主线程(用于显示界面)
class MyWindow1(QMainWindow):
    # 初始化父类
    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    # 定义一个打印函数
    def my_print(self, str_text):
        self.text_are.append(str_text)
        self.text_are.repaint()

    # 读取cmd名称的函数
    def my_cmd_name(self, name):
        self.now_cmd_are.setText(name)
        self.text_are.repaint()

    '''ui界面按钮动作函数'''
    # 点击配置文件动作
    def peizhi_action(self):
        self.open_file = MyThread2()
        self.open_file.start()

    # 点击图片文件夹动作
    def picture_action(self):
        self.open_picture = MyThread3()
        self.open_picture.start()
        self.open_picture.textsignal.connect(self.my_print)

    # 点击开始按钮动作
    def start_action(self):
        global key_num
        global stop_flag
        global confidence

        stop_flag = 1
        confidence = self.confidence_are.value()

        key_num = self.input_are.text()
        self.my_thread = MyThread()
        # 开启子线程,并将循环次数key传过去
        self.my_thread.start()
        # 链接子线程传回的信号与主线程打印函数绑定
        self.my_thread.textsignal.connect(self.my_print)
        self.my_thread.textsignal2.connect(self.set_now_state)

    # 点击结束按钮动作
    def stop_action(self):
        global stop_flag
        stop_flag = 0

    # 点击鼠标定位按钮的动作
    def mouse_position_action(self):
        global stop_flag
        stop_flag = 1
        self.my_thread5 = MyThread5()
        # 开启子线程,并将循环次数key传过去
        self.my_thread5.start()
        self.my_thread5.textsignal.connect(self.my_print)

    # 图片检测速度选项
    def step_action(self):
        global step_flag
        step_flag = self.step_are.text()
        self.my_thread6 = MyThread6()
        # 开启子线程,并将循环次数key传过去
        self.my_thread6.start()
        self.my_thread6.textsignal.connect(self.my_print)
        self.my_thread6.textsignal2.connect(self.set_now_state)

    # 选择图片检测速度的快慢
    def select_action(self, btn):
        global picture_check_speed
        if btn.text() == '快':
            if btn.isChecked():
                picture_check_speed = 0.2
        elif btn.text() == '标准':
            if btn.isChecked():
                picture_check_speed = 1
        elif btn.text() == '慢':
            if btn.isChecked():
                picture_check_speed = 3

    # 设置软件运行的状态函数
    def set_now_state(self,text):
        self.now_state.setText(text)

    '''UI显示界面'''
    def sys_ui(self):
        # 加载UI界面
        self.ui = uic.loadUi('./mini_sys.ui')
        self.ui.setWindowTitle('自动化工具箱v{}'.format(main.NAME))
        # 初始化子线程的返回函数
        global version_value
        version_value = 0

        # 标题栏按钮
        self.mainWindow_bt = self.ui.pushButton_3  # 返回目录按钮
        self.mainWindow_bt.clicked.connect(self.tow)  # 打开目录界面
        self.mainWindow_bt.clicked.connect(self.ui.close)  # 关闭原来窗口

        # 图片检测时间选择按钮
        self.select_bt = self.ui.radioButton  # 快
        self.select_bt2 = self.ui.radioButton_2  # 标准
        self.select_bt3 = self.ui.radioButton_3  # 慢
        # 设置默认选中按钮
        self.select_bt2.setChecked(True)
        # 给检测时间按钮绑定槽函数
        self.select_bt.toggled.connect(lambda: self.select_action(self.select_bt))
        self.select_bt2.toggled.connect(lambda: self.select_action(self.select_bt2))
        self.select_bt3.toggled.connect(lambda: self.select_action(self.select_bt3))

        # 当前表格显示区域/子线程
        self.now_cmd_are = self.ui.lineEdit_3
        self.my_thread7 = MyThread7()
        self.my_thread7.start()
        self.my_thread7.textsignal.connect(self.my_cmd_name)
        # 图片相似度显示区域
        self.confidence_are = self.ui.spinBox

        # 配置文件按钮/槽函数
        self.peizhi_bt = self.ui.pushButton_2
        self.peizhi_bt.clicked.connect(self.peizhi_action)
        # 开始按钮/槽函数
        self.start_bt = self.ui.pushButton
        self.start_bt.clicked.connect(self.start_action)
        # 文本显示窗口(显示打印信息)/没有槽函数
        self.text_are = self.ui.textBrowser
        self.text_are.setText('---自动化操作---')
        # 输入窗口(输入循环次数)/没有槽函数
        self.input_are = self.ui.lineEdit
        # 图片文件夹按钮/槽函数
        self.picture_bt = self.ui.pushButton_4
        self.picture_bt.clicked.connect(self.picture_action)
        # 设置结束按钮/槽函数
        self.stop_bt = self.ui.pushButton_6
        self.stop_bt.clicked.connect(self.stop_action)
        # 鼠标定位按钮/槽函数
        self.mouse_position_bt = self.ui.pushButton_7
        self.mouse_position_bt.clicked.connect(self.mouse_position_action)
        # 单步调试按钮/槽函数
        self.step_are = self.ui.lineEdit_2
        self.step_bt = self.ui.pushButton_5
        self.step_bt.clicked.connect(self.step_action)

        # 当前运行状态显示区域
        self.now_state = self.ui.label_6

    # 切换目录
    def tow(self):
        self.w1 = main.MyWindow()
        self.w1.ui.show()


# 用于自动化操作的子线程
class MyThread(QThread):
    # 设置鼠标按键类型参数
    mouse_type = ['空', 'left', 'middle', 'right']
    # 设定传递文本信息的变量
    textsignal = pyqtSignal(str)  # 文本显示区域信息
    textsignal2 = pyqtSignal(str)  # 当前运行状态信息

    def __init__(self):
        super().__init__()

    def run(self):
        global stop_flag
        global picture_file_name
        self.message = '配置文件检索完毕,开始执行程序.'
        self.textsignal.emit(self.message)
        file = 'data/配置文件.xls'
        # 打开文件
        cmd_file = xlrd.open_workbook(filename=file)
        # 通过索引获取sheet表格,默认只获取第一个表格.sheet[0][1]可以取出对应行列的数据
        sheet1 = cmd_file.sheet_by_index(0)
        # 从主线程传过来的循环次数参数key
        key = key_num  # 字符串形式

        # 判断路径图片文件夹是否存在
        if sheet1.row_values(rowx=1)[0] == '':
            picture_file_name = 0
        else:
            picture_file_name = sheet1.row_values(rowx=1)[0]
        path = os.path.abspath('data')
        fg = os.path.exists('{}/{}'.format(path, picture_file_name))
        if fg: # 如果路径存在文件夹
            if key == '0':  # 循环执行并计数
                i = 1
                self.message = '您选择了循环到死,程序已经开始执行.'
                self.textsignal.emit(self.message)
                while True:
                    if stop_flag == 1:
                        self.message = '当前为第{}次执行'.format(i)
                        self.textsignal.emit(self.message)
                        self.main_work(sheet1)
                        i = i + 1
                        time.sleep(1)
                    else:
                        self.message = '程序已退出！'
                        self.textsignal.emit(self.message)

                        self.message = '就绪.'
                        self.textsignal2.emit(self.message)
                        break
            else:  # 执行到最大次数的分支
                i = 1
                self.message = '当前程序最大执行次数为{}次,程序已经开始执行.'.format(int(key))
                self.textsignal.emit(self.message)
                while int(key) >= i:
                    if stop_flag == 1:
                        self.message = '当前为第{}次执行'.format(i)
                        self.textsignal.emit(self.message)
                        self.main_work(sheet1)
                        i = i + 1
                        time.sleep(1)
                    else:
                        self.message = '程序已退出！'
                        self.textsignal.emit(self.message)

                        self.message = '就绪.'
                        self.textsignal2.emit(self.message)
                        break
                else:
                    self.message = '就绪.'
                    self.textsignal2.emit(self.message)
        else: # 如果路劲不存在文件夹
            self.message = '路径图片文件夹不存在，请检查.'
            self.textsignal.emit(self.message)

    # 主要工作函数
    def main_work(self, sheet1):
        global stop_flag
        global picture_file_name
        max_rows = sheet1.nrows  # 读取表格的行数
        n = 2  # 从第二行第一列开始读取(排除表头)
        while n <= max_rows - 1:
            # 打印当前运行状态
            self.message = '第{}行命令运行中...'.format(n+1)
            self.textsignal2.emit(self.message)

            if stop_flag == 1:
                # 读取当前行的信息
                tab_value = sheet1.row_values(rowx=n)
                # 1.鼠标点击图片
                if tab_value[1] == '图片':
                    img_dir = 'data/{}/{}'.format(picture_file_name,tab_value[2])  # 拿到具体图片名称地址
                    self.mouse_click(img_dir, self.mouse_type[int(tab_value[3])], int(tab_value[4]), tab_value[5])
                # 2.鼠标点击坐标位置
                elif tab_value[1] == '坐标':
                    self.mouse_position(tab_value[2], self.mouse_type[int(tab_value[3])], int(tab_value[4]),
                                        tab_value[5])
                # 3.鼠标拖拽操作
                elif tab_value[1] == '拖拽':
                    self.mouse_drag(tab_value[2], tab_value[4])
                # 4.
                elif tab_value[1] == '长按':
                    self.mouse_long_push(self.mouse_type[int(tab_value[3])], tab_value[5])
                # 5.鼠标滚动操作
                elif tab_value[1] == '滚动':
                    self.mouse_scroll(tab_value[6])
                # 6.键盘操作
                elif tab_value[1] == '键盘':
                    self.key_board(int(tab_value[7]), tab_value[8], tab_value[9])
                else:  # 出现错误时跳出执行
                    self.message = '第{}行判断标志错误,请修正!'.format(n + 1)
                    self.textsignal.emit(self.message)
                    break
                n = n + 1
            else:
                self.message = '---命令执行完毕!---'
                self.textsignal.emit(self.message)
                break
        else:
            self.message = '---命令执行完毕!---'
            self.textsignal.emit(self.message)

    '''
    键鼠操作
    img:表示图片地址,需要点击的位置,用图片定位方式 
    button_type:表示点击鼠标的哪个按钮(左中右) 
    clicks_time:代表点击次数
    '''
    # 1.定义鼠标点击图片
    def mouse_click(self, img, button_type, clicks_time, wait_time):
        global stop_flag
        global picture_check_speed
        global confidence

        if wait_time == '':
            wait_time = 0
        else:
            wait_time = int(wait_time)
        t = 0
        while True:
            if stop_flag == 1:
                location = pg.locateCenterOnScreen(img, confidence=confidence/100)
                if location is not None:
                    pg.moveTo(location.x, location.y, duration=0.2)
                    pg.click(clicks=clicks_time, interval=0.1, button=button_type)
                    time.sleep(0.5)
                    break
                # else:  # 打印正在检测图片信息
                #     name = img.split('/')
                #     self.message = '...正在检测"{}"...'.format(name[-1])
                #     self.textsignal.emit(self.message)
                time.sleep(picture_check_speed)
                t = t + picture_check_speed
                if wait_time != 0:
                    if t >= int(wait_time):
                        self.message = '.指令等待时间结束,未检测到该图片.'
                        self.textsignal.emit(self.message)
                        break
            else:
                break

    # 2.定义鼠标点击坐标位置
    def mouse_position(self, position, button_type, clicks_time, wait_time):
        global stop_flag
        if wait_time == '':
            wait_time = 0
        else:
            wait_time = int(wait_time)
            self.message = '正在等待点击...'
            self.textsignal.emit(self.message)
        # 休眠时间判断
        for i in range(wait_time):
            if stop_flag == 1:
                time.sleep(1)
            else:
                break
        if stop_flag == 1:
            position = position.split('/')
            pg.moveTo(int(position[0]), int(position[1]), duration=0.2)
            pg.click(clicks=clicks_time, interval=0.1, button=button_type)
            self.message = '-点击坐标({},{})完毕-'.format(position[0],position[1])
            self.textsignal.emit(self.message)
            time.sleep(0.5)
        else:
            return 0

    # 3.定义鼠标拖拽(只需要开始/结束两个位置)
    def mouse_drag(self, start_position, end_position):
        start_position = start_position.split('/')
        end_position = end_position.split('/')
        pg.moveTo(int(start_position[0]),int(start_position[1]), duration=0.2)
        pg.mouseDown()
        pg.moveTo(int(end_position[0]), int(end_position[1]), duration=0.5)
        pg.mouseUp()
        self.message = '-拖拽完毕-'
        self.textsignal.emit(self.message)
        time.sleep(0.5)

    # 4.鼠标长按（类型/时长）
    def mouse_long_push(self, button_type, push_time):
        global stop_flag
        if push_time == '':
            push_time = 0
        else:
            push_time = int(push_time)
        self.message = '-长按鼠标-'
        self.textsignal.emit(self.message)
        pg.mouseDown(button=button_type)
        # 判断长按时间
        for i in range(push_time):
            if stop_flag == 1:
                time.sleep(1)
            else:
                break
        pg.mouseUp()

    # 5.定义滚轮滑动事件
    def mouse_scroll(self, dist):
        pg.scroll(int(dist))
        self.message = '当前滚动距离为:{}'.format(dist)
        self.textsignal.emit(self.message)
        time.sleep(0.5)

    # 6.定义键盘输入事件
    '''
    value:表示需要输入的值
    type:表示操作类型
    time:表示长按时长
    '''
    def key_board(self, bt_type, value, bt_time):
        if bt_type == 0:  # 文本输入
            pyperclip.copy(value)
            pg.hotkey('ctrl', 'v')
            self.message = '-输入文本完毕-'
            self.textsignal.emit(self.message)
            time.sleep(0.5)
        elif bt_type == 1:  # 单独热键
            # 缺省值时点按
            if bt_time == '' or bt_time == '0':
                pg.hotkey(value)
                self.message = '-点击键盘:{}-'.format(value)
                self.textsignal.emit(self.message)
            # 有数字时长按
            else:
                self.message = '-按住键盘:{}-'.format(value)
                self.textsignal.emit(self.message)
                pg.keyDown(value)
                for i in range(int(bt_time)):
                    if stop_flag == 1:
                        time.sleep(1)
                    else:
                        break
                pg.keyUp(value)
            time.sleep(0.5)
        elif bt_type == 2:  # 2键组合
            temp = value.split('/')
            pg.hotkey(temp[0], temp[1])
            self.message = '-点击2键组合-'
            self.textsignal.emit(self.message)
            time.sleep(0.5)
        elif bt_type == 3:  # 3键组合
            temp = value.split('/')
            pg.hotkey(temp[0], temp[1], temp[2])
            self.message = '-点击3键组合-'
            self.textsignal.emit(self.message)
            time.sleep(0.5)
        else:
            self.message = '-键盘没有对应的动作,请检查命令行-'
            self.textsignal.emit(self.message)
            time.sleep(0.5)


# 打开配置文件的子线程
class MyThread2(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        # 通过读取绝对路径的方式打开
        path = os.path.abspath('data') + '/配置文件.xls'
        os.startfile(path)


# 打开图片文件夹的子线程
class MyThread3(QThread):
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global picture_file_name
        try:
            path = os.path.abspath('data')
            os.startfile('{}/{}'.format(path, picture_file_name))
            self.message = '-打开文件夹成功-'
            self.textsignal.emit(self.message)
        except:
            self.message = '-文件夹不存在，请检查-'
            self.textsignal.emit(self.message)


# 鼠标坐标定位的子线程
class MyThread5(QThread):
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        self.message = '-复制坐标时请不要复制括号-'
        self.textsignal.emit(self.message)
        while stop_flag == 1:
            time.sleep(1)
            x, y = pg.position()
            self.message = '当前坐标为（{}/{}）'.format(x, y)
            self.textsignal.emit(self.message)
        else:
            self.message = '-停止检测坐标-'
            self.textsignal.emit(self.message)


# 单步调试的子线程
class MyThread6(MyThread):
    # textsignal2 = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        self.message = '.2s后开始单步调试.'
        self.textsignal.emit(self.message)

        self.message = '.单步调试中.'
        self.textsignal2.emit(self.message)

        time.sleep(2)
        file = 'data/配置文件.xls'
        # 打开文件
        cmd_file = xlrd.open_workbook(filename=file)
        # 通过索引获取sheet表格,默认只获取第一个表格.sheet[0][1]可以取出对应行列的数据
        sheet1 = cmd_file.sheet_by_index(0)

        # 判断是否存在对应的图片文件夹
        global picture_file_name
        if sheet1.row_values(rowx=1)[0] == '':
            picture_file_name = 0
        else:
            picture_file_name = sheet1.row_values(rowx=1)[0]
        path = os.path.abspath('data')
        fg = os.path.exists('{}/{}'.format(path, picture_file_name))
        if fg: # 如果路径存在文件夹
            self.main_work(sheet1)
            self.message = '.单步调试结束.'
            self.textsignal.emit(self.message)

            self.message = '就绪.'
            self.textsignal2.emit(self.message)
        else: # 如果不存在对应文件夹
            self.message = '不存在对应的图片文件夹，请检查.'
            self.textsignal.emit(self.message)

            self.message = '.就绪.'
            self.textsignal2.emit(self.message)

    def main_work(self, sheet1):
        global step_flag
        global picture_file_name
        try:
            n = int(step_flag) - 1
            # 读取当前行的信息
            tab_value = sheet1.row_values(rowx=n)
            # 1.鼠标点击图片
            if tab_value[1] == '图片':
                img_dir = 'data/{}/{}'.format(picture_file_name, tab_value[2])  # 拿到具体图片名称地址
                self.mouse_click(img_dir, self.mouse_type[int(tab_value[3])], int(tab_value[4]), tab_value[5])
            # 2.鼠标点击坐标位置
            elif tab_value[1] == '坐标':
                self.mouse_position(tab_value[2], self.mouse_type[int(tab_value[3])], int(tab_value[4]),
                                    tab_value[5])
            # 3.鼠标拖拽操作
            elif tab_value[1] == '拖拽':
                self.mouse_drag(tab_value[2], tab_value[4])
            # 4.
            elif tab_value[1] == '长按':
                self.mouse_long_push(self.mouse_type[int(tab_value[3])], tab_value[5])
            # 5.鼠标滚动操作
            elif tab_value[1] == '滚动':
                self.mouse_scroll(tab_value[6])
            # 6.键盘操作
            elif tab_value[1] == '键盘':
                self.key_board(int(tab_value[7]), tab_value[8], tab_value[9])
            else:  # 出现错误时跳出执行
                self.message = '第{}行判断标志错误,请修正!'.format(n+1)
                self.textsignal.emit(self.message)
        except:
            self.message = '当前行指令行不存在或有误，请检查。'
            self.textsignal.emit(self.message)


# 读取表格名称的子线程
class MyThread7(QThread):
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global picture_file_name
        file = 'data/配置文件.xls'
        # 打开文件
        cmd_file = xlrd.open_workbook(filename=file)
        sheet1 = cmd_file.sheet_by_index(0)
        picture_file_name = sheet1.row_values(rowx=1)[0]

        self.message = cmd_file.sheet_names()[0]
        self.textsignal.emit(self.message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow1()
    w.ui.show()
    sys.exit(app.exec_())
