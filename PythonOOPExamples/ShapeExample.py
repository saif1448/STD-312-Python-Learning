# from abc import abstractmethod


#Inheritence
#Abstraction ---> Hiding complex logic inside the class
#Polymorphism ---> same name, but different purpose

class Shape():

    def show_string(self):
        print("I am an type of shape")
    # @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = 0

    def __add__(self, other):
        area1 = self.calculate_area()
        area2 = other.calculate_area()
        return area1 + area2

    def calculate_area(self):
        # print(f'AREA OF RECTANGLE: {self.length * self.width}')
        self.area = (self.length * self.width)
        return self.area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        print(f'AREA OF CIRCLE: {3.1416 *self.radius * self.radius}')

    def __str__(self):
        return 'This is a circle'

class Triangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        print(f'AREA OF TRIANGLE: {0.5 * self.a * self.b}')

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        print(f'AREA OF SQUARE: {self.side * self.side}')


rect = Rectangle(5,6)
rect2 = Rectangle(15,16)

rect3 = rect + rect2

circle = Circle(3)
triangle = Triangle(7,8)
square = Square(8)

print(rect.calculate_area())
print(rect2.calculate_area())
print(rect3)

circle.calculate_area()
triangle.calculate_area()
square.calculate_area()


print(circle)