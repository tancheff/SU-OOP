class Vehicle:
    def __init__(self, mileage: int, max_speed: int = 150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

    def get_info(self):
        return f"mileage: {self.mileage}, max_speed: {self.max_speed}"

    def __str__(self):
        return self.max_speed + " " + self.mileage

car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

Peugeot = Vehicle(15000, 120)

print(Peugeot.get_info())
print(Vehicle)
print(Peugeot.__str__())
