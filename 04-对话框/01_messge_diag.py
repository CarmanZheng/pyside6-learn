from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QMessageBox


class Mywidow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,300)
        self.setvlayout = QVBoxLayout()
        self.btn = QPushButton('点击弹出消息框')
        self.setvlayout.addWidget(self.btn)
        self.btn.clicked.connect(self.btn_clicked)
        self.setLayout(self.setvlayout)
        
    def btn_clicked(self):
        # 参数第一项为父对象，第二项为标题，第三项为内容，第四项为可选按钮，第五项为默认按钮
        reply = QMessageBox.information(self,'标题','内容',QMessageBox.StandardButton.Ok|
                                        QMessageBox.StandardButton.Cancel|
                                        QMessageBox.StandardButton.Apply, 
                                        QMessageBox.StandardButton.Ok)
                               
        print(reply)
        if reply == QMessageBox.StandardButton.Ok:
            print('点击了ok')
        elif  reply == QMessageBox.StandardButton.Cancel:
            print('点击了取消')
        else:
            print('点击了应用')

        # reply = QMessageBox.warning(self,'标题','内容',QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        # reply = QMessageBox.question(self,'标题','内容',QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        # reply =  QMessageBox.critical(self,'标题','内容',QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        # QMessageBox.aboutQt(self)
        # QMessageBox.about(self,'标题','内容')

if __name__ == "__main__":
    app = QApplication([])
    window = Mywidow()
    window.show()
    app.exec()