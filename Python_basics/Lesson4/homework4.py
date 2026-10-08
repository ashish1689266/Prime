# Create a class shape with a method area().
# Create subclasses circle, rectangle, triangle that override the area() method

class shape:
    def area(self):
        print("This is the area method that needs to be overrided in child classes")

class circle(shape):
    def area(self, radius):
        self.circle_area = 3.14 * (radius ** 2)

    def display_area(self):
        print(f"Area: {self.circle_area}")

class rectangle(shape):
    def area(self, length, breadth):
        self.rect_area = length * breadth

    def display_area(self):
        print(f"Area: {self.rect_area}")

class triangle(shape):
    def area(self, length, breadth):
        self.triangle_area = (length * breadth) / 2

    def display_area(self):
        print(f"Area: {self.triangle_area}")

circle1 = circle()
circle1.area(7)
circle1.display_area()
print()
rect1 = rectangle()
rect1.area(5, 4)
rect1.display_area()
print()
triangle1 = triangle()
triangle1.area(3, 5)
triangle1.display_area()