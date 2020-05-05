Z webu CinemaCity stáhněte data o promítaných filmech v Plzni a zobrazte je v
tabulce jednoduchém html.

Odkazy
------

CinemaCity webové stránky
https://www.cinemacity.cz/cinemas/plzen/1054#/buy-tickets-by-cinema?in-cinema=1054&at=2019-12-11&view-mode=list

Tutoriál k requests a beautifulsoup na naucse.python.cz
https://naucse.python.cz/2019/brno-jaro-knihovny/beginners/scraping/

Správné zpracování stránky i s JavaScriptem
https://stackoverflow.com/questions/26393231/using-python-requests-with-javascript-pages

CSS selector
https://www.w3schools.com/cssref/css_selectors.asp


Struktura webu CinemaCity
-------------------------

Sekce s tabulkou filmů:
    section "light quickbook-section"
    section "quickbook-component"
    section "container-fluid qb qb-by-cinema"

Tabulka filmů: "qb-list-by-list"
!!> Řádky v tabulce: div "row movie-row first-movie-row", "row movie-row"
Položky v řádku: "col-xs-9 qb-movie-details"::"qb-movie-info"
                 "col-xs-12 col-sm-7 col-md-8 events"::
                 "qb-movie-info-column col-xs-6"::
                 "qb-movie-info-column col-xs-6"::"btn btn-sm btn-primary"
