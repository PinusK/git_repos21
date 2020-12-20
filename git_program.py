import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Круг.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('круг')
        self.pbt.clicked.connect(self.push_flag)
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_elips(qp)
            qp.end()

    def draw_elips(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        hw = random.randint(50, 300)
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        qp.drawEllipse(x, y, hw, hw)


    def push_flag(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
