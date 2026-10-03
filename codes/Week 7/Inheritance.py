# Inheritance:
# If Class A inherit Class B, class B is Parent and Class A is Child 


# Part1: Demonstration of How child inherti attributes and methods of Parent class 
# Parent classes
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        # Instance Attributes
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # instance methods
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Child class
class ElectricCar(Car):
    pass

ec1 = ElectricCar("CIVIC", "HC1", 2019)

print(ec1.make)
print(ec1.model)
print(ec1.year)
print(ec1.odometer_reading)

print(ec1.get_descriptive_name())
print(ec1.read_odometer())
print(ec1.update_odometer(10))
print(ec1.increment_odometer(5))
print(ec1.read_odometer())