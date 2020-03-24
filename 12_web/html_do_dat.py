"""
Stáhne stránku s programem Cinemacity Plzeň Plaza a
vytáhne z ní data o filmech v programu
"""

from requests_html import HTMLSession
from typing import List


def stahni_data_filmu(day=11, month=12):
    """
    Vrátí seznam filmů promítaných v daný den a měsíc,
    každý film je reprezentován seznameme, který obsahuje:
    [jméno filmu, informace o filmu, informace o promítání, [časy promítání]]
    """
    mode = "list"

    # adresa URL se dá rozdělit na několk částí, které nakonec spojíme
    # pomocí '&'
    base_url = "https://www.cinemacity.cz/cinemas/plzen/1054#/\
               buy-tickets-by-cinema?in-cinema=1054"

    # část adresy, která říká webové stránce který den chceme zobrazit
    day_url = "at=2019-{month}-{day}".format(day=day, month=month)
    view_mode_url = "view-mode={mode}".format(mode=mode)

    sezeni = HTMLSession()

    # spojíme části adresy a vyžádáme si stažení stránky
    stranka = sezeni.get("&".join([base_url, day_url, view_mode_url]))

    # vynutíme zpracování stránky, aby se objevila všechna data
    stranka.html.render()

    # vyhledáme všechny řádky obsahující informace o filmech
    film_radky = stranka.html.find("div .movie-row")

    # procházíme řádek po řádku a zpracováváme
    data = []
    for film_radek in film_radky:
        film_radek_list = film_radek.text.split("\n")
        nazev = film_radek_list[0]
        info_f = film_radek_list[1]
        #  vymaže znaky xa0, což je nedělitelná mezera a znaky •
        info_p = film_radek_list[2].replace("\xa0", "").replace("•", "")

        casy = film_radek_list[3]
        casy_list = []
        # řetězec obsahující časy rozdělíme na řetězce o pěti znacích
        for i in range(0, len(casy), 5):
            casy_list.append(casy[i:i+5])
        # print(nazev, info_f, info_p, casy_list)

        # zpracovaný řádek připojíme k datům
        data.append([nazev, info_f, info_p, casy_list])
    return data
