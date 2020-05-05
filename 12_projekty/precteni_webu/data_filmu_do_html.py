"""
Prevezme data filmu a presklada je do podoby tabulky v HTML.
Prevzato z https://github.com/Mintaka/pyladies_examples
Permalink
https://github.com/Mintaka/pyladies_examples/blob/1697d326eeb7388c3d55a8579a7155382cbed3db/preskladani_filmu_z_do_html/data_filmu_do_html.py
"""

__author__ = "Mintaka"


def uloz_data_do_html_stranky(data):
    hlavicka_stranky = \
    """<html><head>
    <meta charset=utf-8>
    </head><body>"""
    paticka_stranky = """</body></html>"""
    nazev_souboru = 'index.html'
    fw = open(nazev_souboru, 'w')
    fw.write(hlavicka_stranky + data + paticka_stranky)
    fw.close()


def radek_dat_do_html(radek):
    html_radek = """<tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                    <tr>""".format(radek[0], radek[1], radek[2], radek[3],)
    return html_radek


def tabulka_html(data_filmu):
    html_radky_tabulky = ""
    for radek in data_filmu:
        html_radky_tabulky += radek_dat_do_html(radek)
    return "<table border='2'>" + html_radky_tabulky + "</table>"