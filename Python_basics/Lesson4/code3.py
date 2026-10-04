# class variables and instance variables
class student:
    # these all are class variables so for every object they are not created separately but
    # they are created once class is created and will remain same for every object
    Language = ["English", "Hindi"]
    Country = "India"
    Session = 2026
    College = "ApnaCollege"
    Course = "AI/ML" # this variable will be created again in init
    Address = "ApnaCollege Campus"

    def __init__(self, name, cgpa, Course):
        # these are instance variables which are related to the object with which 
        # this method called
        self.name = name
        self.cgpa = cgpa
        self.Course = Course # this variable also present as class variable
        # so when called with object instance related value will be printed,
        # if called with class name class value will be printed
        # class variables can be called by both class and object
        # instance variables can only be called with the name of instance

    def show_data(self):
        print(self.name)
        print(self.cgpa)
        print(self.Course)

student1 = student("Ashish", 8.48, "Python")
student1.show_data()

print(student1.Country) # this is class variable hence can  be called with both
print(student1.Course) # Course called with object
print(student.Course) # Course called with class
