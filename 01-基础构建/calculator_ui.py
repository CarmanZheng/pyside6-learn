# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(426, 564)
        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(60, 30, 321, 50))
        self.lcdNumber.setMinimumSize(QSize(0, 30))
        self.lcdNumber.setMaximumSize(QSize(16777215, 50))
        self.lcdNumber.setDigitCount(15)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 110, 322, 386))
        font = QFont()
        font.setPointSize(14)
        self.widget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_back = QPushButton(self.widget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(100, 70))
        self.btn_back.setMaximumSize(QSize(120, 16777215))
        self.btn_back.setFont(font)

        self.gridLayout.addWidget(self.btn_back, 0, 2, 1, 1)

        self.btn_clear = QPushButton(self.widget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(80, 70))
        self.btn_clear.setMaximumSize(QSize(120, 16777215))
        self.btn_clear.setFont(font)

        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_7 = QPushButton(self.widget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setMinimumSize(QSize(20, 70))
        self.btn_7.setMaximumSize(QSize(80, 16777215))
        self.btn_7.setFont(font)

        self.gridLayout_2.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_8 = QPushButton(self.widget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setMinimumSize(QSize(20, 70))
        self.btn_8.setMaximumSize(QSize(80, 16777215))
        self.btn_8.setFont(font)

        self.gridLayout_2.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_9 = QPushButton(self.widget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setMinimumSize(QSize(20, 70))
        self.btn_9.setMaximumSize(QSize(80, 16777215))
        self.btn_9.setFont(font)

        self.gridLayout_2.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_div = QPushButton(self.widget)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setEnabled(True)
        self.btn_div.setMinimumSize(QSize(20, 70))
        self.btn_div.setMaximumSize(QSize(80, 16777215))
        self.btn_div.setFont(font)

        self.gridLayout_2.addWidget(self.btn_div, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_4 = QPushButton(self.widget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(20, 70))
        self.btn_4.setMaximumSize(QSize(80, 16777215))
        self.btn_4.setFont(font)

        self.gridLayout_3.addWidget(self.btn_4, 0, 0, 1, 1)

        self.btn_5 = QPushButton(self.widget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(20, 70))
        self.btn_5.setMaximumSize(QSize(80, 16777215))
        self.btn_5.setFont(font)

        self.gridLayout_3.addWidget(self.btn_5, 0, 1, 1, 1)

        self.btn_6 = QPushButton(self.widget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setMinimumSize(QSize(20, 70))
        self.btn_6.setMaximumSize(QSize(80, 16777215))
        self.btn_6.setFont(font)

        self.gridLayout_3.addWidget(self.btn_6, 0, 2, 1, 1)

        self.btn_multi = QPushButton(self.widget)
        self.btn_multi.setObjectName(u"btn_multi")
        self.btn_multi.setEnabled(True)
        self.btn_multi.setMinimumSize(QSize(20, 70))
        self.btn_multi.setMaximumSize(QSize(80, 16777215))
        self.btn_multi.setFont(font)

        self.gridLayout_3.addWidget(self.btn_multi, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_1 = QPushButton(self.widget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(20, 70))
        self.btn_1.setMaximumSize(QSize(80, 16777215))
        self.btn_1.setFont(font)

        self.gridLayout_4.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_2 = QPushButton(self.widget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(20, 70))
        self.btn_2.setMaximumSize(QSize(80, 16777215))
        self.btn_2.setFont(font)

        self.gridLayout_4.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_3 = QPushButton(self.widget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(20, 70))
        self.btn_3.setMaximumSize(QSize(80, 16777215))
        self.btn_3.setFont(font)

        self.gridLayout_4.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_sub = QPushButton(self.widget)
        self.btn_sub.setObjectName(u"btn_sub")
        self.btn_sub.setEnabled(True)
        self.btn_sub.setMinimumSize(QSize(20, 70))
        self.btn_sub.setMaximumSize(QSize(80, 16777215))
        self.btn_sub.setFont(font)

        self.gridLayout_4.addWidget(self.btn_sub, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_0 = QPushButton(self.widget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setMinimumSize(QSize(20, 70))
        self.btn_0.setMaximumSize(QSize(80, 16777215))
        self.btn_0.setFont(font)

        self.gridLayout_5.addWidget(self.btn_0, 0, 0, 1, 1)

        self.btn_dot = QPushButton(self.widget)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setMinimumSize(QSize(20, 70))
        self.btn_dot.setMaximumSize(QSize(80, 16777215))
        self.btn_dot.setFont(font)

        self.gridLayout_5.addWidget(self.btn_dot, 0, 1, 1, 1)

        self.btn_equal = QPushButton(self.widget)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setMinimumSize(QSize(20, 70))
        self.btn_equal.setMaximumSize(QSize(80, 16777215))
        self.btn_equal.setFont(font)

        self.gridLayout_5.addWidget(self.btn_equal, 0, 2, 1, 1)

        self.btn_plus = QPushButton(self.widget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setEnabled(True)
        self.btn_plus.setMinimumSize(QSize(20, 70))
        self.btn_plus.setMaximumSize(QSize(80, 16777215))
        self.btn_plus.setFont(font)

        self.gridLayout_5.addWidget(self.btn_plus, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"back", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"clear", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_multi.setText(QCoreApplication.translate("Form", u"*", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.btn_equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.btn_plus.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

