# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini_sys6.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_OcrWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(691, 566)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 93, 28))
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 70, 651, 481))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 10, 93, 51))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(390, 10, 93, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(510, 40, 72, 15))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(590, 40, 72, 15))
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 31, 87, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setEditable(False)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 10, 72, 15))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u76ee\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u56fe\u7247", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u6587\u5b57", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u72b6\u6001\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5c31\u7eea...", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u4e2d\u6587", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u82f1\u6587", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u65e5\u6587", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u5fb7\u6587", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u97e9\u6587", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"\u6cd5\u6587", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8bed\u8a00\uff1a", None))
    # retranslateUi

