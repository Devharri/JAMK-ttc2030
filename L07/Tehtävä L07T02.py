# Tehtävä L07T02

class Human:
    name = ""
    age = 0
    def __str__(self):
        return "Nimi: " + self.name + ", " + "ikä: " + str(self.age)

ihminen1 = Human()
ihminen1.name = "Adam"
ihminen1.age = 19
print(ihminen1)

ihminen2 = Human()
ihminen2.name = "Eve"
ihminen2.age = 18
print(ihminen2)