# type 2 - multilevel inheritance, in this parent to child and then child's child class, means base class will become grand_parent

class employee:
    start = "10am"
    end = "6pm"

    def __init__(self, id):
        self.id = id

    @staticmethod
    def admin_parent():
        print("this is employee class")

class admin(employee):
    def __init__(self, name, id):
        self.name = name
        super().__init__(id)

    @staticmethod
    def account_parent():
        print("this is admin class")

class account(admin):
    def __init__(self, name, id, salary):
        self.salary = salary
        super().__init__(name, id)

    def show_data(self):
        print(f"Name: {self.name}, id : {self.id}, salary : {self.salary}")

    @staticmethod
    def admin_child():
        print("this is account class")

emp1 = account("Ashish", "emp101", 80_000)
emp1.show_data()

emp1.admin_child()
emp1.account_parent()
emp1.admin_parent()

# here you can see that one parent than child than grand child class is here and we can 
# access grandparent class methods by the object of grandchild class