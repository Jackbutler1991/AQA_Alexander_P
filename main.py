class Pet():
    def __init__(self, kind, name, weight, age):
        self.kind = kind
        self.name = name
        self.weight = weight
        self.age = age


class Dog(Pet):
    def __init__(self, walk_m, walk_e, tale="full"):
        self.walktime_morning = walk_m
        self.walktime_evening = walk_e
        self._type_tale = tale

    def make_sound(self):
        print("BARK!")


class Cat(Pet):
    def __init__(self, type_f, waight_f, sterelized="yes"):
        self.type_food = type_f
        self.waight_food = waight_f
        self._sterelized = sterelized

    def make_sound(self):
        print("MEOM!")


my_Pet1 = Pet('Собака', 'Гуфи', 9, 4)
my_Pet1 = Dog("9:00", "19,00")

my_Pet2 = Pet('Кошка', 'Буся', 13, 3.5)
my_Pet2 = Cat("Royal Canin", 60)

print(my_Pet1.walktime_morning)
my_Pet1._type_tale = "Crop"
print(my_Pet1._type_tale)

for pet in (my_Pet1, my_Pet2):
    pet.make_sound()
