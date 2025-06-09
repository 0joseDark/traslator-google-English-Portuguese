O script traduz ficheiros `.txt` de uma pasta para outra, usando o **Google Translate** via a biblioteca `googletrans`.
---

## ✅ Versão com GUI em PyQt5 (para macOS, Windows e Ubuntu)

Abaixo está o **script convertido para usar PyQt5** com comentários passo a passo, mantendo todas as funcionalidades:

---

### 🧠 Script comentado: `qt_translator.py`

```python
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QProgressBar,
    QFileDialog, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
)
from googletrans import Translator

# Dicionário com idiomas disponíveis e seus códigos
LANGUAGES = {
    "English": "en", "Portuguese": "pt", "Spanish": "es", "French": "fr",
    "German": "de", "Italian": "it", "Dutch": "nl", "Chinese": "zh-CN", "Japanese": "ja"
    # Adicione mais conforme necessário
}

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Título e tamanho da janela
        self.setWindowTitle("Text Translator (Qt)")
        self.setFixedSize(500, 400)

        # Entradas e botões
        self.input_path = QLineEdit(self)
        self.input_path.setReadOnly(True)
        input_button = QPushButton("Input Folder")
        input_button.clicked.connect(self.choose_input_folder)

        self.output_path = QLineEdit(self)
        self.output_path.setReadOnly(True)
        output_button = QPushButton("Output Folder")
        output_button.clicked.connect(self.choose_output_folder)

        self.source_lang = QComboBox(self)
        self.source_lang.addItems(LANGUAGES.keys())
        self.source_lang.setCurrentText("English")

        self.target_lang = QComboBox(self)
        self.target_lang.addItems(LANGUAGES.keys())
        self.target_lang.setCurrentText("Portuguese")

        self.progress = QProgressBar(self)

        translate_button = QPushButton("Translate")
        translate_button.clicked.connect(self.translate_files)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Select Input Folder:"))
        h1 = QHBoxLayout()
        h1.addWidget(self.input_path)
        h1.addWidget(input_button)
        layout.addLayout(h1)

        layout.addWidget(QLabel("Select Output Folder:"))
        h2 = QHBoxLayout()
        h2.addWidget(self.output_path)
        h2.addWidget(output_button)
        layout.addLayout(h2)

        layout.addWidget(QLabel("Source Language:"))
        layout.addWidget(self.source_lang)

        layout.addWidget(QLabel("Target Language:"))
        layout.addWidget(self.target_lang)

        layout.addWidget(self.progress)
        layout.addWidget(translate_button)
        layout.addWidget(exit_button)

        self.setLayout(layout)

    def choose_input_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Input Folder")
        if folder:
            self.input_path.setText(folder)

    def choose_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.output_path.setText(folder)

    def translate_files(self):
        input_folder = self.input_path.text()
        output_folder = self.output_path.text()
        src_lang = LANGUAGES[self.source_lang.currentText()]
        tgt_lang = LANGUAGES[self.target_lang.currentText()]

        if not input_folder or not output_folder:
            QMessageBox.warning(self, "Error", "Please select both folders.")
            return
        if src_lang == tgt_lang:
            QMessageBox.warning(self, "Error", "Source and target languages must be different.")
            return

        files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]
        if not files:
            QMessageBox.information(self, "Info", "No .txt files found.")
            return

        translator = Translator()
        total = len(files)

        for i, filename in enumerate(files, 1):
            try:
                with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                    content = f.read()

                translated = translator.translate(content, src=src_lang, dest=tgt_lang).text
                new_name = f"{i:03d}_translated.txt"
                with open(os.path.join(output_folder, new_name), "w", encoding="utf-8") as f:
                    f.write(translated)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Error with {filename}: {e}")

            self.progress.setValue(int(i / total * 100))
            QApplication.processEvents()

        QMessageBox.information(self, "Done", "All files translated successfully!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    translator = TranslatorApp()
    translator.show()
    sys.exit(app.exec_())
```

---

## 💾 Como instalar (Windows 10, Ubuntu, macOS)

### 1. Instalar Python (3.8+ recomendado)

#### ✅ Windows

* Baixe em: [https://www.python.org](https://www.python.org)
* Durante a instalação: selecione **“Add Python to PATH”**

#### ✅ Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### ✅ macOS

```bash
brew install python
```

---

### 2. Instalar dependências

Execute num terminal (Windows: cmd/powershell, Ubuntu/macOS: terminal):

```bash
pip install PyQt5 googletrans==4.0.0-rc1
```

---

### ✅ Como executar

1. Salve o script como `qt_translator.py`
2. Execute:

```bash
python qt_translator.py
```

---
