from computer_types.computer import Computer


class Laptop(Computer):

    @property
    def type(self):
        return "laptop"

    @property
    def desktop_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    @property
    def max_ram(self):
        return 64

    min_RAM = 2
    max_RAM = 64
    available_RAM = [2, 4, 8, 16, 32, 64]

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0
