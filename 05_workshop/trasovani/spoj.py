# nejprve otevreme soubory s abecedami pro cteni
text_1_soubor = open("text_1.txt", encoding="utf-8")
text_2_soubor = open("text_2.txt", encoding="utf-8")

# pote nacteme jejich obsah (abecedy) do promennych,
# se kterymi budeme pracovat
text_1 = text_1_soubor.read()
text_2 = text_2_soubor.read()

# kazdy soubor, ktery otevreme, bychom meli i zavrit
text_1_soubor.close()
text_2_soubor.close()

vysledek_soubor = open("vysledek.txt", mode="w", encoding="utf-8")
vysledek_soubor.write(text_1 + text_2)
vysledek_soubor.close()
