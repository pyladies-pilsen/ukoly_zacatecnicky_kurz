"""
Demonstruje nepřesnost konečné aritmetiky počítače
"""

soucet = 0
for i in range(1000):
    soucet += 0.001
print(soucet)
