from PySide6.QtWidgets import QApplication,QWidget,QSlider
from slider_ui import Ui_Form



class Mywidow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置滑块的最大值 最小值 间隔 位置
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        # 设置改变滑块值的信号
        self.horizontalSlider.valueChanged.connect(self.valueChange)
    def valueChange(self):
        print(self.horizontalSlider.value())

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()