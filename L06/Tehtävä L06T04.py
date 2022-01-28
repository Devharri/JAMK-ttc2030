# Tehtävä L06T04

yhteensa = 0
thisList = []

for i in range(5):
    piste1 = int(input("Hypyn pisteet: "))
    thisList.append(piste1)
    yhteensa += piste1

max_value = max(thisList)
min_value = min(thisList)

yhteensa = yhteensa - min_value
yhteensa = yhteensa - max_value

print(yhteensa)