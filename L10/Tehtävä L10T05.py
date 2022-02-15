# Tehtävä L10T05

try:
    filename = "C:\L09T01.txt"
    file = open(filename, "w")
    file.write("Tekstiä" + "\n")
    file.close()
except PermissionError:
    print("Permission denied. Try another location.")
except:
    print("Something else went wrong.")