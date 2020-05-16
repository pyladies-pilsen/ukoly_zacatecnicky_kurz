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
        self.obsah = []
        self.nacti_zaznamy()
        self.odemceno = False

    def odemkni(self, heslo):
        self.klic = self._priprav_klic(heslo)
        try:
            self._odkoduj_zaznamy()
        except InvalidToken:
            return False
        self.odemceno = True
        return True

    def zamkni(self):
        self._zakoduj_zaznamy()
        self.odemceno = False
        self.klic = ""

    def pridej_zaznam(self, zaznam):
        if not self.odemceno:
            raise IndexError("Klicenka je zamcena, nelze pridat zaznam" +
                             f"{zaznam}")
        self.obsah.append({"stranka": zaznam[0],
                           "jmeno": zaznam[1],
                           "heslo": zaznam[2]})

    def smaz_zaznam(self, index):
        if not self.odemceno:
            raise IndexError("Klicenka je zamcena, nelze smazat zaznam" +
                             f"{index}")
        else:
            self.obsah.pop(index)

    def uloz_zaznamy(self):
        if self.odemceno:
            self._zakoduj_zaznamy()

        with open(self.tajny_soubor, "w", encoding="utf-8") as soubor:
            for zaznam in self.obsah:
                stranka, jmeno, heslo = zaznam.values()
                print(stranka,
                      jmeno,
                      heslo, file=soubor)

        if self.odemceno:
            self._odkoduj_zaznamy()

    def nacti_zaznamy(self):
        try:
            with open(self.tajny_soubor, "r", encoding="utf-8") as soubor:
                for l in soubor:
                    zaznam = l.split()
                    self.obsah.append({"stranka": zaznam[0],
                                       "jmeno": zaznam[1],
                                       "heslo": zaznam[2]})
        except FileNotFoundError:
            pass

    def _zakoduj_zaznamy(self):
        f = Fernet(self.klic)
        for zaznam in self.obsah:
            zaznam["stranka"] = f.encrypt(zaznam["stranka"].encode()).decode("utf-8")
            zaznam["jmeno"] = f.encrypt(zaznam["jmeno"].encode()).decode("utf-8")
            zaznam["heslo"] = f.encrypt(zaznam["heslo"].encode()).decode("utf-8")

    def _odkoduj_zaznamy(self):
        f = Fernet(self.klic)
        for zaznam in self.obsah:
            zaznam["stranka"] = f.decrypt(zaznam["stranka"].encode()).decode("utf-8")
            zaznam["jmeno"] = f.decrypt(zaznam["jmeno"].encode()).decode("utf-8")
            zaznam["heslo"] = f.decrypt(zaznam["heslo"].encode()).decode("utf-8")

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
        self.zamikatelna_tlacitka = []

        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()

        self.synchronizuj()

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
        self.unlock_button = ttk.Button(self.frame_ovladani,
                                        text="Odemknout",
                                        command=self.odezamkni_klicenku)
        self.entry_master_heslo.pack(side=LEFT)
        self.unlock_button.pack(side=LEFT)

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
                                         columns=("Stránka", "Jméno", "Heslo"))
        self.tree_zaznamy.heading("#0", text="#")
        self.tree_zaznamy.column("#0", minwidth=0, width=30, stretch=NO)
        self.tree_zaznamy.heading("Stránka", text="Stránka")
        self.tree_zaznamy.column("Stránka", minwidth=0, width=200, stretch=NO)
        self.tree_zaznamy.heading("Jméno", text="Jméno")
        self.tree_zaznamy.column("Jméno", minwidth=0, width=300)
        self.tree_zaznamy.heading("Heslo", text="Heslo")
        self.tree_zaznamy.column("Heslo", minwidth=0, width=300)
        self.tree_zaznamy.pack()

        # Mazani zaznamu
        self.frame_seznam_tlacitka = tk.Frame()
        self.frame_seznam_tlacitka.pack()
        self.smaz_button = ttk.Button(self.frame_seznam_tlacitka,
                                      text="Smazat záznam",
                                      state=DISABLED,
                                      command=self.on_smaz)
        self.zamikatelna_tlacitka.append(self.smaz_button)
        self.smaz_button.pack()

    def odezamkni_klicenku(self):
        if self.klicenka.odemceno:
            # zamkni
            self.klicenka.zamkni()
            self.master_heslo.set("")
            self.synchronizuj()
            self.unlock_button.config(text="Odemknout")
            self.pridej_button.config(state=DISABLED)
            self.smaz_button.config(state=DISABLED)
            self.entry_master_heslo.config(state=NORMAL)
        else:
            # odemkni
            self.klicenka.odemkni(self.master_heslo.get())
            if self.klicenka.odemceno:
                self.synchronizuj()
                self.unlock_button.config(text="Zamknout")
                self.pridej_button.config(state=NORMAL)
                self.smaz_button.config(state=NORMAL)
                self.entry_master_heslo.config(state=DISABLED)

    def synchronizuj(self):

        for ii in self.tree_zaznamy.get_children():
            self.tree_zaznamy.delete(ii)

        for zaznam in self.klicenka.obsah:
            self.tree_zaznamy.insert("", "end",
                                 text=f"{len(self.tree_zaznamy.get_children())}",
                                 values=(zaznam["stranka"],
                                         zaznam["jmeno"],
                                         zaznam["heslo"]))

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
        self.synchronizuj()

    def on_smaz(self):
        if self.tree_zaznamy.focus():
            index = int(self.tree_zaznamy.item(self.tree_zaznamy.focus())["text"])
            self.klicenka.smaz_zaznam(index)
            self.synchronizuj()

    def on_close(self):
        self.klicenka.uloz_zaznamy()
        self.parent.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    klicenka = Klicenka()
    app = KlicenkaGUI(root, klicenka)
    app.mainloop()
