# Tehtävä L08T01

nimet = []
numero = 0

while numero < 10:
    nimet.append(input("Anna nimi: "))
    numero += 1

for i in range (len(nimet)):
    print(nimet[i])

for i in range (len(nimet)):
    print(nimet[len(nimet)-1-i])