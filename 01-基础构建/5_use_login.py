from PySide6.QtWidgets import QMainWindow,QApplication
from login import Ui_Form

# 继承Ui_Form
class Mywidow(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        # 接收Ui_Form
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()