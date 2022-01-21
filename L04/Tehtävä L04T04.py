# Tehtävä L04T04

luku1 = int(input("Anna numero väliltä 1-10 :"))

for i in range(1, luku1+1):
    luku2 = i
    luku3 = luku2 * luku2
    print("Luvun " + str(luku2) + " neliö on: " + str(luku3))