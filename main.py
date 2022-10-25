import cv2
import qrcode

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("qrcodegui.ui", self)
        self.show()

        self.current_file = ""
        self.actionLoad.triggered.connect(self.load_image)
        self.actionSave.triggered.connect(self.load_image)

        self.pushButton.clicked.connect(self.generate_code)
        self.pushButton_2.clicked.connect(self.read_code)

    def load_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*)", options=options
        )
        if filename != "":
            self.current_file = filename
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(300, 300)
            self.label.setScaledContents(True)
            self.label.setPixmap(pixmap)

    def save_image(self):
        pass

    def generate_code(self):
        pass

    def read_code(self):
        pass


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
