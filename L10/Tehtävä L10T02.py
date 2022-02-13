# Tehtävä L10T02

def kerro3(numero):
    if numero < 13:
        return "child"
    elif numero >= 13 and numero <= 19:
        return "teen"
    elif numero >= 20 and numero <= 65:
        return "adult"
    else:
        return "senior"

teksti = int(input("Anna ikä: "))

print(kerro3(teksti))