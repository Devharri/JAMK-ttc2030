# Tehtävä L06T03

isValueNull = False
kokonimi = ""
lukumaara = 0

while isValueNull == False:
    nimi = input("Anna oppilaan nimi: ")

    if nimi:
        if lukumaara == 0:
            kokonimi = nimi
        else:
            kokonimi = kokonimi + ", " + nimi
        lukumaara += 1
    else:
        isValueNull = True

print("Oppilaita: " + str(lukumaara))
print(kokonimi)