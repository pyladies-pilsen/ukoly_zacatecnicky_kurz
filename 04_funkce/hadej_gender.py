jmeno = input("Zadej svoje křestní jméno> ")

if (jmeno[-1].lower() == "a") and (jmeno.lower() != "jirka"):
    print("Jsi holka.")
else:
    print("Jsi kluk")
