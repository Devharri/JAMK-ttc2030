# Tehtävä L10T01

balance = 2000

print("Bank account balance: " + str(balance))

luku1 = float(input("How many euros will be added to the balance? "))
luku2 = float(input("How many cents will be added to the balance? "))

luku3 = balance + luku1+ (luku2/100)

print("Bank account balance: " + str(luku3))