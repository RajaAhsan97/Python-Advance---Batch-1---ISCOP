# part 2: defining attributes and methods of child class

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
# Single - level Inheritance
class ElectricCar(Car):

    # construnctor 
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size} - KWh battery")

ec1 = ElectricCar("CIVIC", "HC1", 2019, 180)

print(ec1.describe_battery())