import base64

import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import LEFT, NO, DISABLED, NORMAL

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class MainWindow(tk.Frame):

    zakodovany_soubor = "super_secure.tjn"

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Moje klíčenka")

        self.odemceno = False
        self.entry_width = 30
        self.zamikatelna_tlacitka = []

        self.parent.protocol("WM_DELETE_WINDOW", self.uloz_zaznamy)
        self.create_widgets()
        self.nacti_zaznamy()

    def create_widgets(self):
        self.label_jmeno = tk.Label(text="Zadejte hlavní heslo (klíč)",
                                    width=50)
        self.label_jmeno.pack()
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

        self.frame_zaznam = tk.Frame()
        self.frame_zaznam.pack()

        self.stranka = StringVar()
        self.entry_stranka = ttk.Entry(self.frame_zaznam, width=self.entry_width,
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
                                        command=self.pridej,
                                        )
        self.pridej_button.pack(side=LEFT)
        self.zamikatelna_tlacitka.append(self.pridej_button)


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

        self.frame_seznam_tlacitka = tk.Frame()
        self.frame_seznam_tlacitka.pack()
        self.smaz_button = ttk.Button(self.frame_seznam_tlacitka,
                                      text="Smazat záznam",
                                      state=DISABLED,
                                      command=self.smaz)
        self.zamikatelna_tlacitka.append(self.smaz_button)
        self.smaz_button.pack()

    def pridej(self):
        self.tree_zaznamy.insert("", "end",
                                 text=f"{len(self.tree_zaznamy.get_children())}",
                                 values=(str(self.stranka.get()),
                                         str(self.jmeno.get()),
                                         str(self.heslo.get())))
        self.stranka.set("")
        self.jmeno.set("")
        self.heslo.set("")

    def smaz(self):
        if self.tree_zaznamy.focus():
            self.tree_zaznamy.delete(self.tree_zaznamy.focus())

    def odezamkni_klicenku(self):
        if self.odemceno:
            self.unlock_button.config(text="Odemknout")
            self.odemceno = not self.odemceno
            self.odezamkni_tlacitka(DISABLED)
            self.zakoduj_zaznamy()
            self.master_heslo.set("")
            self.entry_master_heslo.config(state=NORMAL)
        else:
            self.priprav_klic()
            try:
                self.odkoduj_zaznamy()
            except InvalidToken:
                return
            self.unlock_button.config(text="Zamknout")
            self.odemceno = not self.odemceno
            self.odezamkni_tlacitka(NORMAL)

            self.entry_master_heslo.config(state=DISABLED)


    def priprav_klic(self):
        psswd = self.master_heslo.get().encode()
        salt = b"/*-*/"
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.klic = base64.urlsafe_b64encode(kdf.derive(psswd))
        print(self.klic)

    def zakoduj_zaznamy(self):

        f = Fernet(self.klic)
        for ii in self.tree_zaznamy.get_children():
            # nasledujici radka odhaluje bug v tkinter, values jsou "tajne"
            # konvertovany z řetězců na čísla
            # https://stackoverflow.com/questions/51941260/tkinter-treeview-row-display-value-discrepancy-with-underscore
            # stranka, jmeno, heslo = self.tree_zaznamy.item(ii)["values"]

            # nasledujici radka spoleha na jiny bug, kvuli kteremu konverze nenastane
            stranka, jmeno, heslo = self.tree_zaznamy.item(ii, option="values")

            self.tree_zaznamy.item(ii, values=(f.encrypt(stranka.encode()).decode("utf-8"),
                                               f.encrypt(jmeno.encode()).decode("utf-8"),
                                               f.encrypt(heslo.encode()).decode("utf-8")))

    def odkoduj_zaznamy(self):
        f = Fernet(self.klic)
        for ii in self.tree_zaznamy.get_children():
            stranka, jmeno, heslo = self.tree_zaznamy.item(ii, option="values")
            self.tree_zaznamy.item(ii, values=(f.decrypt(stranka.encode()).decode("utf-8"),
                                               f.decrypt(jmeno.encode()).decode("utf-8"),
                                               f.decrypt(heslo.encode()).decode("utf-8")))

    def odezamkni_tlacitka(self, state):
        for tlacitko in self.zamikatelna_tlacitka:
            tlacitko.config(state=state)

    def uloz_zaznamy(self):
        if self.odemceno:
            self.odezamkni_klicenku()
        with open(self.zakodovany_soubor, "w") as soubor:
            for ii in self.tree_zaznamy.get_children():
                stranka, jmeno, heslo = self.tree_zaznamy.item(ii, option="values")
                print(stranka,
                      jmeno,
                      heslo, file=soubor)
            self.parent.destroy()

    def nacti_zaznamy(self):
        try:
            with open(self.zakodovany_soubor, "r") as soubor:
                for l in soubor:
                    self.tree_zaznamy.insert("", "end",
                                             text=f"{len(self.tree_zaznamy.get_children())}",
                                             values=(l.split()))
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    app.mainloop()
