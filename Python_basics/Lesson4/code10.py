# type 3 - multiple inheritance
# in this one class inherits two parent classes

class professor:
    def __init__(self, teaching_amount):
        self.teaching_amount = teaching_amount

class student:
    def __init__(self, subject):
        self.subject = subject

class teaching_assistant(professor, student): # this is how you can inherit multiple class
    def __init__(self, name, teaching_amount, subject):
        self.name = name
        super().__init__(teaching_amount)
        student.__init__(self, subject)

    def show_data(self):
        print(f"Name: {self.name}, Amount: {self.teaching_amount}, Subject: {self.subject}")

teacher1 = teaching_assistant("Ashish", 80_000, "Computer Science")
teacher1.show_data()

# so here we can see that we have two classes that are inherited and they have no relation in between them
# and there will be a child class that inherits properties from both the classes
# this is why when we try to call a function and it is present in bith parent class with same name so if we use super keyword to refer
# the parent class there is the ambiguity, which parents function to call?
# to solve this we need to put class name in parenthesis accordingly, super keyword will refer to the first parent class 
# written inside the parenthesis, and that's how we solve this ambiguity