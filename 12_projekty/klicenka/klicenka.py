import base64

import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import LEFT, NO, DISABLED, NORMAL

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Klicenka:

    tajny_soubor = "super_secure.tjn"

    def __init__(self):
        self.zaznamy = []
        self.nacti_zaznamy()
        self.odemceno = False

    def odemknout(self, heslo):
        self.klic = self._priprav_klic(heslo)
        try:
            self._odkoduj_zaznamy()
        except InvalidToken:
            return False
        self.odemceno = True
        return True

    def zamknout(self):
        self._zakoduj_zaznamy()
        self.odemceno = False
        self.klic = ""

    def pridej_zaznam(self, zaznam):
        if not self.odemceno:
            raise IndexError("Klicenka je zamcena, nelze pridat zaznam" +
                             f"{zaznam}")
        self.zaznamy.append(zaznam)

    def smaz_zaznam(self, index):
        if not self.odemceno:
            raise IndexError("Klicenka je zamcena, nelze smazat zaznam" +
                             f"{index}")
        else:
            self.zaznamy.pop(index)

    def uloz_zaznamy(self):
        if self.odemceno:
            self._zakoduj_zaznamy()

        with open(self.tajny_soubor, "w", encoding="utf-8") as soubor:
            for stranka, jmeno, heslo in self.zaznamy:
                print(stranka, jmeno, heslo, file=soubor)

        if self.odemceno:
            self._odkoduj_zaznamy()

    def nacti_zaznamy(self):
        try:
            with open(self.tajny_soubor, "r", encoding="utf-8") as soubor:
                for l in soubor:
                    zaznam = l.split()
                    self.zaznamy.append(zaznam)
        except FileNotFoundError:
            pass

    def _zakoduj_zaznamy(self):
        f = Fernet(self.klic)
        zasifrovane_zaznamy = []
        for stranka, jmeno, heslo in self.zaznamy:
            zasifrovany_zaznam = (f.encrypt(stranka.encode()).decode("utf-8"),
                                  f.encrypt(jmeno.encode()).decode("utf-8"),
                                  f.encrypt(heslo.encode()).decode("utf-8"))
            zasifrovane_zaznamy.append(zasifrovany_zaznam)

        self.zaznamy = zasifrovane_zaznamy

    def _odkoduj_zaznamy(self):
        f = Fernet(self.klic)
        ozaznamy = []
        for stranka, jmeno, heslo in self.zaznamy:
            zaznam = (f.decrypt(stranka.encode()).decode("utf-8"),
                      f.decrypt(jmeno.encode()).decode("utf-8"),
                      f.decrypt(heslo.encode()).decode("utf-8"))
            ozaznamy.append(zaznam)

        self.zaznamy = ozaznamy

    def _priprav_klic(self, heslo):
        salt = b"/*-*/"
        kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(heslo.encode()))


