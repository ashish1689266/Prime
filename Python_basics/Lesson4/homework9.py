# Create the following classes: carnivore, herbivore , omnivore with some
# attributes & methods. Then create a class bear that inherits from all the above
# classes to showcase how multiple inheritance works

class carnivore:
    food = "non-veg"
    def __init__(self, species, name, speed):
        self.name = name
        self.speed = speed
        self.species = species

    def food_type(self):
        print(f"As a Carnivore it eats {carnivore.food}")

class herbivore:
    food = "veg"
    def __init__(self, species, name, size):
        self.name = name
        self.size = size
        self.species = species

    def food_type(self):
            print(f"As a Herbivore it eats {herbivore.food}")

class omnivore:
    food = "all food"
    def __init__(self, species, name, speed, size):
        self.name = name
        self.speed = speed
        self.size = size
        self.species = species

    def food_type(self):
            print(f"As a Omnivore it eats {omnivore.food}")

class bear(omnivore, carnivore, herbivore):
    def __init__(self, species, name, size, speed):
        super().__init__(species, name, speed, size)
        carnivore.__init__(self, species, name, speed)
        herbivore.__init__(self, species, name, size)

    def show_data(self):
        print(f"Species: {self.species} Name: {self.name}, Size: {self.size}, Speed: {self.speed}")

    def food_type(self):
        super().food_type()
        carnivore.food_type(self)
        herbivore.food_type(self)

ballu = bear("bear", "ballu", "big", "60mph")
ballu.show_data()
ballu.food_type()