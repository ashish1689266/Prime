# there are 3 types of inheritance
# type 1 - single level inheritance meaning one parent one child

class employee:
    start = "10am"
    end = "6pm"

    def __init__(self, id):
        self.id = id

    def show_data(self):
        print(self.id)

class intern(employee):
    def __init__(self, name, id):
        self.name = name
        employee.__init__(self, id)

    def show_data(self):
        print(self.name)
        super().show_data()

emp1 = intern("Ashish", "emp101")
emp1.show_data()

# this is single level inheritance
# here you can see that we are having one class inheriting another