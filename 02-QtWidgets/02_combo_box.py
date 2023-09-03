from PySide6.QtWidgets import QApplication,QWidget,QComboBox,QVBoxLayout


class Mywidow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,500,300)
        cb = QComboBox()
        cb.addItems(['张三','李四','王五'])
        # 选项改变，输出当前的的选项
        cb.currentIndexChanged.connect(lambda: print(cb.currentText()))
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(cb)
        self.setLayout(mainLayout)
        

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()