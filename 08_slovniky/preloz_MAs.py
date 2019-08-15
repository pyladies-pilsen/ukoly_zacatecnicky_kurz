"""
Super kratka jednoducha verze prekadu do morzeovky
"""

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

# dve hledani ve slovniku, bez znalosti slovnikovych metod
vystup = " ".join(morse[c] for c in retezec if c in morse)

#  jen jedno hledani ve slovniku
vystup2 = " ".join(morse.get(c, "") for c in retezec)

print(vystup)
