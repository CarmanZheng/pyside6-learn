from PySide6.QtWidgets import QApplication,QWidget,QCheckBox,QVBoxLayout,QLabel


class Mywidow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,500,300)
        self.lb = QLabel()
        cb = QCheckBox('是否被选中')
        
        # 选项改变，输出当前的的选项,默认值为状态
        cb.stateChanged.connect(self.check_func)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(cb)
        mainLayout.addWidget(self.lb)
        self.setLayout(mainLayout)

    def check_func(self,state):
        self.lb.setText(str(False) if state==0 else str(True))  

        

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()