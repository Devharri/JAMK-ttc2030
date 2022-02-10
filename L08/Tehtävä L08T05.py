# Tehtävä L08T05

import random

lottonumerot = []

#arvotaan kolme lukua väliltä 1-40
for x in range(7):
    luku = random.randint(1,40)
    lottonumerot.append(luku)
lottonumerot.sort()

luvut_str = str(lottonumerot)
luvut_str = luvut_str[1:]
luvut_str = luvut_str[:-1]
print(luvut_str)