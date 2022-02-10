# Tehtävä L08T03

isValueNull = False
numCount = 0
numAvg = 0.0
arvosanat = []

while isValueNull == False:
    numero = input("Anna arvosana: ")

    if numero:
        arvosanat.append(int(numero))
        numCount += 1
    else:
        isValueNull = True
        numAvg = (sum(arvosanat) / numCount)
        print("Keskiarvo: " + str(numAvg) + ", lukumäärä: " + str(numCount))