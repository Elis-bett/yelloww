from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.figure = 'circle'
        self.setWindowTitle('Желтые круги')
        self.pushButton.clicked.connect(self.draw)
        self.color = (255, 255, 0)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            size = random.choice(range(100))
            x, y = random.randint(100, 800 - 100), random.randint(100, 600 - 100)
            if self.figure == 'circle':
                qp.drawEllipse(x, y, size, size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