class KlicenkaGUI(tk.Frame):

    def __init__(self, parent, klicenka):
        super().__init__(parent)
        self.parent = parent
        self.klicenka = klicenka
        self.parent.title("Moje klíčenka")

        self.entry_width = 30

        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()

        self.zobraz()

    def create_widgets(self):
        self.label_jmeno = tk.Label(text="Zadejte hlavní heslo (klíč)",
                                    width=50)
        self.label_jmeno.pack()

        # Hlavni heslo
        self.frame_ovladani = tk.Frame()
        self.frame_ovladani.pack()

        self.master_heslo = StringVar()
        self.master_heslo.set("")
        self.entry_master_heslo = ttk.Entry(self.frame_ovladani,
                                            width=self.entry_width,
                                            textvariable=self.master_heslo)
        self.odezamkni_button = ttk.Button(self.frame_ovladani,
                                           text="Odemknout",
                                           command=self.odezamkni_klicenku)
        self.entry_master_heslo.pack(side=LEFT)
        self.odezamkni_button.pack(side=LEFT)

        # Pridavani zaznamu
        self.frame_zaznam = tk.Frame()
        self.frame_zaznam.pack()

        self.stranka = StringVar()
        self.entry_stranka = ttk.Entry(self.frame_zaznam,
                                       width=self.entry_width,
                                       textvariable=self.stranka)
        self.entry_stranka.pack(side=LEFT)

        self.jmeno = StringVar()
        self.entry_jmeno = ttk.Entry(self.frame_zaznam, width=self.entry_width,
                                     textvariable=self.jmeno)
        self.entry_jmeno.pack(side=LEFT)

        self.heslo = StringVar()
        self.entry_heslo = ttk.Entry(self.frame_zaznam, width=self.entry_width,
                                     textvariable=self.heslo)

        self.entry_heslo.pack(side=LEFT)
        self.pridej_button = ttk.Button(self.frame_zaznam,
                                        text="Přidat",
                                        state=DISABLED,
                                        command=self.on_pridej,
                                        )
        self.pridej_button.pack(side=LEFT)

        # Seznam zaznamu
        self.frame_seznam = tk.Frame()
        self.frame_seznam.pack()
        self.tree_zaznamy = ttk.Treeview(self.frame_seznam,
                                         columns=("stranka", "jmeno", "heslo"))
        self.tree_zaznamy.heading("#0", text="#")
        self.tree_zaznamy.column("#0", minwidth=0, width=30, stretch=NO)
        self.tree_zaznamy.heading("stranka", text="Stránka")
        self.tree_zaznamy.column("stranka", minwidth=0, width=200, stretch=NO)
        self.tree_zaznamy.heading("jmeno", text="Jméno")
        self.tree_zaznamy.column("jmeno", minwidth=0, width=300)
        self.tree_zaznamy.heading("heslo", text="Heslo")
        self.tree_zaznamy.column("heslo", minwidth=0, width=300)
        self.tree_zaznamy.pack()

        # Mazani zaznamu
        self.frame_seznam_tlacitka = tk.Frame()
        self.frame_seznam_tlacitka.pack()
        self.smaz_button = ttk.Button(self.frame_seznam_tlacitka,
                                      text="Smazat záznam",
                                      state=DISABLED,
                                      command=self.on_smaz)
        self.smaz_button.pack()

    def odezamkni_klicenku(self):
        if self.klicenka.odemceno:
            # zamknout
            self.klicenka.zamknout()
            self.master_heslo.set("")
            self.zobraz()
            self.odezamkni_button.config(text="Odemknout")
            self.pridej_button.config(state=DISABLED)
            self.smaz_button.config(state=DISABLED)
            self.entry_master_heslo.config(state=NORMAL)
        else: # je zamceno
            if self.master_heslo.get() == "":
                return

            self.klicenka.odemknout(self.master_heslo.get())
            if self.klicenka.odemceno:
                self.odezamkni_button.config(text="Zamknout")
                self.pridej_button.config(state=NORMAL)
                self.smaz_button.config(state=NORMAL)
                self.entry_master_heslo.config(state=DISABLED)
                self.zobraz()


    def zobraz(self):

        for ii in self.tree_zaznamy.get_children():
            self.tree_zaznamy.delete(ii)

        for zaznam in self.klicenka.zaznamy:
            self.tree_zaznamy.insert("", "end",
                                 text=f"{len(self.tree_zaznamy.get_children())}",
                                 values=zaznam)

    def on_pridej(self):
        zaznam = (self.stranka.get(),
                  self.jmeno.get(),
                  self.heslo.get())

        if sum(len(z) for z in zaznam) == 0:
            return

        self.klicenka.pridej_zaznam(zaznam)
        self.stranka.set("")
        self.jmeno.set("")
        self.heslo.set("")
        self.zobraz()

    def on_smaz(self):
        if self.tree_zaznamy.focus():
            index = int(self.tree_zaznamy.item(self.tree_zaznamy.focus())["text"])
            self.klicenka.smaz_zaznam(index)
            self.zobraz()

    def on_close(self):
        self.klicenka.uloz_zaznamy()
        self.parent.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    klicenka = Klicenka()
    app = KlicenkaGUI(root, klicenka)
    app.mainloop()
