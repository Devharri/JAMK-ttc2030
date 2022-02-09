# Tehtävä L07T05

class Car:
    brand = ""
    model = ""
    price = 0
    def __str__(self):
        return "Auto: " + self.brand + " " + self.model + " " + str(self.price)
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

auto1 = Car("Skoda", "Octavia", 3000)
auto2 = Car("Audi", "A4", 4000)
auto3 = Car("Volvo", "V70", 5000)

total_price = auto1.price+auto2.price+auto3.price

print(auto1)
print(auto2)
print(auto3)

print("Autojen hinta yhteensä: " + str(total_price))