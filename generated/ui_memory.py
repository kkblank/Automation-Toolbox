# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini_sys4.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QTextEdit, QWidget)

class Ui_MemoryWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(557, 518)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 80, 256, 401))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 80, 93, 41))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 140, 93, 41))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 170, 72, 15))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(310, 270, 221, 211))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 250, 111, 16))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 20, 93, 28))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(430, 80, 93, 41))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 200, 221, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8bb0\u5fc6\u6587\u4ef6\u5939", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("Form", u"\u547d\u4ee4\u7a97\u53e3\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7c98\u8d34\u6d4b\u8bd5\u7a97\u53e3\uff1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u76ee\u5f55", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.lineEdit.setText("")
    # retranslateUi

