# Tehtävä L10T04

nimet = []

nimet.append("Ykä")
nimet.append("Eka")
nimet.append("Ekku")
nimet.append("Musti")

try:
    indeksi = int(input("Monettako indeksiä muutetaan: "))
    teksti = input("Anna teksti: ")
    print("Vanha nimi: " + nimet[indeksi])
    nimet[indeksi] = teksti
    print("Uusi nimi: " + nimet[indeksi])
except IndexError:
    print("List index out of range.")
except:
    print("Something else went wrong.")