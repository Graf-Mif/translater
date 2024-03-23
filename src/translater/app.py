"""
this is a translater 
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import tkinter as tk
import pyperclip

TRANSLATION_TABLE = {
    'а': '5',
    'б': '4',
    'в': '9',
    'г': '6',
    'д': '3',
    'е': '7',
    'Ё': '+',
    'ж': '*',
    'з': '%',
    'и': '№',
    'к': '"',
    'л': ';',
    'м': '!',
    'н': '2',
    'о': '8',
    'п': '0',
    'р': '=',
    'с': '-',
    'т': '1',
    'й': ':',
    'у': '@',
    'ф': '&',
    'х': '?',
    'ц': '$',
    'ч': '<',
    'щ': '~',
    'ъ': '+',
    'ь': '/',
    'э': ']',
    'ю': "'",
    'я': '>',
    'ы': '`',
}

REVERSE_TRANSLATION_TABLE = {v: k for k, v in TRANSLATION_TABLE.items()}

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Letter Substitution Translator")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter text to translate:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack(pady=10)

        self.translate_button = tk.Button(self.master, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.copy_button = tk.Button(self.master, text="Copy", command=self.copy_text)
        self.copy_button.pack(pady=10)

        self.reverse_button = tk.Button(self.master, text="Reverse translation", command=self.reverse_translation)
        self.reverse_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def translate_text(self):
        text = self.entry.get()
        translated_text = "".join([TRANSLATION_TABLE.get(c.lower(), c) for c in text])
        self.result_label.config(text=translated_text)

    def copy_text(self):
        pyperclip.copy(self.result_label.cget("text"))

    def reverse_translation(self):
        text = self.result_label.cget("text")
        reversed_text = "".join([REVERSE_TRANSLATION_TABLE.get(c, c) for c in text])
        self.result_label.config(text=reversed_text)

root = tk.Tk()
app = Application(master=root)
app.mainloop()


class translater(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return translater()
