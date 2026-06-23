import sys
import tkinter as tk
from tkinter import filedialog
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import *
from generated.ui_ocr import Ui_OcrWindow
from paddleocr import PaddleOCR

# import main

# 定义全局变量用于传参
FILE_PATH = 0
PICTURE_PATH = 0
LANGUAGE = 'ch'


class MyWindow6(QMainWindow):
    # 初始化父类
    def __init__(self):
        super().__init__()
        # 依次调用自己写的主函数（顺序）
        self.sys_ui()
        # 只显示x按钮,不显示最大化/最小化
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    # 定义一个打印函数(打印子线程中传回来的信息)
    def my_print(self, str_text):
        self.text_area.append(str_text)
        self.text_area.repaint()

    # 定义显示状态的函数
    def my_state(self, text):
        self.state_area.setText(text)

    # 清除文字动作
    def clear_action(self):
        self.text_area.setText('---欢迎使用OCR功能---')

    # 选择语言动作
    def select_language(self):
        global LANGUAGE
        if self.select_lang_bt.currentText() == '中文':
            LANGUAGE = 'ch'
        elif self.select_lang_bt.currentText() == '英文':
            LANGUAGE = 'en'
        elif self.select_lang_bt.currentText() == '日文':
            LANGUAGE = 'japan'
        elif self.select_lang_bt.currentText() == '德文':
            LANGUAGE = 'german'
        elif self.select_lang_bt.currentText() == '韩文':
            LANGUAGE = 'korean'
        elif self.select_lang_bt.currentText() == '法文':
            LANGUAGE = 'fr'

    # 选择文件夹动作
    def slect_file(self):
        self.my_print('该功能正在开发中...')
        # global FILE_PATH
        # root = tk.Tk()
        # root.withdraw()
        # FILE_PATH = filedialog.askdirectory()
        # self.my_thread = MyThread()
        # self.my_thread.start()
        # self.my_thread.textsignal.connect(self.my_print)

    # 选择图片动作
    def select_picture(self):
        global FILE_PATH
        root = tk.Tk()
        root.withdraw()
        FILE_PATH = filedialog.askopenfilename()
        self.my_thread2 = MyThread2()
        self.my_thread2.start()
        self.my_thread2.textsignal.connect(self.my_print)
        self.my_thread2.textsignal2.connect(self.my_state)

    '''UI显示界面'''
    def sys_ui(self):
        self.ui = Ui_OcrWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('自动化工具箱v{}'.format(4.3))

        # 标题栏按钮
        # self.mainWindow_bt = self.ui.pushButton  # 返回目录界面按钮
        # self.mainWindow_bt.clicked.connect(self.tow)  # 打开目录界面
        # self.mainWindow_bt.clicked.connect(self.ui.close)  # 关闭原来窗口

        # 选择语言按钮/槽函数
        self.select_lang_bt = self.ui.comboBox
        self.select_lang_bt.activated.connect(self.select_language)
        # 选择图片按钮/槽函数
        self.select_picture_bt = self.ui.pushButton_2
        self.select_picture_bt.clicked.connect(self.select_picture)
        # 清除文字按钮/槽函数
        self.clear_bt = self.ui.pushButton_3
        self.clear_bt.clicked.connect(self.clear_action)

        # 文本显示区域
        self.text_area = self.ui.textBrowser
        self.text_area.setText('---欢迎使用OCR功能---')
        # 运行状态显示区域
        self.state_area = self.ui.label_2

    # # 切换目录
    # def tow(self):
    #     self.w1 = main.MyWindow()
    #     self.w1.ui.show()


# 选择图片文件夹的子线程
class MyThread(QThread):
    textsignal = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global FILE_PATH
        print(FILE_PATH)

    # 文字识别函数
    def picture_action(self):
        global FILE_PATH
        global LANGUAGE
        ocr = PaddleOCR(use_angle_cls=True, lang=f"{LANGUAGE}")
        img_path = FILE_PATH  # 读图方式与opencv完全相同
        result = ocr.ocr(img_path, cls=True)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                self.message = line[-1][0]
                self.textsignal.emit(self.message)


# 选择图片的子线程
class MyThread2(MyThread):
    textsignal2 = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        # 设置状态为运行中
        self.message = '运行中...'
        self.textsignal2.emit(self.message)
        # 显示提示文字
        self.message = '#####-文字识别中，请等待-#####'
        self.textsignal.emit(self.message)

        # 文本识别
        try:
            self.picture_action()
        except:
            self.message = '请选择正确的图片文件！'
            self.textsignal.emit(self.message)

        # 设置状态为就绪
        self.message = '就绪...'
        self.textsignal2.emit(self.message)
        # 显示提示文字
        self.message = '#####-文字识别完毕-#####'
        self.textsignal.emit(self.message)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建app
    w = MyWindow6()  # 实例化类
    w.show()  # 展示窗口
    sys.exit(app.exec())  # 保持窗口
