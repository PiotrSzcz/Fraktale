import sierpinski
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
os.environ['SDL_VIDEO_CENTERED'] = '1'

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()

    win.setGeometry(100, 100, 500, 500)
    win.setWindowTitle("Fractal visualization")
    win.setWindowIcon(QIcon("icon.jpg"))
    win.show()
    sys.exit(app.exec_())

window()
