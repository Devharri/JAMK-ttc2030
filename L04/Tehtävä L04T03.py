# Tehtävä L04T03

from contextlib import nullcontext


lukujenSumma = 0
lukujenLukumaara = 0
isValueNull = False

while isValueNull == False:
    luku1 = input("Anna luku: ")

    if luku1:
        lukujenSumma = lukujenSumma + int(luku1)
        lukujenLukumaara += 1
    else:
        isValueNull = True
        print("Lukuja annettu: " + str(lukujenLukumaara))
        print("Lukujen summa: " + str(lukujenSumma))




