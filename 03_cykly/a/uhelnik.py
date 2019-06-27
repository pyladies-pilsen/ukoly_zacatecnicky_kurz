import turtle as t

n = int(input("Zadejte, kolik strana ma n-uhelnik mít> "))

strana = 2*50/n  # aby nebyl n-úhelník obrovsky
uhel = 360 / n  # velikost vnitrnho uhlu je 180*(1-2/n), my ale potrebujeme doplnek toho uhlo do 180
# tedy 180 - 180*(1-2/n) = 360/n

for i in range(n):
    t.forward(strana)
    t.left(uhel)

t.done()