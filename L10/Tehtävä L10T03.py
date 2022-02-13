# Tehtävä L10T03

vuosi = int(input("Anna vuosiluku: "))

jako4 = vuosi % 4
jako100 = vuosi % 100
jako400 = vuosi % 400

if jako4 == 0 and jako100 != 0:
    print(str(vuosi) + " is a leap year!")
elif jako4 == 0 and jako100 == 0 and jako400 == 0:
    print(str(vuosi) + " is a leap year!")
else:
    print(str(vuosi) + " is not a leap year!")