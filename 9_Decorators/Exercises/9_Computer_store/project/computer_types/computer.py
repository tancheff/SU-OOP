from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0

        if len(manufacturer.strip()) == 0:
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self.manufacturer = manufacturer

        if len(model.strip()) == 0:
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self.model = model

    @property
    @abstractmethod
    def type(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self.__model = value

    @staticmethod
    def power_of_two(ram: int):
        if log2(ram).is_integer():
            return True

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor}is not compatible with desktop "
                             f"computer {self.manufacturer} {self.model}!")

        if self.power_of_two(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop "
                             f"computer {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def set_parts(self, processor: str, ram: int):
        ram_price = 100 * log2(ram)
        processor_price = self.available_processors[processor]

        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price

    @abstractmethod
    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
