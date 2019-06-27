"""
Vypise dokonala cisla mensi nez n
"""


n = int(input("Zadejte n> "))

for i in range(1, n+1):  # postupne vyzkousime vsechna cisla mensi nez n
    s = 0
    for j in range(1, i):  # otestujem vsechna cisla mensi nez i
        if i % j == 0:  # pokud j deli i beze zbytku
            s += j  # pridame ho do souctu
    if s == i:
        print(i)  # kdyz se soucet delitelu rovna i je i dokonale!
