from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("merde")
        self.geometry()
        self.resize(400, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Fen = Window()
    Fen.show()
    sys.exit(app.exec_())  