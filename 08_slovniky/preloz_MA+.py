morse = {'0' : '-----',
           '1' : '.----',
           '2' : '..---',
           '3' : '...--',
           '4' : '....-',
           '5' : '.....',
           '6' : '-....',
           '7' : '--...',
           '8' : '---..',
           '9' : '----.',
           'A' : '.-'   ,
           'B' : '-...' ,
           'C' : '-.-.' ,
           'D' : '-..'  ,
           'E' : '.'    ,
           'F' : '..-.' ,
           'G' : '--.'  ,
           'H' : '...'  ,
           'I' : '..'   ,
           'J' : '.---' ,
           'K' : '-.-'  ,
           'L' : '.-..' ,
           'M' : '--'   ,
           'N' : '-.'   ,
           'O' : '---'  ,
           'P' : '.--.' ,
           'Q' : '--.-' ,
           'R' : '.-.'  ,
           'S' : '...'  ,
           'T' : '-'    ,
           'U' : '..-'  ,
           'V' : '...-' ,
           'W' : '.--'  ,
           'X' : '-..-' ,
           'Y' : '-.--' ,
           'Z' : '--..' }

retezec = str(input("Zadejte zprávu> ")).upper()

vystup = ""
oddel = False
for c in retezec:
    if c in morse:
        if oddel: # predchozi znaky byly mezery, carky, pomlcky nebo stredniky
                  # takze ted musime oddelit slova
            vystup = vystup + "| "
            oddel = False
        vystup = vystup + morse[c] + " "
    elif c in [".", "?", "!"]:
        vystup = vystup + " STOP "
    elif c in [",", " ", ";", "-"]: # pokud jsme narazili na mezeru, čárku, středník nebo pomlčku,
        # připravíme se na oddělení slov svislítkem "|"
        oddel = True

print("Do telegrafu vyťukejte: \n {}".format(vystup))
