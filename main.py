from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from lexico import *
from sintactico import *


class CodeLabel(QWidget):
    def __init__(self):
        super(CodeLabel, self).__init__()
        layout = QHBoxLayout()
        label1_txt = QLabel()
        label1_txt.setText("Escribe tu codigo aqui")
        layout.addWidget(label1_txt)
        self.setLayout(layout)


class MainApp(QMainWindow):

    def __init(self, parent=None, *args):
        super().__init__()
        self.title = "Analizador Dart G6"
        self.geometry = (100, 100, 900, 650)
        self.setStyleSheet("background-color: #E5E8ED;")
        self.mountComponents()

    def mountComponents(self):
        self.windowTitle(self.title)
        codeLabel = CodeLabel()
        layout_v1 = QVBoxLayout()
        layout_v1.addWidget(codeLabel)
        widget = QWidget(self)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainApp()
    mainWindow.show()
    app.exec_()
