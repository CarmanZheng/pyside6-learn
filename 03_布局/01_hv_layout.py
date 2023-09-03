
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout,QPushButton

class Mywindow(QWidget):
    def __init__(self) :
        super().__init__()

        # 定义垂直布局
        self.setmainlayout = QVBoxLayout()
        
        # 设置第一行布局 水平布局
        self.sethlayout1 = QHBoxLayout()
        self.sethlayout1.addWidget(QLabel('账号'))
        self.sethlayout1.addWidget(QLineEdit())
        # 设置第二行布局 水平布局
        self.sethlayout2 = QHBoxLayout()
        self.sethlayout2.addWidget(QLabel('密码'))
        self.sethlayout2.addWidget(QLineEdit())
        # 设置第三行布局 水平布局
        self.sethlayout3 = QHBoxLayout() 
        self.sethlayout3.addWidget(QPushButton('登录')) 
        
        # 将水平布局 加入到垂直布局中
        self.setmainlayout.addLayout(self.sethlayout1)
        self.setmainlayout.addLayout(self.sethlayout2)
        self.setmainlayout.addLayout(self.sethlayout3)

        # 将整体布局设置为垂直布局
        self.setLayout(self.setmainlayout)
        


if __name__ == "__main__":
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()
