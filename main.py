import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter

from random import randrange


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(251, 255, 0))
            qp.drawEllipse(randrange(300), randrange(300), randrange(300), randrange(300))
            self.do_paint = False
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    app.exit(app.exec())
