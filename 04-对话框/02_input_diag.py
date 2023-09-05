from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QInputDialog,QLineEdit


class Mywidow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,300)
        btn1 = QPushButton('获取一个整型数字')
        btn1.clicked.connect(self.getIntDialog)
        btn2 = QPushButton('获取一个浮点型数字')
        btn2.clicked.connect(self.getDoubletDialog)
        
        # 0 代表默认选中干得元素
        # True /False 代表选项是否可编辑，默认True
        btn3  = QPushButton('获取一个item')
        btn3.clicked.connect(lambda:print(QInputDialog.getItem(self,'标题','内容',['小王','小米','小李'],0,False)))

        btn4  = QPushButton('获取单行文字')
        # 这里正常显示回显
        btn4.clicked.connect(lambda:print(QInputDialog.getText(self,'标题','内容', QLineEdit.EchoMode.Normal,'默认值')))

        btn5 =  QPushButton('获取多行文字')
        btn5.clicked.connect(lambda:print(QInputDialog.getMultiLineText(self,'标题','内容')))

        self.setvlayout = QVBoxLayout()
        self.setvlayout.addWidget(btn1)
        self.setvlayout.addWidget(btn2)
        self.setvlayout.addWidget(btn3)
        self.setvlayout.addWidget(btn4)
        self.setvlayout.addWidget(btn5)
        self.setLayout(self.setvlayout)

    def getIntDialog(self):
        reply,ok = QInputDialog.getInt(self,'标题','内容',1,0,100,1)
        if ok :
            print(reply)

    def getDoubletDialog(self):
        reply,ok = QInputDialog.getDouble(self,'标题','内容',1 ,4.0,10.0, 1)
        if ok :
            print(reply)



if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()