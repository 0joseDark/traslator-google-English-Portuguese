- ![translator](https://github.com/0joseDark/traslator-google-English-Portuguese-Indian/blob/main/imadens/image.jpg)
# translator-google-English-Portuguese-Indian
**Text File Translator with Graphical Interface** on Windows 10. This translator allows you to:

1. Select the **input folder** and the **output folder**.
2. Choose the **first language** (source) and the **second language** (target) from a list of options: *English, European Portuguese, Indian*.
3. Translate `.txt` files from the input folder to the target language and save them in the output folder.

### Step-by-Step

1. **Module Imports**:
   - `os`: For file and folder management.
   - `tkinter` and `ttk`: For the graphical interface.
   - `googletrans`: For text translation.
   - `Combobox`: For language selection.

2. **Interface Functions**:
   - `choose_input_folder` and `choose_output_folder`: Use `filedialog` to select folders.
   - `translate_files`: Manages the translation and updates the progress bar.

3. **Language Dictionary**:
   - Defines the supported languages by ISO code.

4. **Graphical Interface**:
   - Fields to select folders.
   - Combobox to select source and target languages.
   - Progress bar to track the translation progress.

5. **Execution**:
   - Translated files are saved with the `_translated` suffix in the output folder.
### Dependencies

Install the `googletrans` module before running the code:

```bash
pip install googletrans==4.0.0-rc1
---
