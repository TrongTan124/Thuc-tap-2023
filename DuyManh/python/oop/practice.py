#Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle():
     def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
     def __str__(self):
         return f"Max_speed: {self.max_speed}, mileage: {self.mileage}"
v1 = Vehicle(30, 100)

#Create a Vehicle class without any variables and methods
class Vehicle():
    pass

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __str__(self):
        return f"Bus: {self.name, self.max_speed, self.mileage}"


#Class Inheritance
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
     def seating_capacity(self, capacity=50):
          return f"Capacity: {capacity}"
          pass
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


#Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise.
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

