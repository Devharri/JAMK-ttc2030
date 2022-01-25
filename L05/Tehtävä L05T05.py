# Tehtävä L05T05

def get_cost(dist, cons, money):
    kulutus = round((((dist*cons)/100)*money),2)
    teksti = str(kulutus) + " €"
    return teksti

print(get_cost(100,7.5,1.88))
print(get_cost(220,6.9,1.88))