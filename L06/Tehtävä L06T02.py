# Tehtävä L06T02

def celToFah(cel):
    fah = cel * 1.8 + 32
    format_fah = "{:.1f}".format(fah)
    return format_fah

def fahToCel(fah):
    cel = (fah - 32) * 0.5556 
    format_cel = "{:.1f}".format(cel)
    return format_cel

print(celToFah(10.0))
print(fahToCel(38.0))