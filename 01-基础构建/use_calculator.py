from PySide6.QtWidgets import QMainWindow,QApplication
from calculator_ui import Ui_Form

# 继承Ui_Form
class Mywidow(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        # 接收Ui_Form
        self.setupUi(self)
        # 绑定函数
        self.bind()
        # 定义结果
        self.result = ''
        # 定义计算符号
        self.cal_symbol = ['+','-','*','/']
    

    def bind(self):
        self.btn_0.clicked.connect(lambda: self.addNum('0'))
        self.btn_1.clicked.connect(lambda: self.addNum('1'))
        self.btn_2.clicked.connect(lambda: self.addNum('2'))
        self.btn_3.clicked.connect(lambda: self.addNum('3'))
        self.btn_4.clicked.connect(lambda: self.addNum('4'))
        self.btn_5.clicked.connect(lambda: self.addNum('5'))
        self.btn_6.clicked.connect(lambda: self.addNum('6'))
        self.btn_7.clicked.connect(lambda: self.addNum('7'))
        self.btn_8.clicked.connect(lambda: self.addNum('8'))
        self.btn_9.clicked.connect(lambda: self.addNum('9'))
        self.btn_dot.clicked.connect(lambda: self.addNum('.'))
        self.btn_plus.clicked.connect(lambda: self.addSymbol('+'))
        self.btn_sub.clicked.connect(lambda: self.addSymbol('-'))
        self.btn_multi.clicked.connect(lambda: self.addSymbol('*'))
        self.btn_div.clicked.connect(lambda: self.addSymbol('/'))
        self.btn_equal.clicked.connect(self.getResult)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_back.clicked.connect(self.delete)

    def addNum(self,number):
        self.result += number 
        symbol = list(filter( lambda i:  i in self.result , [i for i in self.cal_symbol]))
    
        if symbol:
            content = self.result.split(sep=symbol[0])[-1]
            self.lcdNumber.display(content)
        else:
            self.lcdNumber.display(self.result)

    def addSymbol(self,symbol):
        if self.result[-1] in self.cal_symbol:
            self.result[-1] = symbol
        else:
            self.result += symbol 
        self.lcdNumber.display(self.result[:-1])
        

    def getResult(self):
        self.lcdNumber.display(eval(self.result))
        self.result = ''

    def clear(self):
        self.result = ''
        self.lcdNumber.display(None)

    def delete(self):
        self.result = self.result[:-1]
        self.lcdNumber.display(self.result)

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()