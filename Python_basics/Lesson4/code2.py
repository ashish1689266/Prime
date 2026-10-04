# here we will talk about constructors
# so basically we can have methods here to define uncommon data, # when creating data for the student 
# it is obvious that name of the students will not be the same so we have __init__ method which is a constructor that 
# runs automatically when we create a oject, you can do anything there but normally used to
# assign values to instance variables

class student:
    Country = "India"
    Session = 2026
    College = "ApnaCollege"
    Course = "AI/ML" # these are class variables

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa  # self.name and self.cgpa are the instance variables, name and cgpa are parameters
        # this self parameter is compulsory to use because this refer to the object with which init is being called with
        # otherwise you are going to store so many same named variables for any number of objects

    def show_cgpa(self):
        print(f"The cgpa for {self.name} is {self.cgpa}") # this is also a method

student1 = student("Ashish", 8.48) # this is how you pass the value and putting parenthesis means to call __init__
print(student1.name)
student1.show_cgpa()

stu_list = []
for i in range(0, 5):
    name = input("Enter a name: ")
    cgpa = float(input("Enter cgpa: "))
    new_stu = student(name, cgpa)
    stu_list.append(new_stu)

for stu in stu_list:
    print(stu.name, end=" ")
    stu.show_cgpa() # this is how you can call other methods
    print()

# you can store as much information as you want by just increasing the interation of loop

# last important thing is constructors can be default and parameterized

# they are default when they only have self parameter

# and they are parameterized when they have other parameters than self

# do not write two constructors in same class, it is not allowed in python
