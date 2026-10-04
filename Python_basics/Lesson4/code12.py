# The last concept for this lesson the polymorphism
# poly means many, morph means forms
# here methods with same names having different forms

class Admin:
    def show_designation(self): # this is one function where we are writing its defination
        print("Designation: Admin")

    def work_address(self): # this method we are creating but we will not redefine this in the child class
        print("IT park Bangalore")

class manager(Admin):
    def show_designation(self): # here we are redefining the parent class method 
        print("Designation: Manager")
        # and this is called function overriding because we are defining it again and overriding the parents defination

mg1 = manager()
mg1.show_designation() # here overrided defination will work
mg1.work_address() # on this one there is no overriding and this is why parents defination will work

