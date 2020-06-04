import base64

import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import LEFT, NO, DISABLED, NORMAL

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Klicenka:

    def __init__(self):
        self.odemceno = False

    ...


class KlicenkaGUI(tk.Frame):

    def __init__(self, parent, klicenka):
        super().__init__(parent)
        self.parent = parent
        self.klicenka = klicenka
        self.parent.title("Moje klíčenka")

        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()

    def create_widgets(self):
        ...

    def on_close(self):
        ...
        self.parent.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    klicenka = Klicenka()
    app = KlicenkaGUI(root, klicenka)
    app.mainloop()
