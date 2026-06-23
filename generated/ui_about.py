# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini_sys3.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_AboutWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(557, 518)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 160, 301, 301))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 10, 93, 28))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(210, 120, 115, 19))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(430, 160, 115, 19))
        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(430, 120, 115, 19))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 60, 93, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8fd9\u91cc\u662f\u6350\u8d60\u901a\u9053", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u76ee\u5f55", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u652f\u4ed8\u5b9d\u7ea2\u5305", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u652f\u4ed8\u5b9d", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u5fae\u4fe1", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\u4e3b\u9875", None))
    # retranslateUi

