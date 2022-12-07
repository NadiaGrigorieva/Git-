import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygon
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.x1 = 600
        self.y1 = 400
        self.setGeometry(300, 300, self.x1, self.y1)
        self.do_paint = False
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            self.size = random.randint(5, 100)
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, self.x1 - 100), random.randint(100, self.y1 - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()
            
    def draw(self):
        self.do_paint = True
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
