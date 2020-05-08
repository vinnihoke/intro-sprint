# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# BASE
class Vehicle:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class GroundVehicle(Vehicle):
    def __init__(self, name, desc, wheels, fuel):
        super().__init__(name, desc)
        self.wheels = wheels
        self.fuel = fuel

class Car(GroundVehicle):
    def __init__(self, name, desc, wheels, fuel, bodytype):
        super().__init__(name, desc, wheels, fuel)
        self.bodystyle = bodystyle

class Motorcycle(GroundVehicle):
    def __init__(self, name, desc, wheels, fuel, purpose):
        super().__init__(name, desc, fuel, wheels)
        self.purpose = purpose

class FlightVehicle(Vehicle):
    def __init__(self, name, desc, purpose):
        super().__init__(name, desc)
        self.purpose = purpose

class Airplane(FlightVehicle):
    def __init__(self, name, desc, purpose, commuter, comfort):
        super().__init__(name, desc, purpose)
        self.commuter = commuter
        self.comfort = comfort

class Starship(FlightVehicle):
    def __init__(self, name, desc, purpose, transport):
        super().__init__(name, desc, purpose)
        self.transport = transport