'''
批量处理界面
'''
import imghdr
import os
import sys
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore
import main

# 全局变量,用于传递主界面信息
# 0中间,1左上,2左下,3右上,4右下(水印位置)
DIC = {'file_name':'file_', 'file_num':'2', 'start_num':'1', 'water_flag':'1', 'file_path':'', 'picture_path':'',
       'front_size':'14', 'water_text':'请输入水印', 'water_picture':'', 'water_position':'0', 'tmd':'50'}


class MyWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    # 切换目录
    def tow(self):
        self.w1 = main.MyWindow()
        self.w1.ui.show()

    def sys_ui(self):
        self.ui = uic.loadUi('./mini_sys5.ui')
        self.ui.setWindowTitle('自动化工具箱v{}'.format(main.NAME))
        # 标题栏按钮
        self.mainWindow_bt = self.ui.pushButton
        self.mainWindow_bt.clicked.connect(self.tow)
        self.mainWindow_bt.clicked.connect(self.ui.close)
        # 图片文件夹2按钮
        self.picture_bt = self.ui.pushButton_5
        self.picture_bt.clicked.connect(self.picture_action)
        # 提示文字显示区域
        self.text_are = self.ui.textBrowser

        '''批量重命名区'''
        # 位数显示区域
        self.file_num_are = self.ui.lineEdit_6
        # 起始编号显示区域
        self.start_num_are = self.ui.lineEdit_7
        # 文件头显示区域
        self.file_name_are = self.ui.lineEdit
        # 选择文件按钮
        self.select_file_bt = self.ui.pushButton_2
        self.select_file_bt.clicked.connect(self.select_file_action)

        '''批量水印区'''
        # 水印位置选择按钮/槽函数
        self.tool_bt = self.ui.comboBox
        self.tool_bt.activated.connect(self.select_water_position)

        # 水印方式选择按钮
        self.select_bt = self.ui.radioButton  # 文字水印
        self.select_bt2 = self.ui.radioButton_2  # 图片水印
        # 设置默认选中按钮
        self.select_bt.setChecked(True)
        # 给水印选择按钮绑定槽函数
        self.select_bt.toggled.connect(lambda: self.select_action(self.select_bt))
        self.select_bt2.toggled.connect(lambda: self.select_action(self.select_bt2))

        # 图片水印按钮/槽函数
        self.picture_water_bt = self.ui.pushButton_4
        self.picture_water_bt.clicked.connect(self.picture_water_action)
        # 图片水印路径显示区域
        self.picture_water_are = self.ui.lineEdit_5

        # 批量选择图片按钮
        self.picture_select_bt = self.ui.pushButton_6
        self.picture_select_bt.clicked.connect(self.picture_path_action)
        # 水印字体大小区域
        self.front_size_are = self.ui.spinBox_2
        # 水印文字区域
        self.front_are = self.ui.lineEdit_2
        # 透明度区域
        self.tmd_are = self.ui.spinBox

    # 选择水印位置动作
    def select_water_position(self):
        global DIC
        if self.tool_bt.currentText() == '中间':
            DIC['water_position'] = '0'
        elif self.tool_bt.currentText() == '左上角':
            DIC['water_position'] = '1'
        elif self.tool_bt.currentText() == '左下角':
            DIC['water_position'] = '2'
        elif self.tool_bt.currentText() == '右上角':
            DIC['water_position'] = '3'
        elif self.tool_bt.currentText() == '右下角':
            DIC['water_position'] = '4'

    # 打开图片文件夹2
    def picture_action(self):
        path = os.path.abspath('data') + '\picture2'
        os.startfile(path)

    # 选择重命名文件夹
    def select_file_action(self):
        global DIC
        DIC['file_name'] = self.file_name_are.text()
        DIC['file_num'] = self.file_num_are.text()
        DIC['start_num'] = self.start_num_are.text()
        # 选择路径
        root = tk.Tk()
        root.withdraw()
        DIC['file_path'] = filedialog.askdirectory()
        # 开启子线程
        self.my_thread = MyThread()
        self.my_thread.start()
        self.my_thread.textsignal.connect(self.my_print)

    # 定义一个打印函数(打印子线程中传回来的信息)
    def my_print(self, str_text):
        self.text_are.append(str_text)
        self.text_are.repaint()

    # 选择水印的方式(文字/图片)
    def select_action(self, btn):
        global DIC
        if btn.text() == '文字水印':
            if btn.isChecked():
                DIC['water_flag'] = '1'
        elif btn.text() == '图片水印':
            if btn.isChecked():
                DIC['water_flag'] = '2'

    # 选择水印图片动作
    def picture_water_action(self):
        global DIC
        root = tk.Tk()
        root.withdraw()
        DIC['water_picture'] = filedialog.askopenfilename()
        self.picture_water_are.setText(DIC['water_picture'])

    # 批量选择图片动作
    def picture_path_action(self):
        global DIC
        # 开启子线程
        DIC['front_size'] = self.front_size_are.value()
        DIC['water_text'] = self.front_are.text()
        DIC['tmd'] = self.tmd_are.value()
        root = tk.Tk()
        root.withdraw()
        DIC['picture_path'] = filedialog.askdirectory()
        self.my_thread2 = MyThread2()
        self.my_thread2.start()
        self.my_thread2.textsignal.connect(self.my_print)


