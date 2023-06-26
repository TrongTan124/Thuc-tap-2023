class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length

# Encapsulation (Đóng gói)
# Tính chất Encapsulation được thể hiện trong việc đóng gói dữ liệu (bán kính, chiều cao) và mã liên quan vào các đối tượng Circle và Cylinder.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius**2

# Inheritance (Kế thừa)
# Tính chất Inheritance được thể hiện khi lớp Cylinder kế thừa các thuộc tính và phương thức từ lớp Circle.
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def get_volume(self):
        return self.get_area() * self.height

# Polymorphism (Đa hình)
# Tính chất Polymorphism được thể hiện khi các đối tượng Rectangle và Triangle cùng thực hiện phương thức get_area() nhưng cho kết quả khác nhau.
class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

# Abstraction (Trừu tượng)
# Tính chất Abstraction được thể hiện trong việc sử dụng lớp Shape là một lớp trừu tượng có phương thức không được định nghĩa.
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Private, protected, public
class Car:
    def __init__(self):
        self._engine = "V8"  # protected attribute
        self.__mileage = 0  # private attribute

    def get_engine(self):
        return self._engine

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

# Sử dụng các tính chất của OOP
circle = Circle(5)
print("Circle area:", circle.get_area())

cylinder = Cylinder(5, 10)
print("Cylinder volume:", cylinder.get_volume())

rectangle = Rectangle(4, 5)
print("Rectangle area:", rectangle.get_area())

triangle = Triangle(3, 6)
print("Triangle area:", triangle.get_area())

dog = Dog()
print("Dog sound:", dog.sound())

cat = Cat()
print("Cat sound:", cat.sound())

car = Car()
print("Car engine:", car.get_engine())
car.set_mileage(5000)
print("Car mileage:", car.get_mileage())
