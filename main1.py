'''
自动化界面
'''

import sys, os
import time
import datetime
import pyperclip
import xlrd
from PySide6.QtCore import QThread, Signal, Qt, QDateTime
from PySide6.QtWidgets import *
from generated.ui_auto import Ui_AutoWindow
import pyautogui as pg
from pyautogui import ImageNotFoundException as PgImageNotFoundException
import main

'''定义全局变量，用于部分情况下的灵活传参'''
key_num = 0  # 传递循环次数
version_value = 0  # 传递最新版本号
# stop_flag 已废弃，改用 QThread.requestInterruption()
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
        self.setWindowFlags(Qt.WindowCloseButtonHint)

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
        global confidence

        confidence = self.similarity_slider.value()

        key_num = self.input_are.text()
        self.now_state.setText('运行中')
        self.my_thread = MyThread()
        self.my_thread.start_time = self.dtEdit_start.dateTime().toPython()
        # 结束时间：勾选了才启用，且不能小于开始时间
        if self.end_time_check.isChecked():
            edt = self.dtEdit_end.dateTime()
            if edt <= self.dtEdit_start.dateTime():
                self.my_print('错误:结束时间必须大于开始时间!')
                self.now_state.setText('就绪')
                return
            self.my_thread.end_time = edt.toPython()
        else:
            self.my_thread.end_time = None
        # 开启子线程,并将循环次数key传过去
        self.my_thread.start()
        # 链接子线程传回的信号与主线程打印函数绑定
        self.my_thread.textsignal.connect(self.my_print)
        self.my_thread.textsignal2.connect(self.set_now_state)

    # 点击结束按钮动作
    def stop_action(self):
        if hasattr(self, 'my_thread') and self.my_thread.isRunning():
            self.my_thread.requestInterruption()
        if hasattr(self, 'my_thread5') and self.my_thread5.isRunning():
            self.my_thread5.requestInterruption()
        self.now_state.setText('就绪')

    # 点击鼠标定位按钮的动作
    def mouse_position_action(self):
        self.now_state.setText('鼠标坐标定位中')
        self.my_thread5 = MyThread5()
        # 开启子线程,并将循环次数key传过去
        self.my_thread5.start()
        self.my_thread5.textsignal.connect(self.my_print)
        self.my_thread5.textsignal2.connect(self.set_now_state)

    # 图片检测速度选项
    def step_action(self):
        global step_flag
        step_flag = self.step_are.text()
        self.my_thread6 = MyThread6()
        # 开启子线程,并将循环次数key传过去
        self.my_thread6.start()
        self.my_thread6.textsignal.connect(self.my_print)
        self.my_thread6.textsignal2.connect(self.set_now_state)
        self.now_state.setText('单步调试中')

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

    # 图片相似度滑块改变的回调
    def on_similarity_changed(self, val):
        self.similarity_value.setText(str(val))
        global confidence
        confidence = val

    # 结束时间勾选开关
    def toggle_end_time(self, checked):
        self.dtEdit_end.setEnabled(checked)

    # 设置软件运行的状态函数
    def set_now_state(self,text):
        self.now_state.setText(text)

    '''UI显示界面'''
    def sys_ui(self):
        # 加载UI界面
        self.ui = Ui_AutoWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('自动化工具箱v{}'.format(main.NAME))
        self.resize(600, 490)
        # 初始化子线程的返回函数
        global version_value
        version_value = 0

        # ── 顶部工具栏 ──
        self.mainWindow_bt = self.ui.pushButton_3  # 返回目录
        self.mainWindow_bt.setGeometry(30, 10, 93, 28)
        self.mainWindow_bt.clicked.connect(self.tow)
        self.mainWindow_bt.clicked.connect(self.close)

        self.ui.label_4.setGeometry(280, 10, 101, 16)  # 图片检测速度：
        self.select_bt = self.ui.radioButton  # 快
        self.select_bt.setGeometry(390, 10, 41, 19)
        self.select_bt2 = self.ui.radioButton_2  # 标准
        self.select_bt2.setGeometry(440, 10, 61, 19)
        self.select_bt3 = self.ui.radioButton_3  # 慢
        self.select_bt3.setGeometry(510, 10, 41, 20)
        self.select_bt2.setChecked(True)
        self.select_bt.toggled.connect(lambda: self.select_action(self.select_bt))
        self.select_bt2.toggled.connect(lambda: self.select_action(self.select_bt2))
        self.select_bt3.toggled.connect(lambda: self.select_action(self.select_bt3))

        # ── 日志区域 ──
        self.text_are = self.ui.textBrowser
        self.text_are.setGeometry(25, 60, 281, 325)
        self.text_are.setText('---自动化操作---')

        # ── 右侧控制面板（x≥330） ──
        # 第1行：当前表格
        self.ui.label_3.setGeometry(330, 38, 61, 16)  # 当前表格
        self.now_cmd_are = self.ui.lineEdit_3
        self.now_cmd_are.setGeometry(395, 36, 81, 21)
        self.my_thread7 = MyThread7()
        self.my_thread7.start()
        self.my_thread7.textsignal.connect(self.my_cmd_name)

        # 第2行：开始时间
        self.label_start_time = QLabel('开始时间：', self)
        self.label_start_time.setGeometry(330, 65, 61, 16)
        self.dtEdit_start = QDateTimeEdit(self)
        self.dtEdit_start.setGeometry(395, 63, 190, 22)
        self.dtEdit_start.setDisplayFormat('yyyy:MM:dd:HH:mm:ss')
        self.dtEdit_start.setDateTime(QDateTime.currentDateTime())

        # 第3行：结束时间 + 启用勾选
        self.label_end_time = QLabel('结束时间：', self)
        self.label_end_time.setGeometry(330, 93, 61, 16)
        self.dtEdit_end = QDateTimeEdit(self)
        self.dtEdit_end.setGeometry(395, 91, 175, 22)
        self.dtEdit_end.setDisplayFormat('yyyy:MM:dd:HH:mm:ss')
        self.dtEdit_end.setDateTime(QDateTime.currentDateTime())
        self.end_time_check = QCheckBox(self)
        self.end_time_check.setGeometry(575, 91, 22, 22)
        self.end_time_check.setChecked(False)
        self.end_time_check.toggled.connect(self.toggle_end_time)
        self.dtEdit_end.setEnabled(False)

        # 第4行：循环次数
        self.ui.label.setGeometry(340, 125, 72, 15)  # 循环次数：
        self.input_are = self.ui.lineEdit
        self.input_are.setGeometry(416, 125, 91, 21)

        # 第5行：图片相似度（滑块）
        self.ui.label_7.setGeometry(330, 152, 81, 16)  # 图片相似度：
        self.similarity_value = QLineEdit(self)
        self.similarity_value.setGeometry(415, 150, 35, 22)
        self.similarity_value.setReadOnly(True)
        self.similarity_value.setText('75')
        self.similarity_value.setAlignment(Qt.AlignCenter)
        self.similarity_slider = QSlider(Qt.Horizontal, self)
        self.similarity_slider.setGeometry(460, 150, 130, 22)
        self.similarity_slider.setRange(0, 100)
        self.similarity_slider.setValue(75)
        self.similarity_slider.setSingleStep(1)
        self.similarity_slider.valueChanged.connect(self.on_similarity_changed)

        # 按钮第1行：开始 / 结束
        self.start_bt = self.ui.pushButton
        self.start_bt.setGeometry(330, 190, 93, 51)
        self.start_bt.clicked.connect(self.start_action)
        self.stop_bt = self.ui.pushButton_6
        self.stop_bt.setGeometry(450, 190, 93, 51)
        self.stop_bt.clicked.connect(self.stop_action)

        # 按钮第2行：图片文件夹 / 配置文件
        self.picture_bt = self.ui.pushButton_4
        self.picture_bt.setGeometry(330, 260, 93, 51)
        self.picture_bt.clicked.connect(self.picture_action)
        self.peizhi_bt = self.ui.pushButton_2
        self.peizhi_bt.setGeometry(450, 260, 93, 51)
        self.peizhi_bt.clicked.connect(self.peizhi_action)

        # 按钮第3行：鼠标定位 / 单步调试
        self.mouse_position_bt = self.ui.pushButton_7
        self.mouse_position_bt.setGeometry(330, 330, 93, 51)
        self.mouse_position_bt.clicked.connect(self.mouse_position_action)
        self.step_bt = self.ui.pushButton_5
        self.step_bt.setGeometry(450, 330, 93, 51)
        self.step_bt.clicked.connect(self.step_action)

        # 第6行：指令行数
        self.ui.label_2.setGeometry(340, 400, 72, 15)  # 指令行数：
        self.step_are = self.ui.lineEdit_2
        self.step_are.setGeometry(450, 400, 91, 21)

        # ── 底部状态 ──
        self.ui.label_5.setGeometry(30, 445, 71, 16)  # 当前状态：
        self.now_state = self.ui.label_6
        self.now_state.setGeometry(110, 445, 191, 16)
        self.now_state.setText('就绪')
        # 隐藏旧的浮动控件
        self.ui.spinBox.hide()
        self.ui.label_8.hide()

    # 切换目录
    def tow(self):
        self.w1 = main.MyWindow()
        self.w1.show()

