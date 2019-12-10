from requests_html import HTMLSession

day = 11
month = 12
mode = "list"

base_url = "https://www.cinemacity.cz/cinemas/plzen/1054#/buy-tickets-by-cinema?in-cinema=1054"
day_url = "at=2019-{month}-{day}".format(day=day, month=month)
view_mode_url = "view-mode={mode}".format(mode=mode)

session = HTMLSession()

r = session.get("&".join([base_url, day_url, view_mode_url]))

r.html.render()  # this call executes the js in the page

for row in r.html.find("div .movie-row"):
    print(row.text)
