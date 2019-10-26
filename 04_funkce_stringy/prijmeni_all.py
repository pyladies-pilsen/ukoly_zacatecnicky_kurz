koncovky_3 = ["ová", "ova", "ská", "cká"]
koncovky_2 = ["la", "ná"]

prijmeni = input("Napiš své příjmení: ")

for konc3 in koncovky_3:
    if prijmeni[-3:] == konc3:
        print("Žena")
        exit()
for konc2 in koncovky_2:
    if prijmeni[-2:] == konc2:
        print("Žena")
        exit()
print("Muž")
