# Tehtävä L09T01

isValueNull = False
thislist = []
while isValueNull == False:
    nimi = input("Anna sukunimi: ")
    
    if nimi:
        thislist.append(nimi)
    else:
        isValueNull = True

filename = "testi.txt"
file = open(filename, "w")
for x in thislist:
    file.write(x + "\n")
file.close()