# 批量选择文件的子线程
class MyThread(QThread):
    # 设定一个传递文本信息的变量
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global DIC

        filepath = DIC['file_path']  # 记录文件路径
        try:
            lst = os.listdir('{}'.format(filepath))  # 遍历路径下的文件
            self.message = '已选择文件夹,正在进行重命名...'
            self.textsignal.emit(self.message)
            j = 0  # 记录处理的文件数目
            for i in lst:
                filename = '{}/{}'.format(filepath, i)  # 老文件名+路径
                if os.path.isfile(filename):  # 判断是否为文件
                    file_type = os.path.splitext(filename)[1]  # 获取扩展名
                    id = int(DIC['start_num'])
                    # 生成新文件名+路径
                    temp = int(DIC['file_num'])
                    newfilename = DIC['file_name'] + '{}'.format(str(id + j).zfill(temp)) + file_type
                    newfilepath = '{}/{}'.format(filepath, newfilename)
                    os.rename(filename, newfilepath)
                    j = j + 1
            self.message = '--程序运行完毕!--'
            self.textsignal.emit(self.message)
            self.message = '--共处理{}个文件--'.format(j)
            self.textsignal.emit(self.message)
            self.message = '----------------'
            self.textsignal.emit(self.message)
        except:
            self.message = '出错啦,请选择正确的文件夹路径!'
            self.textsignal.emit(self.message)
            self.message = '----------------'
            self.textsignal.emit(self.message)


