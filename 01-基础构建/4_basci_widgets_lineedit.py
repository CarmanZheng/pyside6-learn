from PySide6.QtWidgets import QApplication,QMainWindow,QLineEdit

class Mywidow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口的位置和宽高
        self.setGeometry(500,300,500,300)
        # 添加按钮及按钮的宽高
        btn = QLineEdit('我是输入框',self)
        btn.setGeometry(0,10,100,50)     

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()