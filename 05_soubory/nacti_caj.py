hir = open("hiragana.txt", encoding="utf-8").read().replace("\n", "")
kat = open("katakana.txt", encoding="utf-8").read().replace("\n", "")
text = open("test.txt", encoding="utf-8").read()

nkat = 0
nhir = 0
for c in text:
    if c in hir:
        nhir += 1
    elif c in kat:
        nkat += 1
print("V souboru bylo: \n \t {} znaku hiragany a \n \t {} znaku katakany".format(nhir, nkat))

