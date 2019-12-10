import requests
import bs4

odpoved = requests.get("https://www.cinemacity.cz/cinemas/plzen/1054#/buy-tickets-by-cinema?in-cinema=1054&at=2019-12-10&view-mode=list")
odpoved.raise_for_status()


with open("cc.html", "w", encoding="utf-8") as fout:
    print(odpoved.text, file=fout)
