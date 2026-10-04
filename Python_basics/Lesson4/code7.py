# Inheritance - In inheritance we are inheriting the features of parent class to the child class and 
# parents class methods and variables are accessed by the object of child class

class employee:  # this is parent or base class
    start_time = "10am"
    end_time = "6pm" # these class variables are accessed by child class objects

    def __init__(self, id):
        self.id = id

    def change_id(self, new_id):
        self.id = new_id

class managers(employee):# this is child or derived class
    def __init__(self, name, id):  # this is child class init 
        self.name = name
        super().__init__(id) # here we are handling one variable by calling parent class init by super keyword, we can also use name of class


    def show_data(self):
        print(f"{self.name} : {self.id}")

emp1 = managers("Ashish", "emp101") # object is created
emp1.show_data() # calling the child class method by object of child class
emp1.change_id("emp104") # calling the parent class method by child class object
emp1.show_data() # again showing the data
