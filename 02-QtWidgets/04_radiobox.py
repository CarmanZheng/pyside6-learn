from PySide6.QtWidgets import QApplication,QWidget,QButtonGroup
from radiobutton_ui import Ui_Form

class Mywidow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(500,200,500,300)
        self.btn1.clicked.connect(self.currentValue)
        self.btn2.clicked.connect(self.currentValue)
        # 此处需要手写QButtonGroup，然后将其加入组
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.btn1)
        self.button_group.addButton(self.btn2)

    def currentValue(self):
        selected_button = self.button_group.checkedButton()
        print(selected_button.text())

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()