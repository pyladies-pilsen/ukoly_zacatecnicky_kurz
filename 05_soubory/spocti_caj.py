# nejprve otevreme soubory s abecedami pro cteni
hiragana_soubor = open("hiragana.txt", encoding="utf-8")
katakana_soubor = open("katakana.txt", encoding="utf-8")

# pote nacteme jejich obsah (abecedy) do promennych,
# se kterymi budeme pracovat
hiragana = hiragana_soubor.read()
katakana = katakana_soubor.read()

# kazdy soubor, ktery otevreme, bychom meli i zavrit
hiragana_soubor.close()
katakana_soubor.close()

# soubory obsahuji i znaky pro zalomeni radku "\n",
# tech se zbavime, abychom je nepocitali k abecede
# nahradime je prazdnym retezcem ""
hiragana = hiragana.replace("\n", "")
katakana = katakana.replace("\n", "")

# stejne jako abecedy nacteme i zkoumany text
text_soubor = open("rozsypany_caj.txt",  encoding="utf-8")
text = text_soubor.read()
text_soubor.close()

pocet_katakana = 0
pocet_hiragana = 0
# z textu postupne bereme znaky a zkoumame
# jestli patri do jedne z abeced
for znak in text:
    if znak in hiragana:
        pocet_hiragana = pocet_hiragana + 1
    elif znak in katakana:
        pocet_katakana += 1
        # zkraceny zapis, se stejnym vyznamem jako
        # pocet_katakana = pocet_katakana + 1

print("V souboru bylo:", pocet_hiragana,
      "znaku hiragany a", pocet_katakana,
      "znaku katakany")
