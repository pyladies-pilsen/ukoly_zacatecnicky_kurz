text = input("Zadejte text: ")

novy_text = ""
for z in text:
    if z == " ":
        novy_text = novy_text + "+"
    else:
        novy_text = novy_text + z

print(novy_text)
