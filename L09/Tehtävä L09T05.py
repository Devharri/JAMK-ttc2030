# Tehtävä L09T05

import random
vanhaluku = 0

lukumaara = int(input("Montako riviä arvotaan: "))
    
filename = "lotto.txt"
file = open(filename, "a")
file.write("Arvotut lottorivit:" + "\n")
file.close()

for x in range(lukumaara):
    lottonumerot = []
    #arvotaan kolme lukua väliltä 1-40
    for x in range(7):
        luku = random.randint(1,40)
        while vanhaluku == luku:
            luku = random.randint(1,40)
        lottonumerot.append(luku)
        vanhaluku = luku

    lottonumerot.sort()

    luvut_str = str(lottonumerot)
    luvut_str = luvut_str[1:]
    luvut_str = luvut_str[:-1]

    filename = "lotto.txt"
    file = open(filename, "a")
    file.write(luvut_str + "\n")
    file.close()

    print(luvut_str)

filename = "lotto.txt"
file = open(filename, "a")
file.write("\n")
file.close()