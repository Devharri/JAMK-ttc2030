# Tehtävä L03T02

luku1 = int(input("Anna ensimmäinen kokonaisluku :"))
luku2 = int(input("Anna toinen kokonaisluku :"))
luku3 = int(input("Anna kolmas kokonaisluku :"))

if luku1 > luku2 and luku1 > luku3:
    print("Suurin: " + str(luku1))
elif luku2 > luku1 and luku2 > luku3:
    print("Suurin: " + str(luku2))
else:
    print("Suurin: " + str(luku3))