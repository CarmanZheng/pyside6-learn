from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QFileDialog

class Mywidow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,300)
        # 选择单个文件
        btn1 = QPushButton('选择单个文件')
        btn1.clicked.connect(lambda: print(QFileDialog.getOpenFileName(self,'选择一个文件','.','所有文件(*.py)')))

        # 选择多个文件
        btn2 = QPushButton('选择多个文件')
        btn2.clicked.connect(lambda: print(QFileDialog.getOpenFileNames(self,'选择多个文件','.','所有文件(*.py)')))

        # 选择文件夹
        btn3 = QPushButton('选择文件夹')
        btn3.clicked.connect(lambda: print(QFileDialog.getExistingDirectory(self,'选择一个文件夹','.')))

        # 保存文件：如果真正要保存，需要在这个函数里面做保存的动作
        btn4 = QPushButton('保存文件')
        btn4.clicked.connect(lambda: print(QFileDialog.getSaveFileName(self,'保存这个文件','.','所有文件(*.py);音频文件（*.mp3')))

        self.setvlayout = QVBoxLayout()
        self.setvlayout.addWidget(btn1)
        self.setvlayout.addWidget(btn2)
        self.setvlayout.addWidget(btn3)
        self.setvlayout.addWidget(btn4)
        self.setLayout(self.setvlayout)


if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()