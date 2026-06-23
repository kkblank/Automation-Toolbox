'''
作者界面
'''

import sys
import webbrowser
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from generated.ui_about import Ui_AboutWindow
import main


class MyWindow3(QMainWindow):

    def __init__(self):
        super().__init__()
        self.sys_ui()
        self.setWindowFlags(Qt.WindowCloseButtonHint)

    ''' ui界面按钮动作函数'''
    # 打开作者主页动作
    def main_web_action(self):
        url = 'https://space.bilibili.com/2805045'
        webbrowser.open(url, new=2, autoraise=True)

    ''' ui显示界面'''
    def sys_ui(self):
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('自动化工具箱v{}'.format(main.NAME))

        # 标题栏按钮
        self.mainWindow_bt = self.ui.pushButton_4  # 返回目录界面按钮
        self.mainWindow_bt.clicked.connect(self.tow)  # 打开目录界面
        self.mainWindow_bt.clicked.connect(self.close)  # 关闭原来窗口

        # 作者主页按钮
        self.main_web_bt = self.ui.pushButton
        self.main_web_bt.clicked.connect(self.main_web_action)

        # 捐赠图片显示区域(显示捐赠收款码)/没有槽函数
        self.img_are = self.ui.label_3
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

    def select_action(self, btn):
        pass

    # 切换目录
    def tow(self):
        self.w1 = main.MyWindow()
        self.w1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow3()
    w.show()
    sys.exit(app.exec())