# 用于自动化操作的子线程
class MyThread(QThread):
    # 设置鼠标按键类型参数
    mouse_type = ['空', 'left', 'middle', 'right']
    # 设定传递文本信息的变量
    textsignal = Signal(str)  # 文本显示区域信息
    textsignal2 = Signal(str)  # 当前运行状态信息
    # 指令分发字典
    CMD_DISPATCH = {
        '图片': 'do_mouse_click',
        '坐标': 'do_mouse_position',
        '拖拽': 'do_mouse_drag',
        '长按': 'do_mouse_long_push',
        '滚动': 'do_mouse_scroll',
        '键盘': 'do_key_board',
    }

    def __init__(self):
        super().__init__()
        self.jump_map = {}
        self.label_map = {}
        self.call_stack = []
        self.start_time = None
        self.end_time = None

    @staticmethod
    def build_jump_map(sheet1):
        """预扫描表格,建立IF/ELSE/ENDIF的跳转映射表"""
        stack = []
        jump_map = {}
        max_rows = sheet1.nrows
        for n in range(max_rows):
            tab_value = sheet1.row_values(rowx=n)
            instr = tab_value[1] if len(tab_value) > 1 else ''
            if instr == 'IF':
                stack.append({'if_row': n, 'else_row': None})
            elif instr == 'ELSE':
                if stack:
                    stack[-1]['else_row'] = n
            elif instr == 'ENDIF':
                if stack:
                    item = stack.pop()
                    jump_map[item['if_row']] = (item['else_row'], n)
        return jump_map

    @staticmethod
    def build_label_map(sheet1):
        """预扫描表格,建立LABEL的名称到行号映射"""
        label_map = {}
        max_rows = sheet1.nrows
        for n in range(max_rows):
            tab_value = sheet1.row_values(rowx=n)
            instr = tab_value[1] if len(tab_value) > 1 else ''
            if instr == 'LABEL':
                name = tab_value[2] if len(tab_value) > 2 else ''
                if name:
                    label_map[name] = n
        return label_map

    def wait_for_image_condition(self, img, timeout):
        """等待图片出现在屏幕上,超时返回False。返回True表示找到图片"""
        global picture_check_speed
        global confidence
        if timeout == '' or timeout == 0:
            timeout = 3
        timeout = float(timeout)
        t = 0
        while t < timeout:
            if not self.isInterruptionRequested():
                try:
                    location = pg.locateCenterOnScreen(img, confidence=confidence/100)
                    if location is not None:
                        return True
                except Exception:
                    pass
                time.sleep(picture_check_speed)
                t += picture_check_speed
            else:
                return False
        return False

    def run(self):
        try:
            global picture_file_name
            self.message = '配置文件检索完毕,开始执行程序.'
            self.textsignal.emit(self.message)
            self.message = '运行中.'
            self.textsignal2.emit(self.message)
            # 定时等待：如果 start_time 在未来，则等待
            if self.start_time and self.start_time > datetime.datetime.now():
                self.message = '定时等待中,开始时间为: {}'.format(self.start_time.strftime('%Y:%m:%d %H:%M:%S'))
                self.textsignal.emit(self.message)
                while self.start_time > datetime.datetime.now():
                    if self.isInterruptionRequested():
                        self.message = '定时任务已取消.'
                        self.textsignal.emit(self.message)
                        self.message = '就绪.'
                        self.textsignal2.emit(self.message)
                        return
                    time.sleep(1)
                self.message = '定时时间到,开始执行.'
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
                # 构建跳转映射表
                self.jump_map = self.build_jump_map(sheet1)
                self.label_map = self.build_label_map(sheet1)
                if key == '0':  # 循环执行并计数
                    i = 1
                    self.message = '您选择了循环到死,程序已经开始执行.'
                    self.textsignal.emit(self.message)
                    while True:
                        if not self.isInterruptionRequested():
                            # 检查结束时间
                            if self.end_time and datetime.datetime.now() >= self.end_time:
                                self.message = '结束时间已到,停止执行.'
                                self.textsignal.emit(self.message)
                                self.message = '就绪.'
                                self.textsignal2.emit(self.message)
                                break
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
                        if not self.isInterruptionRequested():
                            # 检查结束时间
                            if self.end_time and datetime.datetime.now() >= self.end_time:
                                self.message = '结束时间已到,停止执行.'
                                self.textsignal.emit(self.message)
                                self.message = '就绪.'
                                self.textsignal2.emit(self.message)
                                break
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
                self.message = '就绪.'
                self.textsignal2.emit(self.message)
        finally:
            pg.mouseUp()
            pg.keyUp()
            self.message = '就绪.'
            self.textsignal2.emit(self.message)

    # 主要工作函数
    def main_work(self, sheet1):
        global picture_file_name
        max_rows = sheet1.nrows  # 读取表格的行数
        n = 2  # 从第二行第一列开始读取(排除表头)
        while n <= max_rows - 1:
            if not self.isInterruptionRequested():
                # 检查结束时间
                if self.end_time and datetime.datetime.now() >= self.end_time:
                    self.message = '结束时间已到,停止执行.'
                    self.textsignal.emit(self.message)
                    break
                tab_value = sheet1.row_values(rowx=n)
                instr = tab_value[1] if len(tab_value) > 1 else ''
                self.message = '第{}行命令运行中...'.format(n+1)
                self.textsignal2.emit(self.message)
                # 处理 IF/ELSE/ENDIF 分支指令
                if instr == 'IF':
                    img = tab_value[2] if len(tab_value) > 2 else ''
                    timeout = tab_value[5] if len(tab_value) > 5 else 0
                    if img == '':
                        img = picture_file_name
                    else:
                        img = 'data/{}/{}'.format(picture_file_name, img)
                    self.message = '正在检测条件: {} (超时{}秒)...'.format(img, timeout)
                    self.textsignal.emit(self.message)
                    found = self.wait_for_image_condition(img, timeout)
                    if found:
                        self.message = '条件满足, 执行IF分支.'
                        self.textsignal.emit(self.message)
                        n += 1
                    else:
                        self.message = '条件不满足, 跳过IF分支.'
                        self.textsignal.emit(self.message)
                        if n in self.jump_map:
                            else_row, endif_row = self.jump_map[n]
                            if else_row is not None:
                                n = else_row
                            else:
                                n = endif_row
                        else:
                            n += 1
                    continue
                elif instr == 'ELSE':
                    # ELSE 只在 IF 条件满足时到达, 需要跳过 ELSE 块
                    if n in self.jump_map:
                        _, endif_row = self.jump_map[n]
                        n = endif_row + 1
                        continue
                    else:
                        n += 1
                        continue
                elif instr == 'ENDIF':
                    n += 1
                    continue
                # 处理 CALL/RETURN/LABEL 子流程指令
                elif instr == 'CALL':
                    sub_name = tab_value[2] if len(tab_value) > 2 else ''
                    if sub_name in self.label_map:
                        self.call_stack.append(n + 1)
                        n = self.label_map[sub_name] + 1
                        self.message = '调用子流程: {}...'.format(sub_name)
                        self.textsignal.emit(self.message)
                    else:
                        self.message = '子流程"{}"未找到!'.format(sub_name)
                        self.textsignal.emit(self.message)
                        n += 1
                    continue
                elif instr == 'RETURN':
                    if self.call_stack:
                        n = self.call_stack.pop()
                        self.message = '子流程返回.'
                        self.textsignal.emit(self.message)
                    else:
                        self.message = '无调用栈, 忽略RETURN.'
                        self.textsignal.emit(self.message)
                        n += 1
                    continue
                elif instr == 'LABEL':
                    n += 1
                    continue

                # 原有指令类型处理（分发字典）
                handler_name = self.CMD_DISPATCH.get(instr)
                if handler_name:
                    handler = getattr(self, handler_name)
                    handler(tab_value)
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

    # 指令分发包装方法
    def do_mouse_click(self, tab_value):
        img_dir = 'data/{}/{}'.format(picture_file_name, tab_value[2])
        self.mouse_click(img_dir, self.mouse_type[int(tab_value[3])], int(tab_value[4]), tab_value[5])

    def do_mouse_position(self, tab_value):
        self.mouse_position(tab_value[2], self.mouse_type[int(tab_value[3])], int(tab_value[4]), tab_value[5])

    def do_mouse_drag(self, tab_value):
        self.mouse_drag(tab_value[2], tab_value[4])

    def do_mouse_long_push(self, tab_value):
        self.mouse_long_push(self.mouse_type[int(tab_value[3])], tab_value[5])

    def do_mouse_scroll(self, tab_value):
        self.mouse_scroll(tab_value[6])

    def do_key_board(self, tab_value):
        self.key_board(int(tab_value[7]), tab_value[8], tab_value[9])

    '''
    键鼠操作
    img:表示图片地址,需要点击的位置,用图片定位方式 
    button_type:表示点击鼠标的哪个按钮(左中右) 
    clicks_time:代表点击次数
    '''
    # 1.定义鼠标点击图片
    def mouse_click(self, img, button_type, clicks_time, wait_time):
        global picture_check_speed
        global confidence

        if wait_time == '':
            wait_time = 0
        else:
            wait_time = int(wait_time)
        t = 0
        while not self.isInterruptionRequested():
            try:
                location = pg.locateCenterOnScreen(img, confidence=confidence/100)
                if location is not None:
                    pg.moveTo(location.x, location.y, duration=0.2)
                    pg.click(clicks=clicks_time, interval=0.1, button=button_type)
                    time.sleep(0.5)
                    break

            except PgImageNotFoundException:
                pass

            except OSError:
                name = img.split('/')[-1]
                self.message = f'.图片文件"{name}"不存在或无法读取,请检查.'
                self.textsignal.emit(self.message)
                break

            except Exception:
                pass

            finally:
                time.sleep(picture_check_speed)
                t = t + picture_check_speed
                if wait_time != 0:
                    if t >= int(wait_time):
                        self.message = '.指令等待时间结束,未检测到该图片.'
                        self.textsignal.emit(self.message)
                        break

    # 2.定义鼠标点击坐标位置
    def mouse_position(self, position, button_type, clicks_time, wait_time):
        if wait_time == '':
            wait_time = 0
        else:
            wait_time = int(wait_time)
            self.message = '正在等待点击...'
            self.textsignal.emit(self.message)
        # 休眠时间判断
        for i in range(wait_time):
            if not self.isInterruptionRequested():
                time.sleep(1)
            else:
                break
        if not self.isInterruptionRequested():
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
        if push_time == '':
            push_time = 0
        else:
            push_time = int(push_time)
        self.message = '-长按鼠标-'
        self.textsignal.emit(self.message)
        pg.mouseDown(button=button_type)
        # 判断长按时间
        for i in range(push_time):
            if not self.isInterruptionRequested():
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
                    if not self.isInterruptionRequested():
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
    textsignal = Signal(str)

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
    textsignal = Signal(str)
    textsignal2 = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        self.message = '-复制坐标时请不要复制括号-'
        self.textsignal.emit(self.message)
        self.message = '鼠标坐标定位中'
        self.textsignal2.emit(self.message)
        while not self.isInterruptionRequested():
            time.sleep(1)
            x, y = pg.position()
            self.message = '当前坐标为（{}/{}）'.format(x, y)
            self.textsignal.emit(self.message)
        self.message = '-停止检测坐标-'
        self.textsignal.emit(self.message)
        self.message = '就绪.'
        self.textsignal2.emit(self.message)


# 单步调试的子线程
class MyThread6(MyThread):
    # textsignal2 = Signal(str)

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
            self.jump_map = self.build_jump_map(sheet1)
            self.label_map = self.build_label_map(sheet1)
            self.main_work(sheet1)
            self.message = '.单步调试结束.'
            self.textsignal.emit(self.message)

            self.message = '就绪.'
            self.textsignal2.emit(self.message)
        else: # 如果不存在对应文件夹
            self.message = '不存在对应的图片文件夹，请检查.'
            self.textsignal.emit(self.message)

            self.message = '就绪.'
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
    textsignal = Signal(str)

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
    w.show()
    sys.exit(app.exec())
