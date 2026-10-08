# Create a class Vehicle with attributes like brand and model.
# Create two subclasses car and bike that add extra attributes - seats (in Car) &
# engine_cc (in Bike)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def show_data(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Seats: {self.seats}")

class bike(Vehicle):
    def __init__(self, brand, model, cc):
        Vehicle.__init__(self, brand, model)
        self.cc = cc

    def show_data(self):
        print(f"Brand: {self.brand}, Model: {self.model}, CC: {self.cc}")

car1 = car("BMW", "M4 Competition", 2)
car1.show_data()
print()
bike1 = bike("Kawasaki", "Ninja", 1200)
bike1.show_data()