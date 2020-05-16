"""
Ukázkový program pro tvorbu GUI k 1D piškvorkám v Tkinteru
"""

from tkinter import Tk, ttk, LEFT, Frame, StringVar
from oop_piskvorky_1D import Hra_piskvorek1D


# seznam vygenerovaných tlačítek představujících herní pole
tlacitka_hraciho_pole = []
# vnitřní reprezentace hry
piskvorky = Hra_piskvorek1D(10)


def priprava_hraciho_pole():
    """
    Pokud existují, smaže tlačítka, vyčistí seznam tlačítek z předchozí hry,
    vytvoří novou vnitřní reprezentaci hry a spustí generování tlačítek.
    """
    print("Přebírá textové zadání velikosti: ", velikost_hry.get())

    velikost_hry_int = int(velikost_hry.get())
    piskvorky.nova_hra(velikost_hry_int)

    # TODO: ošetřit vhodný rozsah herního pole
    for button in tlacitka_hraciho_pole:
        button.destroy()
    tlacitka_hraciho_pole.clear()

    generovani_tlacitek_hraciho_pole(velikost_hry_int)
    zprava.set("Klikněte na pole, na které chce hrát.")


def generovani_tlacitek_hraciho_pole(velikost_hry_int):
    """
    Dle zadání uživatele v textovém poli, generuje tlačítka představující
    herní pole.
    Odkazy na tlačítka uloží do proměnné buttons_hraciho_pole.
    """
    for i in range(velikost_hry_int):
        button_gen = ttk.Button(frame_hraci_pole, text="-", width=2)
        button_gen.configure(command=lambda i=i: obsluha_tahu_hrace(i))
        button_gen.pack(padx=2, pady=50, side=LEFT)
        tlacitka_hraciho_pole.append(button_gen)


def obsluha_tahu_hrace(pozice):
    """
    Obsahuje celý mechanismus hry piskvorek
    """
    print("Hráč kliknul na tlačítko: ", pozice)

    # v pripade ze uz se neda hrat nepokracujeme dale do funkce
    if piskvorky.vyhodnot() != "-":
        return

    # dale stejne jako v textové verzi, misto print mame zpravu v okne
    chyba = piskvorky.tah_hrace(pozice)

    if chyba is not None:
        zprava.set(chyba)
        return

    tlacitka_hraciho_pole[pozice].config(text="X")
    if piskvorky.vyhodnot() != "-":
        # vysledek vypiseme hned, pozdeji k tomu neni prilezitost
        zprava.set(piskvorky.zpravy[piskvorky.vyhodnot()])
        return


    tlacitka_hraciho_pole[piskvorky.tah_pocitace()].config(text="O")
    if piskvorky.vyhodnot() != "-":
        zprava.set(piskvorky.zpravy[piskvorky.vyhodnot()])


# vytvoření hlavního okna
root = Tk()

# popisek s názvem hry
label = ttk.Label(root, text="1D piškvorky", font=("Helvetica", 16))
label.pack()

# dva rámy, do kterých jsou později vkládány widgety grafického prostředí
frame_ovladani = Frame(root)
frame_ovladani.pack()
frame_hraci_pole = Frame(root)
frame_hraci_pole.pack()

# tlačíko zahájení nové hry, funkce predana jako argument command
# je zavolana pri kliknuti na tlacitko
button = ttk.Button(frame_ovladani, text="Nová hra",
                    command=priprava_hraciho_pole)
button.pack(side=LEFT, padx=20)
# root.mainloop()

# popisek pro textového pole
label = ttk.Label(frame_ovladani, text="Velikost hry")
label.pack(side=LEFT)

# textové pole pro zadání, jak velké bude hrací pole
velikost_hry = StringVar()  # promenná ve které bude vložen vstup z textového pole
entry = ttk.Entry(frame_ovladani, width=3, textvariable=velikost_hry)
velikost_hry.set("7")  # výchozí hodnota
entry.pack(side=LEFT)

# popisek ve kterém budou zprávy hry pro uživatele
zprava = StringVar()
label_zprava = ttk.Label(frame_ovladani, textvariable=zprava)
zprava.set("Zvolte velikost herního pole a začněte novou hru.")
label_zprava.pack(side=LEFT, padx=20)

# tlačítko pro ukončení hry (v mu-editoru ukončí hru až při druhém stisku)
button = ttk.Button(frame_ovladani, text="Konec hry", command=exit)
button.pack(side=LEFT, padx=20)

priprava_hraciho_pole()

# smyčka programu, aby program po spuštění hned neskončil, misto while
root.mainloop()
