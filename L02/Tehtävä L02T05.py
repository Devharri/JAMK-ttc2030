# Tehtävä L02T05

etunimi_str = input("Anna etunimesi :")
lukumaara_int = len(etunimi_str)

lukumaara_str = str(lukumaara_int)

print("Nimessäsi " + etunimi_str + " on " + lukumaara_str + " kirjainta.")

teksti = ""
for i in range(lukumaara_int):
    teksti += etunimi_str[0]
    
print(teksti)