# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radiobutton.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(429, 306)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 30, 301, 80))
        self.btn1 = QRadioButton(self.groupBox)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(20, 40, 95, 20))
        self.btn2 = QRadioButton(self.groupBox)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(140, 40, 95, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u6027\u522b", None))
        self.btn1.setText(QCoreApplication.translate("Form", u"\u7537", None))
        self.btn2.setText(QCoreApplication.translate("Form", u"\u5973", None))
    # retranslateUi

