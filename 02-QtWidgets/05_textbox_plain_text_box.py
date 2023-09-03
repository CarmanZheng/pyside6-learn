from PySide6.QtWidgets import QApplication,QWidget,QButtonGroup
from textbox_ui import Ui_Form


class Mywidow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit.setText('我是富文本框')
        self.plainTextEdit.setPlainText('我是纯文本框')
        self.textEdit.textChanged.connect(self.editChange)

    def editChange(self):
        # 获取当前富文本框的值
        print( self.textEdit.toPlainText())
        # 获取当前纯文本框的值
        print(self.plainTextEdit.toPlainText())

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()