# 批量选择图片的子线程
class MyThread2(QThread):
    # 设定一个传递文本信息的变量
    textsignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global DIC
        filepath = DIC['picture_path']  # 记录文件路径
        try:
            lst = os.listdir('{}'.format(filepath))  # 遍历路径下的文件
            self.message = '已选择文件夹,正在添加水印...'
            self.textsignal.emit(self.message)
            j = 0  # 记录处理图片的数目
            k = 0  # 记录不是图片的数目
            for i in lst:
                filename = '{}/{}'.format(filepath, i)  # 路径+文件名
                # 处理目录下面的图像文件,跳过非图像文件
                isimg = imghdr.what(filename)
                if (isimg == 'jpg') or (isimg == 'png'):
                    self.add_watermark(filename)  # 如果是图片则调用添加水印的函数
                    j = j + 1
                else:
                    k = k + 1
            self.message = '--成功{}个,失败{}个--'.format(j, k)
            self.textsignal.emit(self.message)
            self.message = '--水印添加完毕,共处理{}个文件--'.format(j + k)
            self.textsignal.emit(self.message)
        except:
            self.message = '出错啦,请选择正确的文件夹路径!'
            self.textsignal.emit(self.message)
            self.message = '----------------'
            self.textsignal.emit(self.message)

    # 添加水印的函数
    def add_watermark(self, filename):
        global DIC
        if DIC['water_flag'] == '1':
            self.add_text_mark(filename)
        else:
            self.add_picture_mark(filename)

    # 添加文字水印
    def add_text_mark(self, filename):
        global DIC
        word = DIC['water_text']
        front_size = int(DIC['front_size'])  # 字体大小
        im = Image.open(filename).convert('RGBA')  # 打开原始图像,转换格式
        newimg = Image.new('RGBA', im.size, (255,255,255,0))  # 储存添加水印后的图片
        font = ImageFont.truetype('f001.ttf', front_size)
        imgdraw = ImageDraw.Draw(newimg)  # 创建绘制对象
        imgwidth, imgheight = im.size  # 记录图片大小

        # 计算右边框
        def is_chinese(word1):
            for ch in word1:
                if '\u4e00' <= ch <= '\u9fff':
                    return True
            return False

        ch_word_num = 0
        for temp in DIC['water_text']:
            if is_chinese(temp):
                ch_word_num = ch_word_num + 1
        # 获取字体宽度/高度
        txtwidth = front_size * ch_word_num + front_size // 2 * (len(word) - ch_word_num)
        txtheight = front_size
        # 设置水印文字位置
        if DIC['water_position'] == '1':
            water_position = (0, 0)
        elif DIC['water_position'] == '2':
            water_position = (0, imgheight - txtheight)
        elif DIC['water_position'] == '3':
            water_position = (imgwidth - txtwidth, 0)
        elif DIC['water_position'] == '4':
            water_position = (imgwidth - txtwidth, imgheight - txtheight)
        else:
            water_position = ((imgwidth-txtwidth)//2, (imgheight-txtheight)//2)
        # 设置文本颜色
        imgdraw.text(water_position, word, font=font, fill='#FF0000')
        # 设置透明度
        alpha = newimg.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(int(DIC['tmd']) / 100)
        newimg.putalpha(alpha)
        t = filename.split('/')
        Image.alpha_composite(im, newimg).save('{}/{}'.format('data/picture2', t[-1]))

    # 添加图片水印
    def add_picture_mark(self, filename):
        global DIC
        im = Image.open(filename)  # 打开原始图片
        mark = Image.open(DIC['water_picture'])  # 打开水印图片
        rgba_im = im.convert('RGBA')  # 将原始图转换成RGBA
        rgba_mark = mark.convert('RGBA')  # 将水印图转换成RGBA
        imgwidth, imgheight = rgba_im.size  # 获取原始图像尺寸
        nimgwidth, nimgheight = rgba_mark.size  # 获取水印图像尺寸
        # 计算水印位置
        if DIC['water_position'] == '1':
            water_position = (0, 0)
        elif DIC['water_position'] == '2':
            water_position = (0, imgheight - nimgheight)
        elif DIC['water_position'] == '3':
            water_position = (imgwidth - nimgwidth, 0)
        elif DIC['water_position'] == '4':
            water_position = (imgwidth - nimgwidth, imgheight - nimgheight)
        else:
            water_position = ((imgwidth - nimgwidth) // 2, (imgheight - nimgwidth) // 2)
        # 设置透明度
        rgbamarkpha = rgba_mark.convert('L').point(lambda _: int(int(DIC['tmd'])/100*255))
        rgba_mark.putalpha(rgbamarkpha)
        # 水印位置
        rgba_im.paste(rgba_mark, water_position, rgbamarkpha)
        t = filename.split('/')
        rgba_im.save('{}/{}'.format('data/picture2', t[-1]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow5()
    w.ui.show()
    sys.exit(app.exec_())