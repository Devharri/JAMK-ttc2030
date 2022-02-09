# Tehtävä L08T02

isValueNull = False
rekkarit = []

while isValueNull == False:
    teksti = input("Anna rekisterinmero: ")

    if teksti:
        rekkarit.append(teksti)
    else:
        isValueNull = True
        rekkarit.sort()
        print(rekkarit)