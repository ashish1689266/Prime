# in this we will duck-typing polymorphism
# this means that a duck is a duck, so the name is same in different classes and can be called by there respective objects
class manager:
    def show_designation(self):
        print("Designation: Manager")

class Professor:
    def show_designation(self):
        print("Designation: Professor")

mg1 = manager()
mg1.show_designation()

pf1 = Professor()
pf1.show_designation()

# so this is again a concept that we should use here in programming to create multiple function with same name
#  and this is the end of lesson 4 codes but homework is left