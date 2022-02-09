# Tehtävä L07T03

class Cat:
    name = ""
    color = ""
    def __str__(self):
        return self.name + ", " + "color: " + str(self.color)
    def miau(self):
        return self.name + " says: Meoooooow!"

kissa1 = Cat()
kissa1.name = "Kit"
kissa1.color = "black"

kissa2 = Cat()
kissa2.name = "Kat"
kissa2.color = "white"

print(kissa1)
print(kissa2)

print(kissa1.miau())
print(kissa2.miau())