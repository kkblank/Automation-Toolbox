# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini_sys.ui'
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
    QRadioButton, QSizePolicy, QSpinBox, QTextBrowser,
    QWidget)

class Ui_AutoWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(561, 478)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(25, 60, 281, 381))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 190, 93, 51))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(450, 150, 91, 21))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 150, 72, 15))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 270, 93, 51))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(330, 270, 93, 51))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(450, 190, 93, 51))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(330, 350, 93, 51))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 10, 93, 28))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(450, 350, 93, 51))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(452, 420, 91, 21))
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 420, 72, 15))
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(330, 100, 81, 21))
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 70, 61, 16))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(390, 30, 41, 19))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(440, 30, 61, 19))
        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(510, 30, 41, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 30, 101, 16))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 450, 71, 16))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 450, 191, 16))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(460, 70, 81, 16))
        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(470, 100, 70, 22))
        self.spinBox.setMaximum(100)
        self.spinBox.setValue(75)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(545, 100, 16, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Form", u"Ctrl+=", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5faa\u73af\u6b21\u6570\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u914d\u7f6e\u6587\u4ef6", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("Form", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u5b9a\u4f4d", None))
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("Form", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u76ee\u5f55", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5355\u6b65\u8c03\u8bd5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6307\u4ee4\u884c\u6570\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8868\u683c", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u5feb", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u6807\u51c6", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u6162", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u68c0\u6d4b\u901f\u5ea6\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u72b6\u6001\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5c31\u7eea", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u76f8\u4f3c\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"%", None))
    # retranslateUi

