# Create a class person that allows the constructor to work with:
# name only
# name + age
# name + age + address

class person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

person1 = person("Ashish")
person2 = person("Rida", 26)
person3 = person("Harmeet", 27, "Punjab")

person1.show_data()
print()
person2.show_data()
print()
person3.show_data()