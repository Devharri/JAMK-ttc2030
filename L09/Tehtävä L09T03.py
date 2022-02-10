# Tehtävä L09T03

isValueNull = False
thislist = []
thiscount = 0

while isValueNull == False:
    luku = input("Anna kokonaisluku: ")

    if luku:
        thislist.append(int(luku))
        thiscount +=1
    else:
        isValueNull = True

filename = "luvut.txt"
file = open(filename, "w")

for x in thislist:
    file.write(str(x) + "\n")
    
file.write("Syötetty " + str(thiscount) + " lukua."  + "\n")
file.close()