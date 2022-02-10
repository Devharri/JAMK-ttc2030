# Tehtävä L08T04

autot = {}
lista = []
laskuri = 0

while laskuri < 3:
    reknumero = input("Anna rekisterinumero: ")
    valmistaja = input("Anna auton valmistaja: ")
    
    if reknumero:
        if valmistaja:
            laskuri += 1
            autot[reknumero] = valmistaja
        else:
            print("Input was empty. Give valid input.")

    else:
        print("Input was empty. Give valid input.")

for x, y in autot.items():
  lista.append((x+ " " + y))
lista.sort()
for nimi in lista:
    print(nimi)