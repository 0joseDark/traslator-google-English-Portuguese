import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Combobox
from googletrans import Translator

# Dictionary of supported languages
LANGUAGES = {
    "Afrikaans": "af", "Albanian": "sq", "German": "de", "Amharic": "am", "Arabic": "ar",
    "Armenian": "hy", "Azerbaijani": "az", "Basque": "eu", "Bengali": "bn", "Belarusian": "be",
    "Burmese": "my", "Bulgarian": "bg", "Catalan": "ca", "Cebuano": "ceb", "Chichewa": "ny",
    "Simplified Chinese": "zh-CN", "Traditional Chinese": "zh-TW", "Sinhala": "si", "Korean": "ko",
    "Corsican": "co", "Croatian": "hr", "Danish": "da", "Slovak": "sk", "Slovenian": "sl",
    "Spanish": "es", "Esperanto": "eo", "Estonian": "et", "Filipino": "tl", "Finnish": "fi",
    "French": "fr", "Frisian": "fy", "Galician": "gl", "Welsh": "cy", "Georgian": "ka",
    "Greek": "el", "Gujarati": "gu", "Hausa": "ha", "Hawaiian": "haw", "Hebrew": "he",
    "Hindi": "hi", "Hmong": "hmn", "Dutch": "nl", "Hungarian": "hu", "Igbo": "ig",
    "Indonesian": "id", "English": "en", "Irish": "ga", "Icelandic": "is", "Italian": "it",
    "Japanese": "ja", "Javanese": "jw", "Kannada": "kn", "Kazakh": "kk", "Khmer": "km",
    "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt",
    "Luxembourgish": "lb", "Macedonian": "mk", "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml",
    "Maltese": "mt", "Maori": "mi", "Marathi": "mr", "Mongolian": "mn", "Nepali": "ne",
    "Norwegian": "no", "Odia": "or", "Pashto": "ps", "Persian": "fa", "Polish": "pl",
    "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro", "Russian": "ru", "Samoan": "sm",
    "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd", "Somali": "so",
    "Swahili": "sw", "Swedish": "sv", "Tagalog": "tl", "Tajik": "tg", "Tamil": "ta",
    "Tatar": "tt", "Telugu": "te", "Thai": "th", "Turkish": "tr", "Ukrainian": "uk",
    "Urdu": "ur", "Uzbek": "uz", "Vietnamese": "vi", "Xhosa": "xh", "Yiddish": "yi",
    "Yoruba": "yo", "Zulu": "zu"
}

# Function to translate text files
def translate_files():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    source_lang = LANGUAGES[first_language_var.get()]
    target_lang = LANGUAGES[second_language_var.get()]

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders!")
        return
    if source_lang == target_lang:
        messagebox.showerror("Error", "Source and target languages must be different!")
        return

    files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]
    if not files:
        messagebox.showinfo("Info", "No .txt files found in the input folder.")
        return

    total_files = len(files)
    progress["value"] = 0
    window.update_idletasks()

    translator = Translator()

    for i, file in enumerate(files, start=1):
        input_path = os.path.join(input_folder, file)
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                content = f.read()

            translation = translator.translate(content, src=source_lang, dest=target_lang).text

            new_name = f"{i:03d}_translated.txt"
            output_path = os.path.join(output_folder, new_name)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(translation)

        except Exception as e:
            messagebox.showwarning("Warning", f"Error translating {file}: {e}")

        progress["value"] = (i / total_files) * 100
        window.update_idletasks()

    messagebox.showinfo("Completed", "Translation completed successfully!")

# Functions to choose input and output folders
def choose_input_folder():
    folder = filedialog.askdirectory(title="Select Input Folder")
    if folder:
        input_folder_var.set(folder)

def choose_output_folder():
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        output_folder_var.set(folder)

# Setting up the main window
window = tk.Tk()
window.title("Text Translator")
window.geometry("500x600")
window.resizable(False, False)

# Variables for folder paths and languages
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
first_language_var = tk.StringVar(value="English")
second_language_var = tk.StringVar(value="Portuguese")

# User interface
tk.Label(window, text="Text Translator", font=("Arial", 16)).pack(pady=10)
tk.Label(window, text="Choose input and output folders:").pack(pady=5)

frame_input = tk.Frame(window)
frame_input.pack(pady=5)
input_entry = tk.Entry(frame_input, textvariable=input_folder_var, width=40, state="readonly")
input_entry.pack(side="left", padx=5)
input_button = tk.Button(frame_input, text="Input Folder", command=choose_input_folder)
input_button.pack(side="left", padx=5)

frame_output = tk.Frame(window)
frame_output.pack(pady=5)
output_entry = tk.Entry(frame_output, textvariable=output_folder_var, width=40, state="readonly")
output_entry.pack(side="left", padx=5)
output_button = tk.Button(frame_output, text="Output Folder", command=choose_output_folder)
output_button.pack(side="left", padx=5)

tk.Label(window, text="Select Source Language:").pack(pady=5)
source_language_combo = Combobox(window, values=list(LANGUAGES.keys()), textvariable=first_language_var, state="readonly")
source_language_combo.pack(pady=5)

tk.Label(window, text="Select Target Language:").pack(pady=5)
target_language_combo = Combobox(window, values=list(LANGUAGES.keys()), textvariable=second_language_var, state="readonly")
target_language_combo.pack(pady=5)

progress = Progressbar(window, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=20)

translate_button = tk.Button(window, text="Translate", command=translate_files)
translate_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=5)

window.mainloop()
