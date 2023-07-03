from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from lexico import *
from sintactico import *

# Editor Code Component
class DartEditorCode(QPlainTextEdit):

    class NumberBar(QWidget):
        def _init_(self, editor):
            QWidget._init_(self, editor)

            self.editor = editor
            self.editor.blockCountChanged.connect(self.updateWidth)
            self.editor.updateRequest.connect(self.updateContents)
            self.font = QFont()
            self.numberBarColor = QColor("#2F2F36")

        def paintEvent(self, event):

            painter = QPainter(self)
            painter.fillRect(event.rect(), self.numberBarColor)

            block = self.editor.firstVisibleBlock()

            while block.isValid():
                blockNumber = block.blockNumber()
                block_top = self.editor.blockBoundingGeometry(
                    block).translated(self.editor.contentOffset()).top()

                if not block.isVisible() or block_top >= event.rect().bottom():
                    break

                if blockNumber == self.editor.textCursor().blockNumber():
                    self.font.setBold(True)
                    painter.setPen(QColor("#2F2F36"))
                else:
                    self.font.setBold(False)
                    painter.setPen(QColor("#2F2F36"))
                painter.setFont(self.font)

                paint_rect = QRect(0, block_top, self.width(),
                                   self.editor.fontMetrics().height())
                painter.drawText(paint_rect, Qt.AlignRight, str(blockNumber+1))

                block = block.next()

            painter.end()

            QWidget.paintEvent(self, event)

        def getWidth(self):
            count = self.editor.blockCount()
            width = self.fontMetrics().width(str(count)) + 10
            return width

        def updateWidth(self):
            width = self.getWidth()
            if self.width() != width:
                self.setFixedWidth(width)
                self.editor.setViewportMargins(width, 0, 0, 0)

        def updateContents(self, rect, scroll):
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update(0, rect.y(), self.width(), rect.height())

            if rect.contains(self.editor.viewport().rect()):
                fontSize = self.editor.currentCharFormat().font().pointSize()
                self.font.setPointSize(fontSize)
                self.font.setStyle(QFont.StyleNormal)
                self.updateWidth()

    def _init_(self, DISPLAY_LINE_NUMBERS=True, HIGHLIGHT_CURRENT_LINE=True):
        super(DartEditorCode, self)._init_()

        self.setFont(QFont("Ubuntu Mono", 11))
        self.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.DISPLAY_LINE_NUMBERS = DISPLAY_LINE_NUMBERS

        if DISPLAY_LINE_NUMBERS:
            self.number_bar = self.NumberBar(self)

        if HIGHLIGHT_CURRENT_LINE:
            self.currentLineNumber = None
            self.currentLineColor = QColor("#FDFDFD")
            self.cursorPositionChanged.connect(self.highligtCurrentLine)

    def resizeEvent(self, *e):

        if self.DISPLAY_LINE_NUMBERS:
            cr = self.contentsRect()
            rec = QRect(cr.left(), cr.top(),
                        self.number_bar.getWidth(), cr.height())
            self.number_bar.setGeometry(rec)

        QPlainTextEdit.resizeEvent(self, *e)

    def highligtCurrentLine(self):
        newCurrentLineNumber = self.textCursor().blockNumber()
        if newCurrentLineNumber != self.currentLineNumber:
            self.currentLineNumber = newCurrentLineNumber
            hi_selection = QTextEdit.ExtraSelection()
            hi_selection.format.setBackground(self.currentLineColor)
            hi_selection.format.setProperty(
                QTextFormat.FullWidthSelection, True)
            hi_selection.cursor = self.textCursor()
            hi_selection.cursor.clearSelection()
            self.setExtraSelections([hi_selection])

# Label Code Component
class CodeLabel(QWidget):
    def _init_(self):
        super(CodeLabel, self)._init_()
        layout = QHBoxLayout()
        label1_txt = QLabel()
        label1_txt.setText("<h4>Write or Paste your copy here: </h4>")
        layout.addWidget(label1_txt)
        self.setLayout(layout)

# Print Label Component
class PrintLabel(QWidget):

    def _init_(self):
        super(PrintLabel, self)._init_()
        vb = QVBoxLayout()
        hb_layout = QHBoxLayout()
        label_text = QLabel()
        plain_text = QPlainTextEdit()

        label_text.setText("Execution <strong> Result Analysis </strong>")
        label_text.setStyleSheet("color: #2D2D2D;")
        
        plain_text.setReadOnly(True)
        plain_text.setStyleSheet("background-color: #E5E8ED;")

        hb_layout.addWidget(label_text)
        hb_layout.addStretch(1)

        vb.addLayout(hb_layout)
        vb.addWidget(plain_text)
        self.setLayout(vb)


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

