from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def drive(self, distance: int):
        req_fuel = (self.fuel_consumption + self.__class__.AIR_CONDITIONER) * distance
        if self.fuel_quantity >= req_fuel:
            self.fuel_quantity -= req_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER = 1.6
    PERCENTAGE_FILL = 0.95

    def drive(self, distance: int):
        req_fuel = (self.fuel_consumption + self.__class__.AIR_CONDITIONER) * distance
        if self.fuel_quantity >= req_fuel:
            self.fuel_quantity -= req_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * self.__class__.PERCENTAGE_FILL


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print()
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

