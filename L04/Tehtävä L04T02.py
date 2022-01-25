# Tehtävä L04T02

dayCount = 0
rainAmount = 0

while dayCount <7:
    luku1 = int(input("Anna sademäärä: "))

    dayCount += 1
    rainAmount = rainAmount + luku1

print("Sademäärä yhteensä: " + str(rainAmount))