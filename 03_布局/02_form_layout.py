from PySide6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QFormLayout


class Mywindow(QWidget):
    def __init__(self) :
        super().__init__()
        self.setformlayout = QFormLayout()
        self.setformlayout.addRow(QLabel('账号'),QLineEdit())
        self.setformlayout.addRow(QLabel('密码'),QLineEdit())
        self.setformlayout.addRow(QPushButton('登录'))

        self.setLayout( self.setformlayout)

if __name__ == "__main__":
    app = QApplication([])
    window = Mywindow()
    window.show()
    app.exec()