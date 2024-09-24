from abc import ABC, abstractmethod


class Supply(ABC):
    # TYPES = ["Food", "Drink"]

    def __init__(self, name: str, energy: int):
        self.name = name  # => равно е на метода @props
        self.energy = energy  # => равно е на метода @props
        self.type = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")

        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.__energy = value

    @abstractmethod
    def details(self) -> str:
        pass
