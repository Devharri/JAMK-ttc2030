# Tehtävä L08T01

nimet = []
numero = 0

while numero < 10:
    nimi = input("Anna nimi: ")
    if nimi:
        nimet.append(nimi)
        numero += 1
    else:
        print("Input was empty. Give valid input.")

for i in range (len(nimet)):
    print(nimet[i])

for i in range (len(nimet)):
    print(nimet[len(nimet)-1-i])