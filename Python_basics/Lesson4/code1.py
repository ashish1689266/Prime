# This is object oriented programming and we will learn about classes and objects.
# Classes are blueprint of something or a facory which know what to make but it will make it only when we create the object
# this means classes do not occupy any memory but object does
# with the help of classes we can increase the reusablility of the code.
# for example we ant to store data of thousands of students, you say it can be done by dictionary or tuple but this
# will require thousands of lines of code to make, writing nested dictionary code for a thousand students, its not easy
# then here comes the classes and objects

class student: # this how you make a class
    Language = ["English", "Hindi"]
    Country = "India"
    Session = 2026
    College = "ApnaCollege"
    Course = "AI/ML"
    Address = "ApnaCollege Campus"

# this is all you have to write for creating this common data and do not worry there are ways for separate data also and that is
# as same as this

# now when i create the object the data will be created for that student when i create the object
student1 = student() # this is how you create the object by calling the class
# now we try printing the details for student1 with dot notation
print(student1.Language, student1.Address, student1.College, student1.Country, student1.Session, student1.Course, sep="\n")

# it is that easy and now you can create as many objects you want
student2 = student() # second object created now see this
print(student2.Language, student2.Address, student2.College, student2.Country, student2.Session, student2.Course, sep="\n")
object_list = []
for i in range(0, 1000):
    new_student = student()
    object_list.append(new_student)

print(object_list)

# here when we print that list it will give us 1000 object and with there address in the memory
print(student1)
print(student2)
