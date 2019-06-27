"""
Jednoduchá kalkulačka
"""

a = float(input("Zadejte číslo a> "))
b = float(input("Zadejte číslo b> "))
op = input("Zadejte operaci> ")

if op == "+":
    vys = a+b
elif op == "-":
    vys = a - b
elif op == "/":
    vys = a / b
else:
    vys = "nevim"

# print("a", op, "b je", vys)





# Dále je příklad dost pokročilého řešení,
# koukni se na něj až na konci kurzu,
# až toho budes umět vic
ops = {"+": lambda x, y: x + y,
       "-": lambda x, y: x - y,
       "*": lambda x, y: x * y,
       "/": lambda x, y: x / y,
       "%": lambda x, y: x % y,
       "^": lambda x, y: x**y}

# print("a", op, "b je", ops[op](a, b) if op in ops else "Nevim")
print("{} {} {} je {}".format(a, op, b, ops[op](a, b) if op in ops else "Nevim"))
