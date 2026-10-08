# Create a class student with private attributes _name, _roll_no, and _marks.
# Provide getters and setters methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 & 100 & name cannot be empty
class student:
    def __init__(self):
        self.__name = ""
        self.__roll = ""
        self.__marks = ""

    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Invalid input, need a name")

    def set_roll(self, roll_no):
        if (type(roll_no) == int) and (roll_no > 1) and (roll_no < 100):
            self.__roll = roll_no 
        else:
            print("Invalid input, need integer value")

    def set_marks(self, marks):
        if (type(marks) == int) and (marks >= 0):
            self.__marks = marks
        else:
            print("Invalid input, need integer value")

    def get_name(self):
        print(f"The name of student is {self.__name}")

    def get_roll(self):
        print(f"The Roll_no of student is {self.__roll}")

    def get_marks(self):
        print(f"The marks of student is {self.__marks}")

stu1 = student()
stu1.set_name("Ashish")
stu1.get_name()
stu1.set_roll(99)
stu1.get_roll()
stu1.set_marks(98)
stu1.get_marks()

