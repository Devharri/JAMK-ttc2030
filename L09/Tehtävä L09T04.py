# Tehtävä L09T04

filename = "nimet.txt"
lines = [""]
linesdict = {}
totalcount = 0
duplicatecount = 0
prevName = ""
try:
    file = open(filename, "r")
    lines = file.readlines()
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

print("Tiedosto:", filename)

lines.sort()

for x in lines:
    totalcount +=1
    if prevName != x:
        for i in lines:
            if i == x:
                duplicatecount +=1
        if x[-1] == "\n":
            linesdict[x[:-1]] = str(duplicatecount) + " kertaa."
        else:
            linesdict[x] = str(duplicatecount) + " kertaa."
        prevName = x
        duplicatecount = 0

print("Nimiä yhteensä: " + str(totalcount))
for x,y in linesdict.items():
    print(x,y)