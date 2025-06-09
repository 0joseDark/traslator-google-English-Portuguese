from PyQt5 import QtWidgets
from deep_translator import GoogleTranslator

class TranslatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.input = QtWidgets.QTextEdit()
        self.output = QtWidgets.QTextEdit()
        btn = QtWidgets.QPushButton("Traduzir")
        btn.clicked.connect(self.translate_text)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(btn)
        layout.addWidget(self.output)
        self.setLayout(layout)
        self.setWindowTitle("Tradutor PT↔EN")

    def translate_text(self):
        src = self.input.toPlainText()
        # Detectar automaticamente
        result = GoogleTranslator(source="auto", target="pt").translate(src)
        self.output.setPlainText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = TranslatorApp()
    win.show()
    app.exec()
