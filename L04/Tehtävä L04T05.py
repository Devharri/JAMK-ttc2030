# Tehtävä L04T05

etunimi_str = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")[::-1]

lukumaara_int = len(etunimi_str)
lukumaara_str = str(lukumaara_int)

teksti = ""
for i in range(lukumaara_int):
    teksti += etunimi_str[0].upper()
    
print(teksti, sukunimi)