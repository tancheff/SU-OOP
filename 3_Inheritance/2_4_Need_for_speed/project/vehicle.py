class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers) -> None:
        needed_fuel = kilometers * self.fuel_consumption
        if needed_fuel <= self.fuel:
            self.fuel -= needed_fuel
