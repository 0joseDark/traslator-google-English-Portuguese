import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Combobox
from googletrans import Translator
from PyPDF2 import PdfReader
import markdown

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

# Function to translate PDF content to Markdown
def translate_pdf_to_md():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    source_lang = LANGUAGES[source_lang_var.get()]
    target_lang = LANGUAGES[target_lang_var.get()]

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Select input and output folders!")
        return
    if source_lang == target_lang:
        messagebox.showerror("Error", "Choose different languages for translation!")
        return

    pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]
    if not pdf_files:
        messagebox.showinfo("Info", "No PDF files found in the input folder.")
        return

    translator = Translator()
    total_files = len(pdf_files)
    progress["value"] = 0
    window.update_idletasks()

    for i, pdf_file in enumerate(pdf_files, start=1):
        input_path = os.path.join(input_folder, pdf_file)
        try:
            reader = PdfReader(input_path)
            full_text = " ".join(page.extract_text() for page in reader.pages)
            translated_text = translator.translate(full_text, src=source_lang, dest=target_lang).text

            markdown_content = markdown.markdown(translated_text)
            output_file = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}_translated.md")
            with open(output_file, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_content)

        except Exception as e:
            messagebox.showwarning("Warning", f"Error translating {pdf_file}: {e}")

        progress["value"] = (i / total_files) * 100
        window.update_idletasks()

    messagebox.showinfo("Completed", "PDF translation completed!")

# ... (The rest of the Tkinter UI setup remains the same, just updating function references)
