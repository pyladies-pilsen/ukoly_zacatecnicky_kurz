from html_do_dat import stahni_data_filmu
from data_filmu_do_html import uloz_data_do_html_stranky, radek_dat_do_html, \
    tabulka_html


data_filmu = stahni_data_filmu()

html_tabulka_filmu = tabulka_html(data_filmu)
uloz_data_do_html_stranky(data=html_tabulka_filmu)
