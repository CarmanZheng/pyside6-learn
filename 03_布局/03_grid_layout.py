from PySide6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QGridLayout

class Mywindow(QWidget):
    def __init__(self) :
        super().__init__()
        self.setgridlayout = QGridLayout()
        self.setgridlayout.addWidget(QLabel('账号'),0,0)
        # 参数分别为元素，行位置，列位置，行扩展，列扩展
        self.setgridlayout.addWidget(QLineEdit(),0,1)
        self.setgridlayout.addWidget(QLabel('密码'),1,0)
        self.setgridlayout.addWidget(QLineEdit(),1,1)
        self.setgridlayout.addWidget(QPushButton('登录'),2,0,10,0)


        self.setLayout(self.setgridlayout)




if __name__ == "__main__":
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()