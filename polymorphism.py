# Base class: Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Subclass: Dog
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Subclass: Fish
class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create instances of Animal and Vehicle subclasses
dog = Dog()
fish = Fish()
car = Car()
plane = Plane()

# Demonstrating polymorphism: each object uses its own version of move()
print("Animal Movements:")
dog.move()   # Running 🐕
fish.move()  # Swimming 🐟

print("\nVehicle Movements:")
car.move()   # Driving 🚗
plane.move() # Flying ✈️
