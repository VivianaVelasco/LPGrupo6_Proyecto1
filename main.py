from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from lexico import *
from sintactico import *
from errorHandle import *

# Buttons Component
class Buttons(QWidget):

    def __init___(self, editor, print_label):
        layout = QVBoxLayout()
        button_lexer = QPushButton("Run Lexer")
        button_lexer.setFixedSize(100, 40)
        button_lexer.setCursor(QCursor(Qt.PointingHandCursor))
        button_lexer.clicked.connect(lambda: self.onClickLexer(editor, print_label))

        button_parser = QPushButton("Run Parser")
        button_parser.setFixedSize(100, 40)
        button_parser.setCursor(QCursor(Qt.PointingHandCursor))
        button_parser.clicked.connect(lambda: self.onClickParser(editor, print_label))

        button_openFile = QPushButton("Open File")
        button_openFile.setFixedSize(100, 40)
        button_openFile.setCursor(QCursor(Qt.PointingHandCursor))
        button_openFile.clicked.connect(lambda: self.openFile(editor))

        layout.addWidget(button_lexer)
        layout.addWidget(button_parser)
        layout.addWidget(button_openFile)
        self.setLayout(layout)
    
    def onClickLexer(self, editor, print_label):
        tp = print_label.plain_text
        tp.setPlainText("")
        tp.insertPlainText("Lexical Analysis Output\n")
        handleError()
        tokens = runLexerAnalyzer(editor.toPlainText())
        if handleError.lexer_err:
            tp.insertPlainText(
                f"Number of lexer errors: {handleError.lexer_err}\n")
            tp.insertPlainText(handleError.lexer_err_descript)
        else:
            for tok in tokens:
                tp.insertPlainText("{:4} : {:4}".format(tok.value, tok.type))
                tp.insertPlainText("\n")
        tp.insertPlainText("\n")
        tp.insertPlainText("\n")

    def onClickedParser(self, editor, print_label):
        tp = print_label.plain_text
        tp.setPlainText("")
        tp.insertPlainText("Syntactic Analysis Output\n")
        handleError()
        tree = runParserAnalyzer(editor.toPlainText())
        if handleError.syntax_err:
            tp.insertPlainText(
                f"Number of syntax errors: {handleError.syntax_err}\n")
            tp.insertPlainText(handleError.syntax_err_descript)
        if handleError.syntax_err:
            tp.insertPlainText(
                f"Number of syntax errors: {handleError.syntax_err}\n")
            tp.insertPlainText(handleError.syntax_err_descript)
        if not handleError.syntax_err and not handleError.syntax_err:
            tp.insertPlainText("Build Successfully")
            tp.insertPlainText("\n")

    def openFile(self, editor):
        fileSelected = QFileDialog.getOpenFileName()
        path = fileSelected[0]
        print(path)
        with open(path, 'r') as f:
            editor.setPlainText(f.read())

# Main Component
class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Dart Analyzer G6"
        self.geometry = (100, 100, 900, 600)
        self.setStyleSheet("background-color: #E5E8ED;")
        self.mountComponents()

    def mountComponents(self):
        self.setWindowTitle(self.title)
        codeLabel = CodeLabel()
        titulo = QLabel()
        titulo.setText("Analizador Dart")
        titulo.setStyleSheet("font-size: 16px; font-weight: bold; text-align: center;")
        layout_v1 = QHBoxLayout()
        layout_v2 = QHBoxLayout()
        layout_v1.addWidget(titulo)
        layout_v1.setAlignment(Qt.AlignCenter)
        layout_v2.addWidget(codeLabel)
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout_v1)
        main_layout.addLayout(layout_v2)
        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainApp()
    mainWindow.show()
    app.exec_()
