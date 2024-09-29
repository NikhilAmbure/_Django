# Constructor override

class Vehicle:

    def __init__(self):
        self.vehicle_name = "TATA"
        print('Vehicle Constructor')

    def can_ride(self):
        print("I can ride")


class Car(Vehicle):

    # To resolve constructor overriding
    # def __init__(self):
    #     self.vehicle_name = "TATA"
    #     print('Car Constructor')

    def get_car(self):
        print("Get Car")
    
car = Car()
print(car.get_car())