class Car:
    def __init__(self, make, model, fuel_capacity, mileage, fuel_efficiency, fuel_level=0):

        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.mileage = mileage
        self.fuel_efficiency = fuel_efficiency

    def refuel(self, amount):
        
        if amount > 0:
            self.fuel_level += amount
            if self.fuel_level > self.fuel_capacity:
                self.fuel_level = self.fuel_capacity
            return f"Fuel level is now {self.fuel_level}"

    def drive(self, distance):
        # This method should:
        # - Calculate the fuel needed to cover the distance (assume 10 km per liter).
        # - Check if there is enough fuel in the tank to drive the distance.
        # - Deduct the fuel used from fuel_level if possible.
        # - Return a message confirming the distance driven and remaining fuel, or an error if fuel is insufficient.
        
        fuel_needed = distance/10
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            return f"The car drove {distance} km and has {self.fuel_level} liters of fuel left."
        else:
            return "The car doesn't have enough fuel to drive that far."
        
    def getMileage(self):
        return self.mileage
    
    def oil_change(self):
        if self.mileage % 5000 == 0:
            print("Time for an oil change!")

# ----------------------------------------------
# Runner

# Create a new car
my_car = Car("Toyota", "Corolla", 50)
# Test refueling
print(my_car.refuel(30)) # Should increase fuel to 30 liters
# Test driving
print(my_car.drive(100)) # Should reduce fuel by 10 liters (to 20 liters)
# Test driving too far
print(my_car.drive(300)) # Should return an error
# After Activity 1: Add Mileage Tracking
print(my_car.getMileage())
print(my_car.drive(150))
print(my_car.getMileage())
# After Activity 2: Oil Change Reminder
# print(my_car.refuel(10000))
# print(my_car.oilChange()) # Should return False
# print(my_car.drive(5000))
# print(my_car.oilChange()) # Shuold return True
# After Activity 3: Challenge
# print(my_car.drive(100))
# my_car.setFuelEff(40)
# print(my_car.drive(100))
# Did you use the min function in the refuel method? If so why?

# I have no idea why anybody in the whole wide world use this function

# What happens if the fuel_level becomes negative?

# it'll never be negative because of if/elses in drive method

# How can this simulation be used in real-world applications like video game design?

# cars in video games cuold use a similar program to track stuff