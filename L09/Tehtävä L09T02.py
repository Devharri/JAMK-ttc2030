# Tehtävä L09T02

filename = "L09T01.txt"
lines = [""]
try:
    file = open(filename, "r")
    lines = file.readlines()
except:
    print("Failed to read file: " + filename)
finally:
    file.close()

print("Tiedosto:", filename)
lines.sort()
print(lines)