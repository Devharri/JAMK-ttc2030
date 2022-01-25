# Tehtävä L05T04

def get_fuel(dist, cons):
    kulutus = round(((dist*cons)/100),1)
    teksti = str(kulutus) + " ltr"
    return teksti

print(get_fuel(100,7.5))
print(get_fuel(220,6.9))